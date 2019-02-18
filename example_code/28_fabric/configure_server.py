import os
import click

from fabric import Connection, Config


@click.command()
@click.option('--ip', help='IP address of the server to connect')
@click.option('--user', '-u', help='New user name to create')
def initial_server_setup(ip, user):
    # As soon as the server is created, we can log in as root
    c = Connection(ip, user='aquiles')

    # Lets create a user and add it to the sudoers group
    # c.run('adduser {}'.format(user))
    # c.run('usermod -aG sudo {}'.format(user))
    # c.run('su - {}'.format(user))
    # c.run('mkdir ~/.ssh')
    # c.run('chmod 700 ~/.ssh')
    # Lets create an ssh-key pair if it does not exist:
    ssh_dir = os.path.join(os.environ.get('HOME'), '.ssh')
    ssh_filename = os.path.join(ssh_dir, 'id_rsa')
    if not os.path.exists(ssh_dir):
        os.makedirs(ssh_dir)
        make_ssh_key(c, ssh_filename)
    else:
        if not os.path.isfile(ssh_filename):
            make_ssh_key(c, ssh_filename)

    # Upload the file to the server
    ssh_filename_pub = ssh_filename+'.pub'
    c.put(ssh_filename_pub, remote='/home/{}/'.format(user))
    c.run('cd /home/{}'.format(user))
    c.run('cat {} >> .ssh/authorized_keys'.format('id_rsa.pub'))

def make_ssh_key(c, ssh_file_path):
    c.local('ssh-keygen -f {}'.format(ssh_file_path))


if __name__ == '__main__':
    initial_server_setup()