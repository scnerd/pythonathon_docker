#!/usr/bin/env sh

set -ex

echo "Running $@" >> ent.log

dl_and_launch.py &

exec "$@"