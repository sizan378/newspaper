# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /app

# set level
LABEL maintainer='sizanmahmud08@gmail.com'
LABEL description="Development image for NewsPaper project"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . ./app
# install dependencies
# RUN apt-get update \
#   && apt-get install -y build-essential \
#   && apt-get install -y libpq-dev \
#   && apt-get install -y gettext \
#   && apt-get -y install netcat gcc postgresql \
#   && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  # && rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements/requirements.txt .
RUN pip3 install -r requirements.txt


EXPOSE 8000

CMD ["python", "manage", "runserver"]