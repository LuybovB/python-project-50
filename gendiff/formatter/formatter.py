from .json import format_json
from .stylish import format_stylish
from .plain import format_plain
from .formats import JSON, STYLISH, PLAIN


def format_diff(diff, formatter):
    if formatter == STYLISH:
        return format_stylish(diff)
    if formatter == JSON:
        return format_json(diff)
    if formatter == PLAIN:
        return format_plain(diff)
