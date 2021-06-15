FROM ubuntu:18.04
LABEL maintainer="PYTHON"
WORKDIR /app/
RUN apt update
RUN apt install python3 -y
RUN apt-get -y install python3-pip
RUN pip3 install FLask
RUN pip3 install -U Flask-SQLAlchemy
RUN pip3 install pymysql
RUN apt-get -y install mysql-client

COPY mainApp.py ./
COPY appConnection.py ./
COPY User.py ./
COPY constants.py ./
COPY testFlask.py ./
EXPOSE 5000

#ENTRYPOINT ["./mainApp.py"]
CMD ["python3" , "mainApp.py"]
#ENTRYPOINT ["mainApp"]
#CMD ["mainApp.py"]