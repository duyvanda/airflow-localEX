FROM duyvanda/pyspark:1.1
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV SPARK_HOME=/usr/local/spark/spark-3.2.0-bin-hadoop3.2
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python3
ENV SPARK_HOME_PYTHON=/usr/local/spark/spark-3.2.0-bin-hadoop3.2/python
ENV PYTHONPATH=$PYTHONPATH:$SPARK_HOME_PYTHON
ENV PATH=$PATH:$SPARK_HOME/bin