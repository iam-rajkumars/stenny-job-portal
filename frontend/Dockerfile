# Step 1: Build the frontend with Vite
FROM node:20-alpine AS builder

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

# Step 2: Serve the build using Nginx
FROM nginx:alpine

# Copy custom Nginx config
#COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built frontend from builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

