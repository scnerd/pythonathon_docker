# pythonathon_docker
A docker-compose wrapper around pythonathon to give it a database and SSL termination proxy

# Installation

To facilitate proper isolation, the whole Pythonathon system runs within an isolated network called and only exposes a single public-facing port on an external network called ```webnet```. To create this network, just execute:

    docker network create webnet

This way, other systems can exist on ```webnet``` without colliding with anything built within pythonathon. It also allows you to run an SSL-termination proxy on webnet, so that all of Pythonathon is agnostic to how you secure entry into its network.

By default, the system launches on and exposes port 8000.

You'll also need to initialize the OAUTH ID and Secret for the JupyterHub server to piggyback on the Pythonathon main server's authentication. Initially, just create two empty files in ```jupyterhub/oauth``` by copying the two template files and removing their suffixes. We'll need to create actual values, but we'll do that later.

# Initialization

## Admin account

When you first launch the Pythonathon suite, it creates an adminstrator user:

Username: admin

Password: admin

The first thing you should do is log into your server by going to the home page, going to "Sign in" at the top, and logging in as the admin. Then, go to the "Admin" link on the top bar to enter the administrative console, go to Users -> admin. Change your username to whatever you'd like, then hit "Save" at the bottom. Then, click "Change Password" in the upper right hand corner of the admin console and change your password.

At any point, you can go back to the Users pane and add other administrators. From here you can also curate which users have which permissions; give them staff status to allow them to log into the admin console, and give them individual permissions as desired for them to create questions, categories, etc.

## JupyterHub

The Pythonathon suite comes with a built-in Jupyter Hub. This is a server that users can log into to get their own dedicated Jupyter Notebook servers. These servers launch as additional docker containers; this allows each user to have essentially "admin" control of their server without any ability to trample on other users or the main Pythonathon servers.

The Hub piggy-backs on the main Pythonathon login system using OAuth2. Once you have the system up and running, go to ```/o/applications```, log in as a superuser on the Pythonathon server, and create an OAUTH application for JupyterHub. In my case, the redirection urls are:

    https://pythonathon.davidmaxson.name/notebook/hub/oauth_callback
    http://localhost:8000/notebook/hub/oauth_callback

You can then copy the generated ID and Secret into their respective jupyterhub/oauth files as plain text. Relaunch the servers to get these to load into the JupyterHub properly.


