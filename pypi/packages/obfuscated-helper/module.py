import base64

_ENCODED_MESSAGE = "ZW5jb2RlZCBjb25maWd1cmF0aW9uIGhlbHBlcg=="


def describe():
    return base64.b64decode(_ENCODED_MESSAGE).decode("utf-8")
