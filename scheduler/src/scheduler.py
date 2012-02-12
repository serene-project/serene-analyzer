#!/usr/bin/env python

'''
Serene scheduler

@version: 0.1
@author: Olivier Morel
@contact: omorel@serene-project.net
'''

import sys
from scheduler.scheduler_daemon import SchedulerDaemon 


if __name__ == "__main__":
    daemon = SchedulerDaemon('/tmp/serene-scheduler-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
        sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)