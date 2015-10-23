#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Guilherme Steinmann

from constants import *

import os
import random
from uuid import uuid4
from datetime import datetime, timedelta
import time

users = {}
resources = ['/index.html', '/meme.jpg', '/lolcats.jpg']

if __name__ == "__main__":
    # create userId linked to userIp
    for i in range(kNumUsers):
        userId = str(uuid4())
        userIp = ".".join(map(str, (random.randint(100, 255) for i in range(4))))
        users[userId] = userIp

    # generate serverXX.log
    for server in servers:
        print 'Generating log for server %s...' % server,

        path = os.path.join(kRootPath, server)
        time = datetime(2015, 10, 1, 0, 0, 0)
        if not os.path.exists(path):
            os.makedirs(path)

        filename = os.path.join(path, kLogFilename)
        with open(filename, 'w') as f:
            for i in range(kNumLogsPerServer):
                time += timedelta(seconds=(random.randint(1,10))) # randomize delta
                userId = random.choice(users.keys()) # randomize user

                data = str(users[userId])
                data += ' - - '
                data += datetime.strftime(time,'[%d/%b/%Y:%H:%M:%S -0300]')
                data += ' "GET ' + random.choice(resources) + ' HTTP/1.1"' # randomize resource
                data += ' 200 2148 "-"'
                data += ' "userid=' + userId + '"'
                print >> f,data

        print 'ok'