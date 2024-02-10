NESTED = 'nested'
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
UNCHANGED = 'unchanged'


def data(data1, data2):
    diff = {}
    keys1, keys2 = set(data1.keys()), set(data2.keys())
    combained_keys = sorted(keys1 | keys2)
    for key in combained_keys:
        if key not in data1 and key in data2:
            diff[key] = {
                'type': ADDED,
                'value': data2[key]
            }
        elif key in data1 and key not in data2:
            diff[key] = {
                'type': REMOVED,
                'value': data1[key]
            }
        elif data1[key] == data2[key]:
            diff[key] = {
                'type': UNCHANGED,
                'value': data2[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = {
                'type': NESTED,
                'value': data(data1[key], data2[key])
            }
        else:
            diff[key] = {
                'type': CHANGED,
                'value': {
                    'old value': data1[key],
                    'new value': data2[key]
                }
            }
    return diff
