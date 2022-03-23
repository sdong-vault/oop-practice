
def validate_str(s: str):
    if s is not None and len(s) > 0:
        return s
    else:
        raise ValueError()
