#!/bin/bash
curl -XPOST localhost:9200/_aliases -d '
{
    "actions": [
        { "add": {
            "alias": "v2",
            "index": "st"
        }}
    ]
}
'
