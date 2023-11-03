from data.data_source.base.api_service import ApiService

class IndodaxDataSource(ApiService):
    def __init__(self) -> None:
        endPoint = 'https://indodax.com'
        headers = {
            'Accept': 'application/json'
        }

        super().__init__(endPoint=endPoint, header=headers)

    def getTickerPairId(self, pairId: str) -> dict:
        response = self.get(f'/api/ticker/{pairId}')
        return response.json()

