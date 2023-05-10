import cv2
# from pyzbar.pyzbar import decode, ZBarSymbol
import qrcode
import qrcode.util
from PIL import Image, ImageDraw
import numpy as np
import logging
from qrsend.core.data_sender import DataSender
from qrsend.core.data_receiver import DataReceiver
from ctypes import string_at
logger = logging.getLogger(__name__)

def test_make_qr(tmp_path):
    data = b"012345678901234589aaaaabbbbb"
    sender = DataSender(data, 16)

    chunk = sender.send()

    qrdata = qrcode.util.QRData(chunk)

    qr = qrcode.QRCode(
        version=22,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )

    qr.add_data(qrdata)
    logger.info(f"Added data {chunk}")
    qr.make(fit=False)

    img = qr.make_image()
    image = img._img

    image.save(tmp_path / "test_qr.png")
    logger.info(f"Exported to: {tmp_path}")


def test_qr(tmp_path):
    data = b"012345678901234589aaaaabbbbb"
    sender = DataSender(data, 16)

    receiver = DataReceiver()

    chunk = sender.send()
    # chunk = b"01234567890123457\xd0\x0e\x08\x16j"

    qrdata = qrcode.util.QRData(chunk)

    qr = qrcode.QRCode(
        version=22,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )

    qr.add_data(qrdata)
    logger.info(f"Added data {chunk}")
    qr.make(fit=False)

    img = qr.make_image()
    image = img._img
    # image = Image.open("/media/sf_Ubuntu22.04-V1_share/DSC_0294.JPG",formats=["jpeg"])

    # canvas = Image.new("RGB", (800,800), (255,255,255))
    # canvas.paste(image, (100,100))

    results = decode(image, symbols=[ZBarSymbol.QRCODE])
    decoded = results[0]
    # decoded_str = decoded.data.decode(encoding="utf-8")
    # logger.info(f"decoded str:{decoded_str}")
    
    x,y,w,h = decoded.rect
    draw = ImageDraw.Draw(image)
    draw.rectangle((x,y,x+w,y+h), outline=(0,))

    image.save(tmp_path / "qr.png")
    logger.info(f"Exported: {tmp_path}")
    logger.info(decoded)
    assert decoded.data == chunk

def test_qr_network():
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
    pass

def test_sample():
    cap = cv2.VideoCapture(0)
    cap.open()
    if not cap.isOpened():
        raise ValueError()


    print(f"Hello")
    logger.info(f"Hello")
