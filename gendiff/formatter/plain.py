
import json
from gendiff.data import NESTED, ADDED, REMOVED, CHANGED


DIFF_MESSAGES = {
    ADDED: "Property '{path}' was added with value: {value}",
    REMOVED: "Property '{path}' was removed",
    CHANGED: "Property '{path}' was updated. From {old_value} to {new_value}"
}


def stringify_value(value):
    if value is None or isinstance(value, (bool, int, float)):
        return json.dumps(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, dict):
        return '[complex value]'
    else:
        return value


def get_path_string(previous_path, key):
    return f"{previous_path}.{key}" if previous_path else key


def get_message_string(diff, previous_path):
    messages = []
    for key, value_types in diff.items():
        current_path = get_path_string(previous_path, key)
        type_ = value_types.get('type')
        value = value_types.get('value')

        if type_ == NESTED:
            nested_messages = get_message_string(value, current_path)
            messages.extend(nested_messages)

        elif type_ == CHANGED:
            old_value = stringify_value(value.get('oldvalue'))
            new_value = stringify_value(value.get('newvalue'))
            message = DIFF_MESSAGES[type_].format(path=current_path,
                                                  old_value=old_value,
                                                  new_value=new_value)
            messages.append(message)

        elif type_ == ADDED:
            added_value = stringify_value(value)
            message = DIFF_MESSAGES[type_].format(path=current_path,
                                                  value=added_value)
            messages.append(message)

        elif type_ == REMOVED:
            message = DIFF_MESSAGES[type_].format(path=current_path)
            messages.append(message)

    return messages


def format_plain(diff):
    return "\n".join(get_message_string(diff, previous_path=''))
