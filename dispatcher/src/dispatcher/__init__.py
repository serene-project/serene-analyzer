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
        return json.dumps({'name' : 'dispatcher', 
                           'version' : '0.1'}) 

class data:     
    def POST(self):    
        from mongodb_connector import mongodb
        
        # select the data collection 
        collection = mongodb.data
        
        inputs = web.input()
        message = inputs.message
        
        #todo: validate message 
        document = json.loads(message)
        
        _id = collection.insert(document)
        return _id;  
    
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