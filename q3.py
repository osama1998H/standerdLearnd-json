import json
a = {
    'name': 'isama',
    'age': 92,
    'company': 'ires'
}
d = ['a', 'f' , 'n', True]
data = json.dumps(d)
x = json.loads(data)
print(x, type(x))
# for i, j in x.items():
#     print(i, j)
