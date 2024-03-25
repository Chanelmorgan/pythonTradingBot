from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.trader import Trader
from datatime import datatime

API_KEY="PKDYCZSOAMMOIB53X8N4"
API_SECRET = "kGlVB1Y1acS6hPDiRgSNucdv35d9Y07th05cDza7"
BASE_URL = "https://paper-api.alpaca.markets/v2"


ALPACA_CRED = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

broker = Alpaca(ALPACA_CRED)