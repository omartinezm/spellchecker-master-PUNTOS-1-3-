# -*- coding: utf-8 -*-
import json
from spell_checker import spell_check_sentence

def spell_check(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    #print(event)
    text=json.dumps(body)
    ubi=text.find('text')
    original=text[ubi+8:]
    original=original[:original.find("'")]
    print(spell_check_sentence(original).encode('utf-8'))
    response = {
        "statusCode": 200,
        "body": u'{"text" : "'+spell_check_sentence(original)+'" }'
    }
    return response