FROM jupyterhub/jupyterhub-onbuild

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install psycopg2 cryptography && \
    apt-get autoremove -y gcc

ADD oauth/oauth_client_id /oath/oauth_client_id
ENV OAUTH_CLIENT_ID_PATH /oath/oauth_client_id

ADD oauth/oauth_client_secret /oath/oauth_client_secret
ENV OAUTH_CLIENT_SECRET_PATH /oath/oauth_client_secret

RUN pip install dockerspawner oauthenticator

ENTRYPOINT ["jupyterhub", "upgrade-db"]