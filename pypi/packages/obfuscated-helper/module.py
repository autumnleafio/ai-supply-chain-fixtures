import base64

_ENCODED_MESSAGE = "ZGlhZ25vc3RpYy1tYXJrZXI6cHlwaS1vYmZ1c2NhdGlvbi1wYXR0ZXJu"


def describe():
    return base64.b64decode(_ENCODED_MESSAGE).decode("utf-8")
