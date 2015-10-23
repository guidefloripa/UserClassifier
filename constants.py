#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Guilherme Steinmann

from os import getcwd

# root where the logs are stored
kRootPath = getcwd()

# folder where the user grouped files are stored
kGroupFolder = 'users_grouped'

# folder where the sorted files are stored
kSortedFolder = 'users_sorted'

# filename of the log file
kLogFilename = 'apache.log'

# number of servers simulated
kNumServers = 5

# number of userids generated
kNumUsers = 6

# number of records generated per server
kNumLogsPerServer = 3000

# server names
servers = ['server0' + str(i+1) for i in range(kNumServers)]
