#!/usr/bin/env bash

set -ex

makedir -p secrets ctf_data/db_backups ctf_data/files oauth db_data

cat /dev/urandom | tr -dc 'a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_' | fold -w 32 | head -n 1 > secrets/db_password