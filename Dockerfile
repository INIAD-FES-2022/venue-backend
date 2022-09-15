FROM python:3.10.6-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/images

CMD ["touch", ".env"]
CMD ["echo", "SECRET_KEY=''", ">>", ".env"]
CMD ["echo", "DEBUG=False", ">>", ".env"]
CMD ["echo", "ALLOWED_HOST=['127.0.0.1']", ">>", ".env"]

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn


CMD ["gunicorn", "config.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]
