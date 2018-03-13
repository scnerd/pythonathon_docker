FROM jupyterhub/jupyterhub

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev && \
    pip install psycopg2 && \
    apt-get clean

ADD launch.sh /usr/bin/launch.sh
RUN chmod +x /usr/bin/launch.sh

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ADD dockerspawner /dockerspawner
RUN pip install -e /dockerspawner

CMD /usr/bin/launch.sh