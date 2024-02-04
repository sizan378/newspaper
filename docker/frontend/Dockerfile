FROM node:alpine

WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY ./frontend/package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY ./frontend .

# Expose the port that the app runs on
EXPOSE 3000
