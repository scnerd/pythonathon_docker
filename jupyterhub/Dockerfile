FROM jupyterhub/jupyterhub:0.9.0.dev

ADD requirements.txt .
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install -r requirements.txt && \
    rm requirements.txt && \
    apt-get autoremove -y gcc && \
    apt-get clean

ADD dockerspawner /dockerspawner
RUN pip install -e /dockerspawner

ADD launch.sh /usr/bin/launch.sh

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# TODO: This is a temporary patch for buggy migration in jupyterhub docker image. It'll probably be fixed in 0.9.1+
ADD "https://github.com/jupyterhub/jupyterhub/raw/master/jupyterhub/alembic/versions/99a28a4418e1_user_created.py" "/opt/conda/lib/python3.5/site-packages/jupyterhub/alembic/versions/99a28a4418e1_user_created.py"

CMD /usr/bin/launch.sh