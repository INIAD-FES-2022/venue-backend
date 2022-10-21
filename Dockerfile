FROM python:3.10.6

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/images

RUN pip install --upgrade pip
COPY ./.env /usr/src/app/.env
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn

CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "config.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]
