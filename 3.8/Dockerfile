FROM duyvanda/airflow_mr:latest
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
# COPY ./logs/* ${AIRFLOW_HOME}/logs/
RUN chmod +x ./entrypoint.sh
EXPOSE 8080
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD [ echo "executable" ]
