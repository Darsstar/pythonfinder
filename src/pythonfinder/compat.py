from __future__ import annotations


def getpreferredencoding():
    import locale

    # Borrowed from Invoke
    # (see https://github.com/pyinvoke/invoke/blob/93af29d/invoke/runners.py#L881)
    _encoding = locale.getpreferredencoding(False)
    return _encoding


DEFAULT_ENCODING = getpreferredencoding()


def fs_str(string):
    """Encodes a string into the proper filesystem encoding"""

    if isinstance(string, str):
        return string
    assert not isinstance(string, bytes)
    return string.encode(DEFAULT_ENCODING)
