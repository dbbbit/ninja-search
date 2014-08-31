#!/bin/bash

curl -XPUT "http://localhost:9200/v2/topic/_mapping" -d '
{
	
		"topic": {

			"_all": {
            	"indexAnalyzer": "ik",
            	"searchAnalyzer": "ik",
            	"term_vector": "no",
            	"store": "false"
        	},
        	
			"properties": {
			    "content": {
					"type": "string"
				},
			    "content_rendered": {
					"type": "string", "index":"no"
				},
			    "created": {
					"type": "long", "store":"yes"
				},
			    "last_modified": {
					"type": "long"
				},
			    "last_touched": {
					"type": "long"
				},
			    "member": {
				    "properties": {
					    "avatar_large": {
							"type": "string", "index":"no"
						},
					    "avatar_mini": {
							"type": "string", "index":"no"
						},
						"avatar_normal": {
							"type": "string", "index":"no"
						},
					    "id": {
							"type": "long"
						},
					    "tagline": {
							"type": "string", "index":"no"
						},
					    "username": {
							"type": "string", "index":"no"
						}
					}
				},
			    "node": {
				    "properties": {
					    "avatar_large": {
							"type": "string", "index":"no"
						},
					    "avatar_mini": {
							"type": "string", "index":"no"
						},
					    "avatar_normal": {
							"type": "string", "index":"no"
						},
					    "id": {
							"type": "long"
						},
					    "name": {
							"type": "string", "index":"no"
						},
					    "title": {
							"type": "string", "index":"no"
						},
					    "topics": {
							"type": "long"
						},
					    "url": {
							"type": "string", "index":"no"
						}
					}
				},
			    "replies": {
					"type": "long", "store":"yes"
				},
                "rcontent": {
                    "type": "string"
                },
			    "title": {
					"type": "string"
				},
			    "url": {
					"type": "string", "index":"no"
				}
			}
		}
	
}
'
