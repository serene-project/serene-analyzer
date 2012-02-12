#!/usr/bin/env python

'''
Scheduler Daemon 

@version: 0.1
@author: Olivier Morel
@contact: omorel@serene-project.net
'''
 
import time
from daemon import Daemon
 
class SchedulerDaemon(Daemon):
    def run(self):
        while True:
            
            # wait one minute before next check
            time.sleep(60)
        