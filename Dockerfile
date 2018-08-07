FROM python:2.7-slim

ENV MICADO_FRONTEND_IP 127.0.0.1

ARG EXPORT_DIR=/srv/micado-dashboard

COPY . ${EXPORT_DIR}
WORKDIR ${EXPORT_DIR}

RUN \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Application is always running on port 4000 in the container
EXPOSE 4000

CMD  ["gunicorn", "-b", "0.0.0.0:4000", "dashboard:app"]
