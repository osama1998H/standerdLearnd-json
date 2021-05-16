import json
a = {
    'name': 'isama',
    'age': 92,
    'company': 'ires'
}

print(a, type(a))
data = json.dumps(a)
print(data, type(data))
