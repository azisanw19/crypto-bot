import requests

from utils.json import jsonFormat

class ApiService:

    def __init__(self, endPoint: str, header: dict) -> None:
        self.endPoint = endPoint
        self.header = header

    def get(self, path: str, header: dict = {}) -> dict:
        headers: dict = self.header
        headers.update(header)

        uri = f'{self.endPoint}/{path}'
        response = requests.get(uri, headers=headers)

        responseString: str = jsonFormat(response.json())
        headerString: str = jsonFormat(headers)
        print(f'{uri}\n{headerString}\n\n{responseString}')

        return response