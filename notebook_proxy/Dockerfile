FROM nginx:alpine

COPY start.sh /usr/bin/start.sh
RUN chmod +x /usr/bin/start.sh
COPY pythonathon.template /etc/nginx/conf.d/pythonathon.template

CMD /bin/sh /usr/bin/start.sh