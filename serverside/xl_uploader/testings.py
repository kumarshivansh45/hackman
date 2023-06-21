import json
from textwrap import indent


data = {"name": "hello",
        "age": 23,
        "secrets": {
            "had_sex": "yes",
            "used_protection": "no",
            "did_she_got_pregnant": "hope not",
        }}

print(data["secrets"]["had_sex"])  # it is a dictionary
print(type(data))  # it is a dictionary
data = json.dumps(data, indent=4)
print(data)
print(type(data))  # data to string or json
print(data)
new_data = '{"name": "hello","age": 23,"secrets": {"had_sex": "yes","used_protection": "no","did_she_got_pregnant": "hope not"}}'
new_data = json.loads(new_data)
print(new_data)
print(type(new_data))  # string/json to dictionary
