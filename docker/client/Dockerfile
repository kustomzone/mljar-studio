FROM node:8.12.0-alpine

WORKDIR /app/client

COPY ./client/src /app/client/src
COPY ./client/public /app/client/public
COPY ./client/package.json /app/client
COPY ./client/server.js /app/client

ENV CLIENT_SERVER_PORT 5000
#ENV REACT_APP_MLJAR_URL http://0.0.0.0:8003

RUN npm install && npm run build

CMD ["node", "server.js"]