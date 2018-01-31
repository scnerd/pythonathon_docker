FROM jupyter/minimal-notebook

ARG PYTHONATHON_HOST
ARG FILES_DIR

ENV PYTHONATHON_HOST=$PYTHONATHON_HOST
ENV FILES_DIR=$FILES_DIR

ADD entrypoint.sh /usr/local/bin/
ADD dl_and_launch.py /usr/local/bin/

CMD ["entrypoint.sh"]
