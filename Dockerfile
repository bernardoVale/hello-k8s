FROM python:3.6-alpine
ADD requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app
ADD . .

ARG APP_VERSION
RUN echo $APP_VERSION > version.txt

CMD python app.py