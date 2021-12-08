FROM ubuntu:20.04
LABEL maintainer="Puckel_"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update \
    && apt-get install -y --no-install-recommends openjdk-11-jdk