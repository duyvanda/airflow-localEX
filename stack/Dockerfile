FROM duyvanda/airflow:3.2.0
LABEL maintainer="duyvanda"
# Run docker build -t ubuntu:airflow_stack .
# Run docker stack deploy --compose-file docker-compose.yml aiflow
# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Airflow
ARG AIRFLOW_VERSION=2.1.3
ARG AIRFLOW_USER_HOME=/usr/local/airflow
ARG AIRFLOW_DEPS=""
ARG PYTHON_DEPS=""
ENV AIRFLOW_HOME=${AIRFLOW_USER_HOME}
ENV PYARROW_IGNORE_TIMEZONE 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
COPY ./logs/* ${AIRFLOW_HOME}/logs/
RUN chmod +x ./entrypoint.sh
EXPOSE 8085
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]

# HEALTHCHECK --interval=30s --start-period=60s --retries=2 CMD -f /usr/local/airflow/airflow-webserver.pid
CMD [ echo "executable" ]
