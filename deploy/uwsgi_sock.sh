#!/bin/bash
uwsgi -s /tmp/uwsgi.sock --module index --callable app --master --processes 4 --stats 127.0.0.1:9191
sudo chmod 777 /tmp/uwsgi.sock