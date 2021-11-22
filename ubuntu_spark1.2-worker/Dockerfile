FROM duyvanda/pyspark:1.1
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV CORES=3
ENV MEMORY=6G
ENV SPARK_MASTER_PORT 7077
ENV SPARK_MASTER_WEBUI_PORT 8081
ENV SPARK_MASTER_LOG /usr/local/spark/logs

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir -p usr/local/spark/logs

EXPOSE 8081
ENTRYPOINT $SPARK_HOME/bin/spark-class org.apache.spark.deploy.worker.Worker -c $CORES -m $MEMORY spark://172.17.0.2:7077
CMD [ echo "executable" ]