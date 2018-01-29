FROM jupyterhub/jupyterhub

ADD requirements.txt .
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install -r requirements.txt && \
    rm requirements.txt && \
    apt-get autoremove -y gcc && \
    apt-get clean

ADD launch.sh /usr/bin/launch.sh
RUN chmod +x /usr/bin/launch.sh

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ADD dockerspawner /dockerspawner
RUN pip install -e /dockerspawner

CMD /usr/bin/launch.sh