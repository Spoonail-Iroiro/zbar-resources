from zbar_helper.utils import decode,show_info
import zbar
from pathlib import Path
import cv2

def test_environ():
    import os
    from pprint import pprint
    envs = os.environ['PATH']
    envs = envs.split(";")
    pprint(f"{envs}")

def test_zbar_lite():
    image_path = Path(r"C:\Users\spoon\VirtualBox VMs\Ubuntu22.04-V1_share\qr2.png")
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("",image)

    cv2.waitKey()

    print(image.shape)

    print(decode(image))

    pass

def test_zbar_lite_prim():
    image_path = Path(r"C:\Users\spoon\VirtualBox VMs\Ubuntu22.04-V1_share\qr2_with_bin.png")
    # create a reader
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('qrcode.enable=1')
    scanner.parse_config('qrcode.binary=1')

    # obtain image data
    pil = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    height, width = pil.shape[:2]
    raw = pil.tobytes()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    # extract results
    for symbol in image:
        # do something useful with results
        print(symbol.data)
        print('decoded', symbol.type, 'text', '"%s"' % symbol.data)
        print(
            'type {} text {} location {} quality {}'.format(symbol.type, symbol.data, symbol.location, symbol.quality))

    # clean up
    del (image)