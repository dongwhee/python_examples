import json

data = '''
{
    "fruit": [
        {
            "name": "banana",
            "color": "yellow"
        },
        {
            "name": "apple",
            "color": "red"
        }
    ]
}
'''

obj = json.loads(data) # json string -> dictionary
print obj
print type(obj) # check type of result

obj['fruit'][0]['color'] = 'brown' # change value

gen = json.dumps(obj) # dictionary -> json string
print gen
print type(gen) # check type of result
