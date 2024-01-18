import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = []
    keys_union = set(data1.keys()) | set(data2.keys())

    for key in sorted(keys_union):
        if key in data1 and key in data2 and data1[key] == data2[key]:
            diff.append(f'   {key}: {data1[key]}')
        else:
            if key in data1 and key not in data2:
                diff.append(f'- {key}: {data1[key]}')
            elif key in data2 and key not in data1:
                diff.append(f'+ {key}: {data2[key]}')
            else:
                diff.append(f'- {key}: {data1[key]}')
                diff.append(f'+ {key}: {data2[key]}')

    result = '{\n' + '\n'.join(diff) + '\n}'
    result = result.replace('\n+', '\n+ ').replace('\n-', '\n- ')

    return result

