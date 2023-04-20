class DataReceiver:
    def __init__(self):
        self.stored_bytes: bytearray = bytearray()
        self.text = "aaa"

    def receive(self, signed_bytes: bytes):
        body = signed_bytes[:-4]
        sign = signed_bytes[-4:]

        self.stored_bytes.append(body)
        return sign
