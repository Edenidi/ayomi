# Utiliser une image de base Node.js
FROM node:16

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier package.json et installer les dépendances
COPY package.json ./
RUN npm install

# Copier tout le code de l'application dans le conteneur
COPY . .

# Construire le projet pour la production
RUN npm run build

# Exposer le port 3000 pour le frontend React
EXPOSE 3000

# Démarrer le serveur de développement React
CMD ["npm", "start"]
