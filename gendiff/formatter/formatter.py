from gendiff.formatter.json import format_json
from gendiff.formatter.stylish import format_stylish
from gendiff.formatter.plain import format_plain
from gendiff.formatter.formats import JSON, STYLISH, PLAIN


def format_diff(diff: dict, formatter: str) -> str:
    if formatter == STYLISH:
        return format_stylish(diff)
    if formatter == JSON:
        return format_json(diff)
    if formatter == PLAIN:
        return format_plain(diff)
    raise ValueError(f"Unsupported formatter: {formatter}")
