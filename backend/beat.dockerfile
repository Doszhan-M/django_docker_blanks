FROM python:3.10.2


EXPOSE 8000

RUN useradd -ms /bin/bash celery

WORKDIR /backend/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY backend/requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY backend/ /home/backend/

RUN chown -R celery:celery /backend/
USER celery

ENTRYPOINT celery -A root worker -l INFO -B
