import requests


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, tok: str):
        self.token = tok

    def upload(self, file_path: str):
        url = f'{self.host}/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': True}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        request_href = (requests.get(url, params=params, headers=headers)).json().get('href')
        requests.put(request_href, data=open(file_path, 'rb'), headers=headers)


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
