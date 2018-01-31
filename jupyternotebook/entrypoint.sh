#!/usr/bin/env sh

set -ex

dl_and_launch.py &
start-notebook.sh $@