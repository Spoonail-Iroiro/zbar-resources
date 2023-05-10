import cv2

_camera = None
def get_camera():
    global _camera
    if _camera is None:
        _camera = cv2.VideoCapture(0)
        if not _camera.isOpened():
            raise ValueError(f"Camera open failed")

    return _camera