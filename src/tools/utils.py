from fabric import Connection
from django.conf import settings


def local(command, flag):

    if '127' in flag:
        pyer = 'longmeier'
        pwd = '1234'
    else:
        pyer = 'pyer'
        pwd = settings.TST_PYER_PWD
    c = Connection(
        host="127.0.0.1",
        user=pyer,
        connect_kwargs={
            "password": pwd,
        },
    )
    c.cd('/home/data/tmp')
    res = c.run('ls')
    res = c.run('rm -rf aa')