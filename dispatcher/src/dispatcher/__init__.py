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
        from mongodb_connector import mongodb
        import time
        
        #select the plugins collection 
        collection = mongodb.plugins
        
        inputs = web.input()
        plugin = { 
            'type' : inputs.type,
            'hostname' : inputs.hostname,
            'enabled' : True, 
            'enabled_since' : time.time()
        }
        
        #todo: validate inputs
        elem = collection.find_one({'type': plugin['type'], 'hostname' : plugin['hostname']})
        
        if elem == None: 
            collection.insert(plugin)
        elif elem['enabled'] == False:
            elem['enabled'] = True
            elem['enabled_since'] = time.time()
            _id = collection.insert(elem)
         
        return {'status' : 'OK', 'message' : 'Subscription enabled'}
    
    def GET(self):
        return 'NOK'

class subscriptions: 
    def GET(self):
        return 'NOK'    