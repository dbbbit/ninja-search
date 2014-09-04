#coding:utf8

from flask import Flask, request, render_template
from search import Search
from util import gen_pages, pretty_date
from time import time
import json

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET'])
@app.route("/api", methods=['GET'])
def index():

    #: request args
    _from = int(request.args.get('from', 0))
    limit = int(request.args.get('limit', 10))
    q = unicode(request.args.get('q', ''))
    s = request.args.get('s','sumup')
    raw = bool(request.args.get('raw', ''))

    if len(q) == 0 and request.path == '/':
        return render_template("index.html")

    #: build search
    search = Search(index='v2', doc_type='topic')
    search.params['body']['query'] = \
        { 
            "multi_match" : 
                    { 
                        "query":"%s"%q ,
                        "fields":["title","content", "rcontent"]
                    }
        }
    search['size'] = limit
    search['from_'] = _from
    
    #: choose a sort method
    search['sort'] = '_score'

    if s in ["replies", "created"]:
        search['sort'] = "%s:desc"%s

    if s == 'sumup':
        search.params['body']['sort'] = {
            "_script" : {
                "script" : "(doc['created'].value-1272124800000) * log10(doc['replies'].value+1)* log10(doc.score)",
                "type" : "number",
                "params" : {
                    "factor" : 0
                },
                "order" : "desc"
            }
        }
    
    #: run search engine
    time0 = time()
    result = search.exe()
    time1 = time()
    
    #: [return] raw json 
    if raw:
        return json.dumps(result, indent=True)

    #: [return] api request 
    if request.path == '/api':
        return json.dumps(result, indent=True)
    
    #: data for template
    total = result['hits']['total'] 
    current = _from / 10
    max_page = total / 10
    pages = gen_pages(current, max_page)

    sort_by = {
                "sumup" : u"综合",
                "match" : u"精确匹配",
                "created" : u"创建时间",
                "replies" : u"回复数"
    }

    return render_template('result.html', res=result, pages=pages, \
        current=current, q=q, s=s, cost=time1-time0, pretty_date=pretty_date, \
        enumerate=enumerate, int=int, sort_by = sort_by, route="")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
