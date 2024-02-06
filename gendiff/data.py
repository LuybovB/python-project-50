NESTED = 'nested'
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
UNCHANGED = 'unchanged'


def build_diff_data(data1, data2):
    keys1, keys2 = set(data1.keys()), set(data2.keys())
    removed_keys = keys1 - keys2
    added_keys = keys2 - keys1
    common_keys = keys1 & keys2

    diff = {}

    for key in common_keys:
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {'type': NESTED, 'value': build_diff_data(data1[key], data2[key])}
        elif data1[key] == data2[key]:
            diff[key] = {'type': UNCHANGED, 'value': data2[key]}
        else:
            diff[key] = {'type': CHANGED, 'value': {'old value': data1[key], 'new value': data2[key]}}

    for key in added_keys:
        diff[key] = {'type': ADDED, 'value': data2[key]}

    for key in removed_keys:
        diff[key] = {'type': REMOVED, 'value': data1[key]}

    return diff
