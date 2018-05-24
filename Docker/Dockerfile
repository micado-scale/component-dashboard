FROM python:2.7-slim

ENV MICADO_FRONTEND_IP 127.0.0.1

ARG GIT_BRANCH=master
ARG GIT_USER=micado-scale
ARG GIT_REPO=component-dashboard
ARG GIT_EXPORT_DIR=/srv/micado-dashboard

RUN \
    apt-get update && apt-get upgrade -y && apt-get install -y git

# Workaround for caching git clone
ADD https://api.github.com/repos/${GIT_USER}/${GIT_REPO}/git/refs/heads/${GIT_BRANCH} version.json
RUN \
    git clone -b ${GIT_BRANCH} https://github.com/${GIT_USER}/${GIT_REPO}.git ${GIT_EXPORT_DIR}

WORKDIR ${GIT_EXPORT_DIR}

RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN \
    apt-get remove --purge -y git && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache

# Application is always running on port 4000 in the container
EXPOSE 4000

CMD  ["gunicorn", "-b", "0.0.0.0:4000", "dashboard:app"]
