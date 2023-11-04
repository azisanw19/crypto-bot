from collections import deque

from config.config import SMOOTHING

class ExponentialMovingAverage:
    alpha = SMOOTHING

    def __init__(self, length) -> None:
        self.length = length
        self.queue = deque()

    def newData(self, item: int):
        if (len(self.queue) < self.length):
            self.queue.append(item)
        else:
            self.queue.popleft()
            self.queue.append(item)

    def exponentialMovingAverageLast(self, data, alpha) -> float:
        ema = data[0]  # Inisialisasi EMA dengan nilai pertama data

        for i in range(1, len(data)):
            ema = alpha * data[i] + (1 - alpha) * ema

        return ema
    
    def getEMA(self, lastPrice: float) -> float:
        self.newData(lastPrice)
        if (len(self.queue) == self.length):
            return self.exponentialMovingAverageLast(self.queue, self.alpha)
        else:
            return None