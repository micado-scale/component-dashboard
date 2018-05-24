#!/usr/bin/env python
from dashboard import app, init_application

if __name__ == "__main__":
    init_application(app)
    app.debug = True
    app.testing = True
    app.run(host="0.0.0.0", port="4000", threaded=True)

