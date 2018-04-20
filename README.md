# Pythonathon

The Pythonathon is a question/answer CTF for learning how to program, primarily in Python; in practice, it could support any textual question/answer competition, and the included JupyterHub could launch notebooks for any language supported by Jupyter Notebook. This codebase makes and attempt to run the entire competition from a fairly minimal server (1 CPU, 1 GB RAM, 4-8 GB disk), permitting a virtually one-click deployment of a coding competition in nearly any environment (even, potentially, a raspberry pi).

[I host a currently running version of this system for demonstration purposes.](https://pythonathon.davidmaxson.name/)

## TODO:

Enable loading questions on first run from a dump file

# Pythonathon_Docker

This repository brings together the [Pythonathon web application](https://github.com/scnerd/pythonathon_v3) and all the additional services needed to make the application run properly. This includes:

* An Nginx proxy to protect the web application and leverage its high-performance uWSGI protocol
* A PostgreSQL server to process and persist the database for the web application
* A JupyterHub server to permit isolated code execution on the Pythonathon server (this also leverages the same Postgres server for its own database)

SSL termination is not handled within this service composition; however, all the configuration is in place to use the [automated proxy](https://github.com/jwilder/nginx-proxy) with its [LetsEncrypt companion service](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion). If these two services are running on the same network as the proxy above, then it will automatically configure the Proxy connection and SSL termination and transparently forward the appropriate traffic (determined by the VIRTUAL_HOST name in this proxy's docker-compose environment variables). Without some SSL termination, this `docker-compose` file will by default permit HTTP on port 8000. The JupyterHub service is accessed through this same proxy under `/notebook/`. 

# Installation

You'll first need to [install docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/). Pythonathon is intended to be run in a Docker Swarm to allow easy scaling of the Jupyter notebooks that can get launched during the competition. If you're executing on a single physical machine, you can easily start up a swarm using `docker swarm init`. If you need to not run this within a swarm, see [the directions below](#Without Swarm mode).

Before first launch, make sure to run `init.sh` to generate the needed directories, as well as a random database password.

You'll also need to create the needed networks. There are three: webnet, that will have contact with the internet; ctfnet, which all the main servers will run on (this will get created automatically); and jupyternet, where the Jupyter notebooks will get launched to isolate them from the core servers. You can create these networks using the following commands:

```bash
docker network create --driver overlay webnet
docker network create --driver overlay ctfnet
docker network create --driver overlay jupyternet
```

You can then pull and launch all necessary images by simply executing `deploy.sh`.

## Without Swarm mode

There are a few changes necessary to launch this server using docker-compose instead of docker swarm.

* Change `SwarmSpawner` to `DockerSpawner` in `jupyterhub/jupyterhub_config.py`
* Create the docker networks without `--driver overlay`
* In `deploy.sh`, just use `docker-compose -f docker-compose.yml -f production.yml up -d` to launch the containers. You can either use `--build` to build the containers yourself or keep the `docker-compose pull` line to pull them from Docker Hub.

Still make sure to run `init.sh`, and with these changes you can still use `deploy.sh` to run the competition.

# Configuration

Most configuration options are made via the `docker-compose.yml` file. Every effort has been made to make this project self-contained and one-click launch using Docker to handle all the dirty work.

## Admin account

When you first launch the Pythonathon suite, it creates an adminstrator user:

Username: admin

Password: admin

The first thing you should do is log into your server by going to the home page, going to "Sign in" at the top, and logging in as the admin. Then, go to the "Admin" link on the top bar to enter the administrative console, go to Users -> admin. Change your username to whatever you'd like, then hit "Save" at the bottom. Then, click "Change Password" in the upper right hand corner of the admin console and change your password.

At any point, you can go back to the Users pane and add other administrators. From here you can also curate which users have which permissions; give them staff status to allow them to log into the admin console, and give them individual permissions as desired for them to create questions, categories, etc.

Note that the JupyterHub and Pythonathon are two distinct servers with distinct logins. They use OAuth2 to make sharing credentials nearly seamless, but most significantly, being an admin on one server does not mean that you're an admin on the other. If you change your Pythonathon admin name, then change the username in `docker-compose.yml` `jupyterhub -> environment -> ADMINS` and re-launch the servers. You can also leave this field blank if you don't need administrative privileges on the JupyterHub server.

## JupyterHub

The Pythonathon suite comes with a built-in Jupyter Hub. This is a server that users can log into to get their own dedicated Jupyter Notebook servers. These servers launch as additional docker containers; this allows each user to have essentially "admin" control of their server without any ability to trample on other users or the main Pythonathon servers.

The Hub piggy-backs on the main Pythonathon login system using OAuth2. Once you have the system up and running, go to ```/o/applications```, log in as a superuser on the Pythonathon server, and create an OAUTH application for JupyterHub. In my case, the redirection urls are:

    https://pythonathon.davidmaxson.name/notebook/hub/oauth_callback
    http://localhost:8000/notebook/hub/oauth_callback

You can then copy the generated ID and Secret into their respective jupyterhub/oauth files as plain text. Relaunch the servers to get these to load into the JupyterHub properly.

## Recaptcha

Recaptcha support can be enabled by adding `/secrets/recaptcha_public` and `/secrets/recaptcha_private` files with your site and private keys. You can get these keys by registering your site with Google's Recaptcha service.

## Email

Email support can be enabled by adding `secrets/gmail_user` and `secrets/gmail_password` files with your Gmail username and password. I'd suggest creating a purpose-made noreply address for these purposes. You can also edit `pythonathon_v3/pythonathon_v3/settings.py` to configure your own email service.

