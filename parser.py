#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Guilherme Steinmann

import re
import threading

regex = '[(\d\.)]+ - - \[(.*?)\] ".*?" \d+ \d+ ".*?" "userid=(.*?)"'

class Parser(threading.Thread):
    def __init__(self, filename, queue):
        self.filename = filename
        self.queue = queue
        threading.Thread.__init__(self)

    def run(self):
        with open(self.filename, 'r') as f:
            for line in f:
                matches = re.match(regex, line)

                # put line in the processing queue
                if matches:
                    date = matches.groups()[0]
                    id = matches.groups()[1]
                    self.queue.put({'id': id, 'date': date, 'line': line.strip()})
