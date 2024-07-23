from minio import Minio


class Image:

    def __init__(self, endpoint, access_key, secret_key):
        self.client = Minio(endpoint, access_key, secret_key, secure=False)
        if not self.client.list_buckets():
            self.client.make_bucket('bucket')

    def set_image(self, id: int):
        result = self.client.fput_object('bucket', f'image_{id}', 'my_file.txt')
        return result.version_id

    def get_image(self, id: int):
        image = self.client.get_object("bucket", f"image_{id}").info().get('Content-Length')
        return image

    def delete_image(self, id: int):
        self.client.remove_object('bucket', f'image_{id}')
        return id


obj_img = Image('localhost:9000', 'key', 'secreasdasdasdat')



