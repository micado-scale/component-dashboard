#!/usr/bin/env python
from dashboard import app, init_application
from config import DebugConfiguration as config

if __name__ == "__main__":
    init_application(app, config)
    app.debug = config.DEBUG
    app.run(host=config.APP_HOST, port=config.APP_PORT, threaded=True)
