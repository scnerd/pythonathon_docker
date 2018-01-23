import logging

c.Application.log_level = 30

log = logging.getLogger()

c.JupyterHub.admin_access = True

c.JupyterHub.answer_yes = False

from oauthenticator.generic import GenericOAuthenticator
c.JupyterHub.authenticator_class = GenericOAuthenticator

import os
client_id = open(os.environ['OAUTH_CLIENT_ID_PATH']).read().strip()
log.info('ID: ' + client_id)
c.GenericOAuthenticator.client_id = client_id
c.GenericOAuthenticator.client_secret = open(os.environ['OAUTH_CLIENT_SECRET_PATH']).read().strip()
# c.GenericOAuthenticator.create_system_users = True

## The base URL of the entire application
path = os.environ.get('JUPYTERHUB_PATH', '/')
c.JupyterHub.base_url = path
log.info("Launching under path '{}'".format(path))

c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=open(os.environ['POSTGRES_PASSWORD_FILE']).read().strip(),
    db=os.environ['POSTGRES_DB'],
)

c.JupyterHub.ip = '0.0.0.0'

c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'
c.SwarmSpawner.container_image = os.environ.get('DOCKER_NOTEBOOK_IMAGE')
c.SwarmSpawner.use_docker_client_env = True

network_name = os.environ['DOCKER_NETWORK_NAME']
c.SwarmSpawner.use_internal_ip = True
c.SwarmSpawner.network_name = network_name
c.SwarmSpawner.extra_host_config = {'network_mode': network_name}
c.SwarmSpawner.remove_containers = True

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.SwarmSpawner.notebook_dir = notebook_dir
# c.SwarmSpawner.volumes = {'notebooks/jupyterhub-user-{username}': notebook_dir}
# c.SwarmSpawner.extra_create_kwargs.update({'volume_driver': 'local'})

c.SwarmSpawner.debug = True

c.Spawner.default_url = '/lab'
c.Spawner.args = ['--NotebookApp.allow_origin=*']

c.JupyterHub.hub_ip = 'jupyterhub'
# c.JupyterHub.hub_port = 8080

c.Spawner.cpu_limit = 0.25

c.Spawner.mem_limit = '256M'

c.Authenticator.admin_users = set(os.environ.get('ADMINS', '').split(','))

c.Authenticator.auto_login = True