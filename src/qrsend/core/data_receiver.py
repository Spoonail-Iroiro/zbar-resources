class DataReceiver:
    def __init__(self):
        self.stored_bytes: bytearray = bytearray()
        self.text = "aaa"

    def receive(self, signed_bytes: bytes):
        body = signed_bytes[:-6]
        sign = signed_bytes[-6:]

        self.stored_bytes.extend(body)
        return sign

    def get_stored(self):
        return self.stored_bytes
