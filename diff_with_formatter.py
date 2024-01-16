import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = {}
    keys_union = set(data1.keys()) | set(data2.keys())

    for key in sorted(keys_union):
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff[key] = data1[key]
        else:
            if key in data1 and key not in data2:
                diff[f'- {key}'] = data1[key]
            elif key in data2 and key not in data1:
                diff[f'+ {key}'] = data2[key]
            else:
                diff[f'- {key}'] = data1[key]
                diff[f'+ {key}'] = data2[key]

    return json.dumps(diff, indent=2)



file_path1 = "/home/ubunt/PycharmProjects/pythonProject/python-project-50/filepath1.json"
file_path2 = "/home/ubunt/PycharmProjects/pythonProject/python-project-50/filepath2.json"
result = generate_diff(file_path1, file_path2)
print(result)
