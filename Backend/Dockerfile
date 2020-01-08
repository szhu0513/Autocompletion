FROM ubuntu:18.04

# Install Django 
RUN apt update && apt install -y python3 python3-pip vim && python3 -m pip install Django 

# expose port
EXPOSE 8000

# Map code base to host 
RUN mkdir /autocompletion
VOLUME ["/autocompletion"]

WORKDIR /autocompletion 
CMD ["python3","manage.py","runserver","0:8000"]
