# ayomi
Calculatrice NPI
# Calculatrice RPN avec Backend FastAPI et Frontend React

Ce projet est une application complète de calculatrice en Notation Polonaise Inverse (RPN), comprenant :
- Un **backend** développé avec **FastAPI** pour gérer les calculs et les requêtes API.
- Un **frontend** développé avec **React** pour offrir une interface utilisateur intuitive.

## Fonctionnalités

- Calculs utilisant la notation polonaise inverse.
- Interface utilisateur conviviale pour entrer des expressions RPN et voir les résultats.
- Export des opérations sous forme de fichier CSV.
- Dockerisé pour un déploiement et une gestion simplifiés.

## Prérequis

- **Docker** et **Docker Compose** installés sur votre machine.
- **Git** pour cloner le dépôt (facultatif si vous avez téléchargé les fichiers directement).

## Structure du Projet

projet_technique/ ├── backend/ │ ├── main.py │ ├── requirements.txt │ ├── Dockerfile │ 
                  └── ... ├── frontend/ │ ├── src/ │ ├── package.json │ ├── Dockerfile │ └── ... ├── 
                  .gitignore ├── 
                  docker-compose.yml 
                  └── README.md
