FROM mongo:4.2.2-bionic
# apply local configuration 
COPY ./mongod.conf /etc/mongod.conf

# expose port
EXPOSE 27017

# map data file to local
RUN mkdir /db_log /database
VOLUME ["/database","/db_log"]

# start mongodb with specified configuration file
CMD ["mongod","--config","/etc/mongod.conf"]
