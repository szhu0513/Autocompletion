FROM ubuntu:18.04 

# Install Django 
RUN apt update && apt install -y python3 python3-pip vim git && python3 -m pip install Django djongo sqlparse==0.2.4 

# Install MongoDB for Django
#RUN pip3 install git+https://github.com/django-nonrel/django@nonrel-1.5 && pip3 install git+https://github.com/django-nonrel/djangotoolbox && pip3 install git+https://github.com/django-nonrel/mongodb-engine

# expose port
EXPOSE 8000

# Map code base to host 
RUN mkdir /autocompletion
VOLUME ["/autocompletion"]

WORKDIR /autocompletion 
CMD ["python3","manage.py","runserver","0:8000"]
