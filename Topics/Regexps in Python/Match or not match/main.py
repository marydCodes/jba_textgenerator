import re


def matched(template, string):
    if re.match(template, string) is None:
        return False
    else:
        return True