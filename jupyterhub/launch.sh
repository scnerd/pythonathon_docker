#!/usr/bin/env sh

set -ex

sleep 4
jupyterhub upgrade-db
jupyterhub -f /srv/jupyterhub/jupyterhub_config.py