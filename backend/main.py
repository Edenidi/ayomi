from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import database  # Importer le fichier de base de données
from fastapi.middleware.cors import CORSMiddleware

# Initialiser l'application FastAPI
app = FastAPI()

# Middleware CORS pour permettre les requêtes du frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Créer la base de données au démarrage de l'application
@app.on_event("startup")
def startup():
    database.init_db()

# Modèle Pydantic pour la validation de l'expression
class ExpressionInput(BaseModel):
    expression: str

# Calcul de la Notation Polonaise Inverse (RPN)
def rpn_calculator(expression: str) -> float:
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(num1 / num2)
            else:
                raise ValueError(f"Unknown operator: {token}")

    return stack[0]

# Dépendance pour obtenir la session de base de données
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route POST pour traiter le calcul RPN
@app.post("/calculate/")
def calculate_rpn(expression_input: ExpressionInput, db: Session = Depends(get_db)):
    try:
        result = rpn_calculator(expression_input.expression)

        # Sauvegarder le calcul dans la base de données
        calc = database.Calculation(expression=expression_input.expression, result=result)
        db.add(calc)
        db.commit()
        db.refresh(calc)

        return {"expression": expression_input.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route GET pour exporter les calculs en CSV
from fastapi.responses import StreamingResponse
from io import StringIO
import csv

@app.get("/export/")
def export_calculations(db: Session = Depends(get_db)):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Expression", "Result"])

    calculations = db.query(database.Calculation).all()

    for calc in calculations:
        writer.writerow([calc.id, calc.expression, calc.result])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=calculations.csv"})
