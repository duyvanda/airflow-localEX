FROM ubuntu:20.04
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=2.1.3
ARG AIRFLOW_USER_HOME=/usr/local/airflow
ARG AIRFLOW_DEPS=""
ARG PYTHON_DEPS=""
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}

COPY ./constraints-3.8.txt /constraints-3.8.txt

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
    # https://airflow.apache.org/docs/apache-airflow/2.1.3/installation.html
    freetds-bin \
    krb5-user \
    ldap-utils \
    # libffi6 \
    libsasl2-2 \
    libsasl2-modules \
    libssl1.1 \
    locales  \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc \
    # install python3 & pip
    python3 \
    python3-pip \
    # for pyodbc
    python3-dev default-libmysqlclient-dev build-essential \
    # utils
    apt-utils \
    zip \
    unzip \
    gcc \
    vim \
    curl \
    rsync \
    netcat \
    locales \
    gnupg \
    ca-certificates \
    wget \
    # install driver
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update -yqq \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get install -y unixodbc-dev \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base \
    # install airflow 2.2.2 (stable)
    && pip install apache-airflow[postgres,google,crypto,mssql,mysql,odbc,tableau]==2.2.2 --constraint /constraints-3.8.txt
