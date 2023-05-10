from .checksum import get_checksum
from typing import Optional

class ChecksumError(Exception):
    def __init__(self, actual, expected):
        super().__init__(f"Checksum error. actual: {actual}, expected: {expected}")

class SameChecksum(Exception):
    pass


class DataReceiver:
    def __init__(self, allow_same_sum=False):
        self.allow_same_sum = allow_same_sum
        self.stored_bytes: bytearray = bytearray()
        self.previous_sum: Optional[bytes] = None

    def receive(self, signed_bytes: bytes):
        body = signed_bytes[:-4]
        sign = signed_bytes[-4:]

        sum_ = get_checksum(body)

        if sum_ != sign:
            raise ChecksumError(sum_, sign)

        if not self.allow_same_sum and sign == self.previous_sum:
            raise SameChecksum()

        self.stored_bytes.extend(body)
        self.previous_sum = sign
        return sign

    def get_stored(self):
        return self.stored_bytes
