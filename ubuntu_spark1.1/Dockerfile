FROM duyvanda/pyspark:1.0
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && mkdir -p usr/local/spark \
    && wget https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz \
    && tar -xzf spark-3.2.0-bin-hadoop3.2.tgz \
    && mv spark-3.2.0-bin-hadoop3.2 /usr/local/spark \
    && rm spark-3.2.0-bin-hadoop3.2.tgz

RUN apt-get install -yqq --no-install-recommends nano \
    && python3 -m pip install findspark==1.4.2 \
    && python3 -m pip install py4j==0.10.9.2