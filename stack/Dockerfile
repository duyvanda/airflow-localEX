FROM duyvanda/airflow_mr:latest
LABEL maintainer="Puckel_"
# Run docker build -t ubuntu:airflow_stack .
# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV TZ="Asia/Bangkok"

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
RUN chmod +x ./entrypoint.sh
EXPOSE 8080
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD [ echo "executable" ]
