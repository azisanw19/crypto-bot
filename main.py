from time import sleep


from data.data_source.indodax_data_source import IndodaxDataSource
from data.data_source.telegram_data_source import TelegramDataSource
from service.exponential_moving_average import ExponentialMovingAverage
from utils.json import jsonFormat
from config.config import DELAY_API_GET
from utils.logger import Log


class App():
    indodaxDataSource: IndodaxDataSource = IndodaxDataSource()
    telegramDataSource: TelegramDataSource = TelegramDataSource()
    ema10: ExponentialMovingAverage = ExponentialMovingAverage(10)
    ema20: ExponentialMovingAverage = ExponentialMovingAverage(20)
    delayAPI: int = DELAY_API_GET
    lastScoreEma10 = 0.0
    lastScoreEma20 = 0.0

    def __init__(self) -> None:
        loopke = 0
        while True:
            loopke += 1
            Log.d('Loop', f'loop ke {loopke}')
            self.running()
            # try:
            #     self.running()
            # except:
            #     print('something wrong')
            sleep(self.delayAPI)


    def running(self) -> None:
        response: dict = self.indodaxDataSource.getTickerPairId('adaidr')
        response = response['ticker']
        scoreEma10 = self.ema10.getEMA(float(response["last"]))
        scoreEma20 = self.ema20.getEMA(float(response["last"]))

        emaCondition = 'undetected'
        if (scoreEma20 is not None and scoreEma10 is not None):
            # kondisi bersilangan naik waktu beli
            if (self.lastScoreEma10 < self.lastScoreEma20 and scoreEma10 > scoreEma20):
                emaCondition = 'buy'
            elif (self.lastScoreEma10 > self.lastScoreEma20 and scoreEma10 < scoreEma20):
                emaCondition = 'jual'
            else:
                emaCondition = 'waiting'
            self.lastScoreEma10 = scoreEma10
            self.lastScoreEma20 = scoreEma20

        if (scoreEma10 is None):
            scoreEma10 = 'xxx'
        if (scoreEma20 is None):
            scoreEma20 = 'xxx'

        Log.d('EMA 10', f'score {scoreEma10}')
        Log.d('EMA 20', f'score {scoreEma20}')
        Log.d('EMA Condition', f'score {emaCondition}')



        # self.telegramDataSource.sendPairData('ada idr\n\n' +
        #                                      f'harga ADAIDR\t: Rp. {response["last"]}\n' +
        #                                      f'EMA 10\t: Rp. {scoreEma10}\n' +
        #                                      f'EMA 20\t: Rp. {scoreEma20}\n' +
        #                                      f'harga beli\t: Rp. {response["buy"]}\n' + 
        #                                      f'harga jual\t: Rp. {response["sell"]}\n\n' +
        #                                      f'waktunya {emaCondition}')


if __name__ == '__main__':
    App()