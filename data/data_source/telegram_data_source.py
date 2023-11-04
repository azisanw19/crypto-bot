import asyncio

from telegram import Bot

from config.config import TELEGRAM_TOKEN_BOT, TELEGRAM_CHAT_GROUP_ID

class TelegramDataSource:
    token: str = TELEGRAM_TOKEN_BOT
    chatGroupId: str = TELEGRAM_CHAT_GROUP_ID

    def __init__(self) -> None:
        self.bot: Bot = Bot(self.token)

    async def asyncSendPairData(self, message: str) -> None:
        await self.bot.send_message(self.chatGroupId, message)

    def sendPairData(self, message: str) -> None:
        asyncio.get_event_loop().run_until_complete(
            self.asyncSendPairData(message=message)
        )