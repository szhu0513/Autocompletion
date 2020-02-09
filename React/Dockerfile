# specify the node base image with your desired version node:<version>
FROM ubuntu:18.04
# Using Ubuntu
RUN apt update && apt-get install -y curl && curl -sL https://deb.nodesource.com/setup_13.x | bash - && apt update && apt-get install -y nodejs
# replace this with your application's default port
EXPOSE 3000
VOLUME ["/react"]
WORKDIR /react/my-app
CMD ["npm", "start"]
