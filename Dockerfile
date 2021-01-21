# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5000

RUN useradd -m todoapi
USER todoapi

WORKDIR /home/todoapi

ENV TODOAPI_ENV=docker
ENV TODOAPI_REMOTE_DEBUG=on
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY --chown=todoapi:todoapi . ./
RUN pip install --upgrade pip \    
 && pip install -r requirements.txt
CMD ["gunicorn","todoapi:app", "-c", "todoapi/config/gunicorn_settings.py"]
