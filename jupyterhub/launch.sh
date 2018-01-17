#!/usr/bin/env sh

sleep 4
set +e
jupyterhub upgrade-db;
set -e
jupyterhub -f /srv/jupyterhub/jupyterhub_config.py