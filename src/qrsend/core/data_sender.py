import random
from typing import List, Tuple, Optional


class DataSender:
    def __init__(self, data_send: bytes, max_bytes_n: int):
        self.data_send = data_send
        self.current_index = -1
        self.current_sign: Optional[bytes] = None
        self.current_data: Optional[bytes] = None

        self.data_chunks = []
        for i in range(0, len(self.data_send), max_bytes_n):
            data_chunk = data_send[i:i+max_bytes_n]
            self.data_chunks.append(data_chunk)

        self.update()

    def update(self):
        if self.current_index < (len(self.data_chunks)-1):
            self.current_index += 1
            self.current_data = self.data_chunks[self.current_index]
            self.current_sign = random.randbytes(5)
            return True
        else:
            return False

    def send(self):
        return self.current_data + self.current_sign

    def confirm(self, sign_read):
        return self.current_sign == sign_read
