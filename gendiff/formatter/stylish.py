import json
from gendiff.data import NESTED, ADDED, REMOVED, CHANGED, UNCHANGED


FLAGS = {
    ADDED: '  + ',
    REMOVED: '  - ',
    UNCHANGED: '    '
}


def get_stringify_value(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def stringify_value(value, depth):
    if not isinstance(value, dict):
        return get_stringify_value(value)
    lines = []
    spaces = "  " * depth
    for key, inner_value in value.items():
        if isinstance(inner_value, dict):
            line = f"{spaces}  {key}: {stringify_value(inner_value, depth + 1)}"
        else:
            line = f"{spaces}  {key}: {stringify_value(inner_value, depth)}"
        lines.append(line)
    result = "{" + "\n".join(lines) + "\n" + spaces + "}"
    return result


def stringify_diff(diff, depth, indent="  "):
    diff_list = []
    spaces = indent * depth
    prefix = indent * (depth + 1)
    for key, flags in diff.items():
        type_ = flags.get('type')
        value = flags.get('value')

        if type_ == NESTED:
            result_key = f"{spaces}  {key}:"
            result_value = (
                f"{prefix}{{\n{stringify_diff(value, depth + 1,indent)}"
                f"\n{spaces}{indent}}}"
            )
            diff_list.append(f"{result_key}\n{result_value}")
        elif type_ == CHANGED:
            old_value = value.get('old value')
            new_value = value.get('new value')
            result_key = (f"{spaces}- {key}:"
                          f" {stringify_value(old_value, depth + 1)}")
            diff_list.append(result_key)
            result_key = (f"{spaces}+ {key}:"
                          f" {stringify_value(new_value, depth + 1)}")
            diff_list.append(result_key)
        else:
            result_string = (f"{spaces}{FLAGS.get(type_, '')}"
                             f" {key}: {stringify_value(value, depth + 1)}")
            diff_list.append(result_string)

    result = "\n".join(diff_list)
    return result


def format_stylish(diff, depth=0):
    final_list = ['{', stringify_diff(diff, depth), '}']
    return '\n'.join(final_list)
