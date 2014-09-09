from elasticsearch import Elasticsearch
import json

class Search:

    """ 
        API Doc for Python Elasticsearch Client
        http://elasticsearch-py.readthedocs.org/en/master/ 
        
    """
    es = Elasticsearch()
    params = {}    
    
    def __init__(self, **kargs):

        #: highlight some result field
        self.params['body'] = {
            "highlight" : {
                "fields" : {
                    "content" : {},
                    "title" : {},
                    "rcontent" : {},    #: replies
                }
             },
        }
        self.params.update(kargs)
        

    def __setitem__(self, key, item):
        self.params[key] = item

    def __getitem__(self, key):
        if self.params.has_key(key):
            return self.params[key]

    def __delitem__(self, key):
        if self.params.has_key(key):
            del self.params[key]

    def exe(self):
        try:
            result = self.es.search(**self.params)
        except Exception, e:
            raise e
        
        return result

if __name__ == "__main__":

    s = Search(index="v2", doc_type="topic")
    s['size'] = 10
    s['q'] = 'content:hello' 
    s['_source_include'] = ['content', 'title']
    print(s.exe())
