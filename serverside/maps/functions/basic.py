import re
import json

class Basic:
    def dict_to_json(input_dict):
        return (json.dumps(input_dict))
    def json_to_dict(input_json):
        return (json.loads(input_json))
    
input = "<22|33 | fuck>"
output = re.split(r"<|>|/",input)
for x in output:
    print(type(x))
    print(x)