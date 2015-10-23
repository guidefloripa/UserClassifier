#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Guilherme Steinmann

from constants import kRootPath, kGroupFolder, kSortedFolder, servers, kLogFilename

import os
import Queue
import threading
import subprocess

from parser import Parser
from classifier import Classifier

if __name__ == "__main__":
    # create thread synchronization mechanisms
    queue = Queue.Queue()
    event = threading.Event()

    # create output folders
    classifier_path = os.path.join(kRootPath, kGroupFolder)
    if not os.path.exists(classifier_path):
        os.makedirs(classifier_path)
    else:
        for f in os.listdir(classifier_path):
            os.unlink(os.path.join(classifier_path, f))

    sorted_path = os.path.join(kRootPath, kSortedFolder)
    if not os.path.exists(sorted_path):
        os.makedirs(sorted_path)
    else:
        for f in os.listdir(sorted_path):
            os.unlink(os.path.join(sorted_path, f))

    # create parsers
    parsers = []
    for server in servers:
        filename = os.path.join(kRootPath, server, kLogFilename)
        parsers.append(Parser(filename, queue))

    # create classifier
    classifier = Classifier(classifier_path, queue, event)

    # start parsers and classifier
    for parser in parsers:
        parser.start()
    classifier.start()

    # wait all parsers
    for parser in parsers:
        parser.join()

    # notify classifier and wait
    event.set()
    classifier.join()

    # sort users file
    users = classifier.users()
    for userkey in users.keys():
        input_file = users[userkey]
        output_file = os.path.join(sorted_path, userkey + '.log')
        sort_args = ['sort', '-t', ' ',\
                     '-k', '4.9,4.12n',\
                     '-k', '4.5,4.7M',\
                     '-k', '4.2,4.3n',\
                     '-k', '4.14,4.15n',\
                     '-k', '4.17,4.18n',\
                     '-k', '4.20,4.21n',\
                     input_file]

        # call unix sort
        with open(output_file, 'w') as output:
            proc = subprocess.Popen(sort_args, stdout=output, stderr=subprocess.PIPE)
            (stdout, stderr) = proc.communicate()
            if proc.returncode != 0:
                print 'Sort error on file ' + input_file
                print 'Error: ' + stderr
                exit(1)

    print 'User classification finalized'