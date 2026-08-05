from typing import Any, Dict

def flatten_dict(d: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    result = {}

    def recurse(subdict: Dict[str, Any], parent_key: str = ""):
        for key, value in subdict.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key
            if isinstance(value, dict):
                recurse(value, new_key)
            else:
                result[new_key] = value

    recurse(d)
    return result

d1 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": 4
        }
    }
}
print(flatten_dict(d1, "."))
