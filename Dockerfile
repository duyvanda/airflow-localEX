FROM ubuntu:18.04
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

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

COPY ./constraints-3.6.txt /constraints-3.6.txt
COPY ./requirements.txt /requirements.txt

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        gnupg \
        ca-certificates \
        wget \
        libczmq-dev \
        inetutils-telnet \
        bind9utils freetds-dev \
        libkrb5-dev \
        freetds-bin build-essential \
        apt-utils \
        zip \
        unzip \
        gcc \
        vim \
        python3 \
        python3-pip \
        krb5-user \
        ldap-utils \
        libffi6 \
        libsasl2-2 \
        libsasl2-modules \
        libssl1.1 \
        lsb-release \
        sasl2-bin \
        sqlite3 \
        unixodbc \
        freetds-bin \
        apt-utils \
        curl \
        rsync \
        netcat \
        locales \
        unixodbc -y \
        unixodbc-dev -y \
        freetds-dev -y \
        freetds-bin -y \
        tdsodbc -y \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    # Install driver
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update -yqq \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
    && python3 -m pip install -U pip \
    && pip install --upgrade pip \
    && pip install -U pip setuptools wheel \
    && pip install pytz \
    && pip install pyOpenSSL \
    && pip install ndg-httpsclient \
    && pip install pyasn1 \
    && apt-get install -y python3-dev default-libmysqlclient-dev build-essential \
    && pip install apache-airflow[async,postgres,google,crypto,s3,mssql,mysql,odbc]==2.1.3 --constraint /constraints-3.6.txt  \
    # && pip install apache-airflow-providers-mysql \
    && pip install -r requirements.txt \
    && apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

# populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini
# COPY ./entrypoint.sh ./entrypoint.sh
# RUN chmod +x ./entrypoint.sh
# RUN chown -R airflow: ${AIRFLOW_HOME}
# USER airflow
# WORKDIR ${AIRFLOW_HOME}
# EXPOSE 8080
# ENTRYPOINT [ "/entrypoint.sh" ]

COPY ./entrypoint.sh /entrypoint.sh
COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
RUN chmod +x ./entrypoint.sh
RUN chown -R airflow: ${AIRFLOW_HOME}
EXPOSE 8080
USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD [ echo "executable" ]
