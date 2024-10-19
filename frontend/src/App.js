import React, { useState } from 'react';

function App() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const calculateRPN = async () => {
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
    try {
      const response = await fetch(`${apiUrl}/calculate/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression }),
      });

      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
        setError('');
      } else {
        setError(data.detail || 'Une erreur est survenue');
      }
    } catch (err) {
      setError('Impossible de se connecter à l\'API');
    }
  };

  const exportCalculations = () => {
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
    window.open(`${apiUrl}/export/`, '_blank');
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Calculatrice RPN</h1>
      <input
        type="text"
        value={expression}
        onChange={(e) => setExpression(e.target.value)}
        placeholder="Entrez l'expression en NPI"
      />
      <button onClick={calculateRPN}>Calculer</button>
      {result !== null && (
        <div>
          <h2>Résultat : {result}</h2>
        </div>
      )}
      {error && (
        <div style={{ color: 'red' }}>
          <p>{error}</p>
        </div>
      )}
      <div style={{ marginTop: '20px' }}>
        <button onClick={exportCalculations}>Exporter les Calculs en CSV</button>
      </div>
    </div>
  );
}

export default App;
