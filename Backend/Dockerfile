FROM ubuntu:18.04

# Install Django 
RUN apt update && apt install -y python3 python3-pip vim && python3 -m pip install Django 

# Map code base to host 
RUN mkdir /autocompletion
VOLUME ["/autocompletion"]

# expose port
RUN apt install -y ufw && ufw allow 8000
EXPOSE 8000

WORKDIR /autocompletion 
CMD ["python3","manage.py","runserver"]
