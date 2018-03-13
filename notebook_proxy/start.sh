envsubst '$MAIN_HOST,$MAIN_PORT,$PATH_REGEX' < /etc/nginx/conf.d/pythonathon.template > /etc/nginx/conf.d/default.conf &&
cat /etc/nginx/conf.d/default.conf &&
nginx -g 'daemon off;'