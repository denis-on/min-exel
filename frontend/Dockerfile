FROM node:20

WORKDIR /app

COPY package.json ./
RUN npm install && \
    npm install --save-dev @types/react @types/react-dom

COPY . .

RUN npm run build

FROM nginx:alpine
COPY --from=0 /app/build /usr/share/nginx/html
EXPOSE 80
