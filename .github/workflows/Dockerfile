# Use the official Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Add the config.txt file
COPY config.txt /app/config.txt

# Set the default command to display the contents of the config.txt file
CMD ["cat", "/app/config.txt"]
