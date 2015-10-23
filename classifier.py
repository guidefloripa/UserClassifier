#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Guilherme Steinmann

import os
import threading
from Queue import Empty

class Classifier(threading.Thread):
    def __init__(self, path, queue, event):
        self.path = path
        self.queue = queue
        self.event = event
        self.usersdict = {}
        threading.Thread.__init__(self)

    def users(self):
        return self.usersdict

    def run(self):
        while True:
            try:
                # get line from processing queue waiting 1 second
                result = self.queue.get(timeout=1)
                if result:
                    filename = os.path.join(self.path, result['id'] + '.log')
                    self.usersdict[result['id']] = filename
                    with open(filename, 'a') as f:
                        print >>f, result['line']

            # if processing queue has no lines
            except Empty:
                # check if parsers finished
                if self.event.is_set():
                    break
