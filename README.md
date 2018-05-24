# MiCADO Dashboard #
This component collects all the user interfaces (e.g., grafana,
docker-visualizer, prometheus) into a single dashboard.

## Usage: ##
```MICADO_FRONTEND_IP=192.168.154.95 gunicorn -b 0.0.0.0:4000 dashboard:app```

Where ```MICADO_FRONTEND_IP``` is the IP address of the MiCADO master node.
