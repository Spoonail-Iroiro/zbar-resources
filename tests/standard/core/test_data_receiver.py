from qrsend.core.data_receiver import DataReceiver
import zlib

# テスト用データのチェックサム計算
# def test_get_checksum():
#     data_ = b"AABB998933302911"
#     sum_ = zlib.adler32(data_).to_bytes(length=4, byteorder="big")
#     print(sum_)
#     pass

def test_receive():
    receiver = DataReceiver()

    s1 = receiver.receive(b"XXYYBB8900\x10\xba\x02\xb8")
    assert s1 == b"\x10\xba\x02\xb8"

    s2 = receiver.receive(b"AABB998933302911\x1fZ\x03\x80")
    assert s2 == b"\x1fZ\x03\x80"

    result = receiver.get_stored()

    assert result == bytearray(b"XXYYBB8900AABB998933302911")
