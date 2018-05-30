FROM jupyterhub/jupyterhub:0.9.0.dev

ADD requirements.txt .
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install -r requirements.txt && \
    rm requirements.txt && \
    apt-get autoremove -y gcc && \
    apt-get clean

ADD launch.sh /usr/bin/launch.sh

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD /usr/bin/launch.sh
