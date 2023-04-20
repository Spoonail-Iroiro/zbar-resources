from qrsend.core.data_sender import DataSender
from qrsend.core.data_receiver import DataReceiver

def test_send():
    data = b"012345678901234589aaaaabbbbb"
    sender = DataSender(data, 7)

    receiver = DataReceiver()

    while True:
        data_send = sender.send()
        sign = receiver.receive(data_send)
        if not sender.confirm(sign):
            raise ValueError()

        is_updated = sender.update()
        if not is_updated:
            break

    assert receiver.get_stored() == data

