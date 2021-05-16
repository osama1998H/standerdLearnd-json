import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}


d = json.dumps(j_str, indent=3, sort_keys=True)
print(d)
