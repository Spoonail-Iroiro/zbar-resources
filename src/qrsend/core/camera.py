import cv2
import numpy as np
from PIL import ImageGrab, Image

class MockCapture():
    def __init__(self, side: str):
        """
        Args:
            side: 'left' or 'right'
        """

        self.side = side

    def _get_pil_image(self):
        grabbed = ImageGrab.grab()
        if self.side == "left":
            bbox = (0, 0, grabbed.width // 2, grabbed.height)
        elif self.side == "right":
            bbox = (grabbed.width // 2, 0, grabbed.width, grabbed.height)
        else:
            raise ValueError(self.side)

        cropped = grabbed.crop(bbox)

        return cropped

    def _pil_image_to_cv_mat(self, image):
        cv_mat = np.array(image, dtype=np.uint8)
        if cv_mat.ndim == 2:
            pass
        elif cv_mat.shape[2] == 3:
            cv_mat = cv2.cvtColor(cv_mat, cv2.COLOR_RGB2BGR)
        elif cv_mat.shape[2] == 4:
            cv_mat = cv2.cvtColor(cv_mat, cv2.COLOR_RGBA2BGRA)
        else:
            raise ValueError(cv_mat.shape)

        return cv_mat

    def read(self):
        image = self._get_pil_image()
        cv_mat = self._pil_image_to_cv_mat(image)

        return True, cv_mat

    def isOpened(self):
        return True


_camera = None
def load_mock_camera(side):
    global _camera
    _camera = MockCapture(side)


def get_camera():
    global _camera
    if _camera is None:
        _camera = cv2.VideoCapture(0)
        if not _camera.isOpened():
            raise ValueError(f"Camera open failed")

    return _camera