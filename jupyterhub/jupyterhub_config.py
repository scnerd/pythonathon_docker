#c.Application.log_level = 30

c.JupyterHub.admin_access = True

c.JupyterHub.answer_yes = False

from oauthenticator.generic import GenericOAuthenticator
c.JupyterHub.authenticator_class = GenericOAuthenticator

import os
client_id = open(os.environ['OAUTH_CLIENT_ID_PATH']).read().strip()
print('ID: ' + client_id)
c.GenericOAuthenticator.client_id = client_id
c.GenericOAuthenticator.client_secret = open(os.environ['OAUTH_CLIENT_SECRET_PATH']).read().strip()

## The base URL of the entire application
c.JupyterHub.base_url = os.environ.get('JUPYTERHUB_PATH', '/')

c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=open(os.environ['POSTGRES_PASSWORD_FILE']).read().strip(),
    db=os.environ['POSTGRES_DB'],
)

c.JupyterHub.ip = '0.0.0.0'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.host_ip = "0.0.0.0"

c.Spawner.cpu_limit = 0.25

c.Spawner.mem_limit = '256M'

c.Authenticator.admin_users = set(os.environ.get('ADMINS', '').split(','))

c.Authenticator.auto_login = True