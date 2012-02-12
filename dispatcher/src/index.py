'''


@version: 0.1
@author: Olivier Morel
@contact: omorel@serene-project.net
'''

import web

from dispatcher import index
from dispatcher import version
from dispatcher import data
from dispatcher import subscription
from dispatcher import subscriptions

urls = (
    '/', 'index',
    '/version', 'version', 
    '/input', 'input', 
    '/inputs', 'inputs', 
    '/subscription', 'subscription', 
    '/subscriptions', 'subscriptions'     
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

