from qrsend.core.data_receiver import DataReceiver

def test_receive():
    receiver = DataReceiver()

    s1 = receiver.receive(b"XXYYBB8900ABCDE")
    assert s1 == b"ABCDE"

    s2 = receiver.receive(b"AABB99893330291198765")
    assert s2 == b"98765"

    result = receiver.get_stored()

    assert result == b"XXYYBB8900AABB998933302911"
