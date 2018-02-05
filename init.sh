#!/usr/bin/env bash

set -ex

mkdir -p secrets ctf_data/db_backups ctf_data/files ctf_data/restore oauth db_data

cat /dev/urandom | tr -dc 'a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_' | fold -w 32 | head -n 1 > secrets/db_password