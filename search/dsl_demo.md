// basic query
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
    "query" : {
        "term" : { "title" : "go" }
    }
}
'

// from & size
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
    "query" : {
        "term" : { "title" : "go" }
    },
    "from":0,
    "size":1
}
'
// sort
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
    "query" : {
        "term" : { "title" : "go" }
    },
    "from":0,
    "size":2,
    "sort":[
      {"replies":"desc"},
      "_score"
    ]
}
'

// sort base on script
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
    "query" : {
        "term" : { "title" : "go" }
    },
    "from":0,
    "size":2,
    "sort" : {
        "_script" : {
            "script" : "_source.replies * factor",
            "type" : "number",
            "params" : {
                "factor" : 0.5
            },
            "order" : "desc"
        }
    }
}
'

// script and score
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
    "query" : {
        "term" : { "title" : "go" }
    },
    "from":0,
    "size":10,
    "sort" : {
        "_script" : {
            "script" : "doc.score * factor",
            "type" : "number",
            "params" : {
                "factor" : 1
            },
            "order" : "desc"
        }
    }
}
'

//multi-match query
curl -XGET 'http://localhost:9200/v2/topic/_search?pretty' -d '{
   "query": {
    "filtered": {
      "query": {
        "bool": {
          "should": [
            {
              "query_string": {
                "query": "content:go or title:go"
              }
            }
          ]
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "match_all": {}
            }
          ]
        }
      }
    }
  },
  "from":0,
  "size":10,
  "sort" : {
        "_script" : {
            "script" : "doc.score * _source.replies",
            "type" : "number",
            "params" : {
                "factor" : 1
            },
            "order" : "desc"
        }
    }
}
'




