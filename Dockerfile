# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update\
    && apt-get install --no-install-recommends -y \
        libmemcached11 \
        libmemcachedutil2 \
        libmemcached-dev \
        libz-dev\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /code/

