import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from '../App';

test('renders the RPN Calculator title', () => {
  render(<App />);
  const titleElement = screen.getByText(/Calculatrice RPN/i);
  expect(titleElement).toBeInTheDocument();
});

test('performs a calculation when the calculate button is clicked', async () => {
  render(<App />);
  
  const input = screen.getByPlaceholderText("Entrez l'expression en NPI");
  fireEvent.change(input, { target: { value: '3 4 +' } });
  
  const button = screen.getByText(/Calculer/i);
  fireEvent.click(button);
  
  const result = await screen.findByText(/Résultat : 7/i);
  expect(result).toBeInTheDocument();
});
