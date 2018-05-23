from __future__ import print_function

import json
import os
import sys


class JSONConfig:
    def __init__(self, config_file, namespace):
        self.config_file = config_file
        self.namespace = namespace
        try:
            with open(config_file, 'r') as content_file:
                content = content_file.read()
                self.config_json = json.loads(content)
        except Exception as e:
            print("WARNING: Could not read configuration file `{}`: {}\n" \
                    .format(self.config_file, str(e)),
                file=sys.stderr)

    def get(self, key, default=None, namespace=None):
        used_namespace = namespace if namespace else self.namespace
        value = default
        try:
            value = self.config_json[used_namespace].get(key, default)
        except AttributeError as e:
            pass
        except KeyError as e:
            print("WARNING: Namespace `{}` not found in config file\n" \
                .format(used_namespace), file=sys.stderr)
        return value
