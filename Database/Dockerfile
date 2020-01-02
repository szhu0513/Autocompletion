FROM mongo:4.2.2-bionic

# apply local configuration 
COPY ./mongod.conf /etc/mongod.conf

# create user and password
ENV MONGO_INITDB_ROOT_USERNAME autocompletion_user
ENV MONGO_INITDB_ROOT_PASSWORD 000

# expose port
EXPOSE 27017

# map data file to local
RUN mkdir /db_log /database
VOLUME ["/database","/db_log"]

# start mongodb with specified configuration file
CMD ["mongod","--config","/etc/mongod.conf"]
