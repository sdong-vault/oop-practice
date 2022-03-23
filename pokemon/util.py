
def validate_str(s: str):
    if s is not None and len(s) > 0:
        return s
    else:
        raise ValueError()

def validate_or_default_list(l: list, default: list = []):
    if l is None or len(l) == 0:
        return default
    return l
