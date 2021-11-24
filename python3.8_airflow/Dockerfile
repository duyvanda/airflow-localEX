FROM duyvanduy/airflow_mr:py2.1.3
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update && apt-get install -y openjdk-8-jdk