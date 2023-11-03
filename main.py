from utils.logger import Log
from data.data_source.indodax_data_source import IndodaxDataSource

class App():
    def __init__(self) -> None:
        self.indodaxDataSource: IndodaxDataSource = IndodaxDataSource()
        self.running()

    def running(self) -> None:
        self.indodaxDataSource.getTickerPairId('adaidr')



if __name__ == '__main__':
    App()