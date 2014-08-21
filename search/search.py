from elasticsearch import Elasticsearch
import json

class Search:

    es = Elasticsearch()
    params = {}    
    DSL = {}
    def __init__(self, **kargs):
        self.DSL = {
            "highlight" : {
                "fields" : {
                    "content" : {},
                    "title" : {}
                }
             },
        }
        self.params.update(kargs)
        self.params['body'] = self.DSL
        self.params['size'] = 10

    def __setitem__(self, key, item):
        self.params[key] = item
    
    def update_params(self, **kargs):
        self.params.update(kargs)

    def toString(self):
        return json.dumps(self.params, indent=True)

    def exe(self):
        try:
            result = self.es.search(**self.params)
        except Exception, e:
            raise e
        
        return result

if __name__ == "__main__":

    s = Search(index="v2ex", doc_type="topic")
    s['size'] = 10
    s['q'] = 'content:hello' 
    s['_source_include'] = ['content', 'title']
    print(s.exe())
