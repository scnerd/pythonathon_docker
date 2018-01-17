#c.Application.log_level = 30

c.JupyterHub.admin_access = True

c.JupyterHub.answer_yes = False

from oauthenticator.generic import LocalGenericOAuthenticator
c.JupyterHub.authenticator_class = LocalGenericOAuthenticator

import os
client_id = open(os.environ['OAUTH_CLIENT_ID_PATH']).read().strip()
print('ID: ' + client_id)
c.LocalGenericOAuthenticator.client_id = client_id
c.LocalGenericOAuthenticator.client_secret = open(os.environ['OAUTH_CLIENT_SECRET_PATH']).read().strip()
c.LocalGenericOAuthenticator.create_system_users = True

## The base URL of the entire application
c.JupyterHub.base_url = os.environ.get('JUPYTERHUB_PATH', '/')

c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=open(os.environ['POSTGRES_PASSWORD_FILE']).read().strip(),
    db=os.environ['POSTGRES_DB'],
)

c.JupyterHub.ip = '0.0.0.0'

# c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# # c.DockerSpawner.container_image = os.environ.get('DOCKER_NOTEBOOK_IMAGE')
#
# network_name = os.environ['DOCKER_NETWORK_NAME']
# c.DockerSpawner.use_internal_ip = True
# c.DockerSpawner.network_name = network_name
# c.DockerSpawner.extra_host_config = {'network_mode': network_name}
# c.DockerSpawner.remove_containers = True
#
# notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
# c.DockerSpawner.notebook_dir = notebook_dir
# c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
# c.DockerSpawner.extra_create_kwargs.update({ 'volume_driver': 'local' })
#
# c.DockerSpawner.debug = True

c.Spawner.default_url = '/lab'  # Why doesn't this work?
c.Spawner.args = ['--NotebookApp.allow_origin=*']

c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080

c.Spawner.cpu_limit = 0.25

c.Spawner.mem_limit = '256M'

c.Authenticator.admin_users = set(os.environ.get('ADMINS', '').split(','))

c.Authenticator.auto_login = True