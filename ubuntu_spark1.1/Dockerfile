FROM duyvanda/pyspark:1.0
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV SPARK_HOME=/usr/local/spark/spark-3.1.2-bin-hadoop3.2
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3
ENV SPARK_HOME_PYTHON=/usr/local/spark/spark-3.1.2-bin-hadoop3.2/python
ENV PYTHONPATH=$PYTHONPATH:$SPARK_HOME_PYTHON
ENV PATH=$PATH:$SPARK_HOME/bin

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && mkdir -p usr/local/spark \
    && mkdir -p usr/local/spark/logs \
    && wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz \
    && tar -xzf spark-3.1.2-bin-hadoop3.2.tgz \
    && mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark \
    && rm spark-3.1.2-bin-hadoop3.2.tgz

# RUN apt-get install -yqq --no-install-recommends nano \
#     && python3 -m pip install findspark==1.4.2 \
#     && python3 -m pip install py4j==0.10.9