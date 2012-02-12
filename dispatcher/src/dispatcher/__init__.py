'''


@version: 0.1
@author: Olivier Morel
@contact: omorel@serene-project.net
'''
import json
import web


class index: 
    def GET(self):
        return json.dumps({'message' : 'welcome to dispatcher'})
    
class version:        
    def GET(self):
        return json.dumps({'name' : '', 
                           'version' : '0.1'}) 

class data: 
    def POST(self):
        i = web.input()
        return json.dumps(i.message)
    
    def GET(self):
        return 'NOK'
        
class subscription: 
    def POST(self):
        return 'NOK'
    
    def GET(self, uuid):
        return 'NOK'

class subscriptions: 
    def GET(self):
        return 'NOK'    