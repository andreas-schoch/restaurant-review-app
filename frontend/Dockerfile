FROM node

WORKDIR /frontend
COPY package.json /app/frontend

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "start"]
