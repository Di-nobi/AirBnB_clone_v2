#!/usr/bin/python3
""" A fabric script that distributes an archive to your
web servers"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ["34.203.29.12", "34.227.90.80"]
env.user = "ubuntu"

def do_pack():
    """
    return the archive path if achive is generated correctly
    """
    local("mkdir -p versions")
    datestamp = datetime.now().strftime("%Y%m%d%H%H%S")
    first_archive = "versions/web_static_{}.tgz".format(datestamp)
    archieved = local("tar -cvzf {} web_static".format(first_archive))

    if archieved.succeeded:
        return first_archived
    else:
        return None
def do_deploy(archive_path):
    """Deploying to server"""
    if os.path.exists(archive_path):
        ach_file = archive_path[9:]
        new_version = "/data/web_static/releases/" + ach_file[:-4]
        ach_file = "/tmp/" + ach_file
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}'.format(new_version))
        run('sudo tar -xzf {} -C {}/'.format(ach_file, new_version))
        run('sudo rm {}'.format(ach_file))
        run('sudo mv {}/web_static/* {}'.format(new_version, new_version))
        run('sudo rm -rf {}/web_static'.format(new_version))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(new_version))
        print("New version deployed")
        return True
    return False
