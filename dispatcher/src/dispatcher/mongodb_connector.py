'''

@version: 0.1
@author: Olivier Morel
@contact: omorel@serene-project.net
'''

from pymongo import Connection
from dispatcher.settings import config 

connection = Connection(config['mongodb']['hostname'])
mongodb = connection[config['mongodb']['database']]