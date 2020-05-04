import books


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    # ours
    elif isinstance(pattern[0], list):
        if len(pattern) > 1:
            return match(seq, pattern[0]) and match(seq, pattern[1:])
        else:
            return match(seq, pattern[0])
    elif pattern[0] == '--':
        if match(seq, pattern[1]):
            return True
        elif not seq:
            return False
        # ours
        elif isinstance(pattern[1], list):
            return match(seq[1:], pattern)
        else:
            return False
    elif not seq:
        return False
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    # ours
    elif not isinstance(seq[0], int):
        for type in seq:
            if type[0] == pattern[0]:
                if isinstance(pattern[1], list):
                    return match(type[1], pattern[1])
                else:
                    return match(type[1:], pattern[1:])
    else:
        return False


def search(pattern, db):
    """
    Matches pattern with each item in the database and returns them in a list
    Parameters: list for one pattern or list in a list for several patterns
    """
    return [book for book in db if match(book, pattern)]
