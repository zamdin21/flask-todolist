# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5000 3000
RUN apt update \
    && apt install -y sudo \
    && apt upgrade -y \
    && useradd -m app

USER app
WORKDIR /home/app

ENV TODOAPI_ENV=docker
# リモートデバッグを実行する場合はon、サーバ起動の場合はoff
ENV TODOAPI_REMOTE_DEBUG=off
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# 何故かuser installされるため、ユーザーローカルをPATHに追加
ENV PATH $PATH:/home/app/.local/bin

COPY requirements.txt ./
RUN pip install --upgrade pip \    
 && pip install -r requirements.txt
COPY --chown=app:app ./docker/app ./
CMD [ "python", "-m", "todoapi" ]
# CMD ["gunicorn","todoapi:app", "-c", "/home/app/gunicorn_settings.py"]