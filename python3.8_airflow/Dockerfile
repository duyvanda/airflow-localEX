FROM python:3.8.12-buster
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV TZ="Asia/Bangkok"

COPY ./constraints-3.8.txt /constraints-3.8.txt

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
    # https://github.com/apache/airflow/blob/main/Dockerfile
    apt-transport-https \
    apt-utils \
    build-essential \
    ca-certificates \
    gnupg \
    dirmngr \
    freetds-bin \
    freetds-dev \
    gosu \
    krb5-user \
    ldap-utils \
    libffi-dev \
    libkrb5-dev \
    libldap2-dev \
    libpq-dev \
    libsasl2-2 \
    libsasl2-dev \
    libsasl2-modules \
    libssl-dev \
    locales  \
    lsb-release \
    nodejs \
    openssh-client \
    postgresql-client \
    # python-selinux \
    sasl2-bin \
    software-properties-common \
    sqlite3 \
    sudo \
    unixodbc \
    unixodbc-dev \
    yarn \
    # install python3 & pip
    python3 \
    python3-pip \
    python3-setuptools \
    # for pyodbc
    python3-dev default-libmysqlclient-dev build-essential \
    # utils
    zip \
    unzip \
    gcc \
    vim \
    nano \
    curl \
    rsync \
    netcat \
    wget \
    tzdata \
    # install driver
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update -yqq \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get install -y unixodbc-dev \
    && apt-get install -y libgssapi-krb5-2 \
    # clean up
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base \
    && pip3 install apache-airflow[postgres,google,crypto,mssql,mysql,odbc,tableau,spark,jdbc,ssh,celery,redis]==2.1.3 --constraint /constraints-3.8.txt

RUN apt-get update \
    && apt-get install -y openjdk-11-jdk \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base
