FROM node:20-alpine

WORKDIR /app

# Copy dependency definitions first to leverage layer cache
COPY package.json package-lock.json* ./

RUN npm install

# Copy application source code
COPY . .

EXPOSE 5173

# Vite requires --host to accept connections from outside the container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]