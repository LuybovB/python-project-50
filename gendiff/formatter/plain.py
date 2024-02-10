import json
from gendiff.data import NESTED, ADDED, REMOVED, CHANGED


DIFF_MESSAGES = {
    ADDED: "Property '{path}' was added with value: {value}",
    REMOVED: "Property '{path}' was removed",
    CHANGED: "Property '{path}' was updated. From {old_value} to {new_value}"
}


def stringify_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    else:
        return str(value)


def get_path(previous_path: str, key: str) -> str:
    if previous_path:
        return f"{previous_path}.{key}"
    return key


def get_message_string(diff, previous_path):
    messages = []
    for key, types in diff.items():
        path = get_path(previous_path, key)
        type_ = types.get('type')
        value = types.get('value')
        if type_ == NESTED:
            messages.append(get_message_string(value, path))
        elif type_ == CHANGED:
            old_value = stringify_value(value.get('old value'))
            new_value = stringify_value(value.get('new value'))
            message = DIFF_MESSAGES[CHANGED].format(path=path,
                                                    old_value=old_value,
                                                    new_value=new_value)
            messages.append(message)
        elif type_ == ADDED:
            value = stringify_value(value)
            message = DIFF_MESSAGES[ADDED].format(path=path, value=value)
            messages.append(message)
        elif type_ == REMOVED:
            message = DIFF_MESSAGES[REMOVED].format(path=path)
            messages.append(message)
    return '\n'.join(messages)


def format_plain(diff):
    return get_message_string(diff, previous_path='')
