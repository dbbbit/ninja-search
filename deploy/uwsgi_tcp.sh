#!/bin/bash
uwsgi --http :9090 --wsgi-file index.py --callable app --master --processes 4  --stats 127.0.0.1:9191
