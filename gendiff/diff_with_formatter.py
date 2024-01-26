from gendiff.parser import load_data_from_file


def generate_diff(file_path1, file_path2):
    data1 = load_data_from_file(file_path1)
    data2 = load_data_from_file(file_path2)
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
