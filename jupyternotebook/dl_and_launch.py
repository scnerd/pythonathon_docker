#!/usr/bin/env python

import os
import re
import requests
import time
import logging

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

print("=" * 80)
print("{} successfully running".format(__file__))
print("=" * 80)

directory = os.path.expanduser(os.environ.get('FILES_DIR', '~/work/files'))
pythonathon_host = os.environ['PYTHONATHON_HOST']
retrieved = {}

log.debug("Writing files to {directory}".format(**locals()))
log.debug("Getting files from {pythonathon_host}".format(**locals()))

if not os.path.exists(directory):
    log.debug("Creating question file directory")
    os.makedirs(directory)

def sync_fs():
    global retrieved
    bad_keys = []
    for key, f in retrieved.items():
        if not os.path.exists(os.path.join(directory, f)):
            log.info("File '{}' (id={}) not found on disk, removing from memorized cache".format(key, f))
            bad_keys.append(key)
    for key in bad_keys:
        del retrieved[key]

def sync_with_server():
    global retrieved
    dl_url = "http://{}/dl/".format(pythonathon_host)
    for key in requests.get(dl_url + 'all').json()['file_ids']:
        if key not in retrieved:
            resp = requests.get(dl_url + str(key))
            if resp.status_code == 200:
                mtch = re.search('filename="?([\w\.]+)"?', resp.headers.get('content-disposition', ''))
                path = mtch.group(1) if mtch else str(key)
                path = os.path.join(directory, path)
                retrieved[key] = path
                open(path, 'wb').write(resp.content)
                log.info("Downloaded new file {} ({} bytes)".format(path, len(resp.content)))

while True:
    log.info("Checking for changes to question files")
    sync_fs()
    sync_with_server()
    time.sleep(5)
