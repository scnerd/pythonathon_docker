#!/usr/bin/env sh

envsubst '$VIRTUAL_HOST,$MAIN_HOST,$MAIN_PORT,$HUB_HOST,$HUB_PORT,$HUB_PATH' < /etc/nginx/conf.d/pythonathon.template > /etc/nginx/conf.d/default.conf &&
cat /etc/nginx/conf.d/default.conf &&

nginx-debug -g 'daemon off;'