#!/bin/bash
curl -XPUT "http://localhost:9200/ik"
curl -XPUT "http://localhost:9200/ik/topic/_mapping" -d '
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
					"type": "string",
					"term_vector": "with_positions_offsets",
                	"indexAnalyzer": "ik",
                	"searchAnalyzer": "ik",
                	"include_in_all": "true"
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
							"type": "string", 
							"index":"no"
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
                    "type": "string",
                    "term_vector": "with_positions_offsets",
                	"indexAnalyzer": "ik",
                	"searchAnalyzer": "ik",
                	"include_in_all": "true",
                	"boost":0.7
                },
			    "title": {
					"type": "string",
					"term_vector": "with_positions_offsets",
                	"indexAnalyzer": "ik",
                	"searchAnalyzer": "ik",
                	"include_in_all": "true",
                	"boost":1.5
				},
			    "url": {
					"type": "string", "index":"no"
				}
			}
		}
	
}
'


