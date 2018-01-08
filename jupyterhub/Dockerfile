FROM jupyterhub/jupyterhub

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install psycopg2 && \
    apt-get autoremove -y gcc

RUN pip install dockerspawner oauthenticator

ADD launch.sh /usr/bin/launch.sh
RUN chmod +x /usr/bin/launch.sh

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD /usr/bin/launch.sh