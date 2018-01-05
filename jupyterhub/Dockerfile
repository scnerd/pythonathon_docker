FROM jupyterhub/jupyterhub

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install psycopg2 && \
    apt-get autoremove -y gcc

ADD oauth/oauth_client_id /oath/oauth_client_id
ENV OAUTH_CLIENT_ID_PATH /oath/oauth_client_id

ADD oauth/oauth_client_secret /oath/oauth_client_secret
ENV OAUTH_CLIENT_SECRET_PATH /oath/oauth_client_secret

RUN pip install dockerspawner oauthenticator

ADD launch.sh /usr/bin/launch.sh
RUN chmod +x /usr/bin/launch.sh

ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD /usr/bin/launch.sh