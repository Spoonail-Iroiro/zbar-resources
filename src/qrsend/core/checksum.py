import zlib

def get_checksum(data: bytes) -> bytes:
    sum = zlib.adler32(data)
    sum_bytes = sum.to_bytes(length=4, byteorder="big")

    return sum_bytes
