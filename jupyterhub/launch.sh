#!/usr/bin/env sh
set +e
jupyterhub upgrade-db;
set -e
jupyterhub -f /srv/jupyterhub/jupyterhub_config.py