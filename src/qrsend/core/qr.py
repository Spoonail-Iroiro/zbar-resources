import zbar

def decode_first_qr(grayed_cv_mat):
    symbols = decode_qr(grayed_cv_mat)
    return symbols[0].data if symbols else None

def decode_qr(grayed_cv_mat):
    scanner = zbar.ImageScanner()

    # configure the reader
    scanner.parse_config('qrcode.enable=1')
    scanner.parse_config('qrcode.binary=1')

    height, width = grayed_cv_mat.shape[:2]
    raw = grayed_cv_mat.tobytes()

    # wrap image data
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    return [symbol for symbol in image]

    # extract results
    # for symbol in image:
    #     # do something useful with results
    #     print(symbol.data)
    #     print('decoded', symbol.type, 'text', '"%s"' % symbol.data)
    #     print(
    #         'type {} text {} location {} quality {}'.format(symbol.type, symbol.data, symbol.location, symbol.quality))
