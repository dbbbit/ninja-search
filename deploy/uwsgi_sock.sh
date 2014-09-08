#!/bin/bash
sudo mkdir -p /var/log/ninja-search
sudo uwsgi -s /tmp/uwsgi.sock --module index --callable app --master --processes 4  \
    --daemonize /var/log/ninja-search/uwsgi_server.log
