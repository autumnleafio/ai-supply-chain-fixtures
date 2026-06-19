import base64

_ENCODED_MESSAGE = "c2FmZSByZXNlYXJjaCBmaXh0dXJlOiBweXBpIG9iZnVzY2F0aW9uLWxpa2UgcGF0dGVybiBvbmx5"


def describe():
    return base64.b64decode(_ENCODED_MESSAGE).decode("utf-8")
