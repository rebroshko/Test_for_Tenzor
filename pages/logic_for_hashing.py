import hashlib


class LogicForHashing:
    HASH_CONTAINER = []

    def transform_img_in_hash(self, file_name):
        with open(file_name, 'rb') as file:
            hasher = hashlib.md5()
            hasher.update(file.read())
            self.HASH_CONTAINER.append(hasher.hexdigest())
