import os
import mplfinance as mpf
from matplotlib import pyplot as plt
import yfinance as yf
import time
import mplfinance as fplt
import pandas as pd
from matplotlib.ticker import ScalarFormatter
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from decimal import Decimal
import matplotlib.ticker as ticker
import base64
import json
import requests
from base64 import b64encode
from discord_webhook import DiscordWebhook , DiscordEmbed
import datetime as dt
import airtable
import matplotlib
import asyncio
import math
serverurl = 'http://ec2-3-15-166-190.us-east-2.compute.amazonaws.com'
pathdel = '/var/www/html/images/'
pathg = '/images/'
path = r'/var/www/html/images/'
sell_binance_bb = 'https://discord.com/api/webhooks/797826078243553280/dx9yUQO859yYXfwqKCnCgV7ReuhoXBUpp1_syzHdpe-If_VEh9xhNw973u8kzIlRd0vN'
sell_binance_stoch = 'https://discord.com/api/webhooks/797826154907303946/q5fgDYeuZDVfbDZfJzwycF0pjzg_WlaY7iDLNQstWhw3YZD-LscYPufhZcFbV6j_WF8M'
sell_binance_trap = 'https://discord.com/api/webhooks/797826219567218699/3x3Cwz21CcZlv8iHXMq5Igs4nbSMdrDa4m2byKm2_4U0YZomQ5of9XyEKZPLm3cdXuLl'
sell_binance_inside = 'https://discord.com/api/webhooks/797826283077763102/oKF0swmRb0v-au132BihX_emUh_F9803lZMPH1KP8ZoF8HkCMwlm_O15F2nAOUChfZVf'
buy_binance_bb = 'https://discord.com/api/webhooks/797826785982939146/4eIob-9IrVGaPjPez2_qXUUg-MleESVDMcdZncIeU5TdjhiHCw9zb7Bfm7mAoeIYrkk1'
buy_binance_stoch = 'https://discord.com/api/webhooks/797826847962169374/gD90STNg7oPw5siqZAUDKYZ2X7pd3FWy1zY0kIMq54oUpFrw5ybxZFrwDabkpx4t5YS1'
buy_binance_trap = 'https://discord.com/api/webhooks/800241202641240104/D0hrAUzkm5SllEccs0O0GBZQxmOKVOP2NYEWpjSvaRS_PdYUvEX3aAlug9eH7ANDhZLW'
buy_binance_inside = 'https://discord.com/api/webhooks/797826906245562368/9jr7E89YxRk3SyzxaCBtXbCiZIrQrSgQsk8jOgYzZiMwBL8qxJlWW5dOPodv9tU2ekem'
matplotlib.use('Agg')
end = dt.datetime.date(dt.datetime.today())
dayss = dt.timedelta(310)
start = end - dayss
at = airtable.Airtable('appyNonWWt3lSoTfP','Signals', 'keyBEQtPBFnA0s8IA')
at2 = airtable.Airtable('appyNonWWt3lSoTfP','Assets', 'keyBEQtPBFnA0s8IA')
stocks = []
long_term_positive = []
short_term_positive = []
long_term_negative = []
short_term_negative = []
def STOD(close, low, high, n):
 STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
 mam = STOK.rolling(3).mean()
 STOD = mam.rolling(3).mean()
 return STOD
def STOK(close, low, high, n):
 STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
 mam = STOK.rolling(3).mean()
 return mam
def format_price(x, _=None):
    x = Decimal(x)
def ema_calc_binance(stock):
 df = get_binance_for_ema(stock)
 spisok = []
 if len(df) >= 280:
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    endik = str(end)
    try:
        if endik in df['ema50'] :
            if df['ema50'][endik] > df['ema100'][endik] > df['ema200'][endik]:
                spisok.append(1)
            if df['ema10'][endik] > df['ema20'][endik] > df['ema30'][endik]:
                spisok.append(2)
            if df['ema50'][endik] < df['ema100'][endik] < df['ema200'][endik]:
                spisok.append(3)
            if df['ema10'][endik] < df['ema20'][endik] < df['ema30'][endik]:
                spisok.append(4)
    except:
        pass
    print(spisok)
 return spisok
def get_binance_for_ema(stock):
    df = requests.get('https://api.binance.com/api/v3/klines?symbol='+stock+'&interval=1d&limit=280')
    print(df.text)
    aa = json.loads(df.text)
    print(len(aa))
    ftxclose = []
    ftxopen = []
    ftxlow = []
    ftxhigh = []
    ftxstarttime = []
    for i in range(len(aa)):
        ftxclose.append(float(aa[i][4]))
        ftxopen.append(float(aa[i][1]))
        ftxlow.append(float(aa[i][3]))
        ftxhigh.append(float(aa[i][2]))
        ftxstarttime.append(str(dt.datetime.fromtimestamp(int(str((aa[i][6]))[:-3])))[:-9])
    df = pd.DataFrame({
    'Close' : ftxclose,
    'Open' : ftxopen,
    'Low' : ftxlow,
    'High' : ftxhigh,
    }, index = ftxstarttime)
    return df
def get_binance(stock):
    df = requests.get('https://api.binance.com/api/v3/klines?symbol='+stock+'&interval=1d&limit=280')
    print(df.text)
    aa = json.loads(df.text)
    print(len(aa))
    ftxclose = []
    ftxopen = []
    ftxlow = []
    ftxhigh = []
    ftxstarttime = []
    for i in range(len(aa)):
        ftxclose.append(float(aa[i][4]))
        ftxopen.append(float(aa[i][1]))
        ftxlow.append(float(aa[i][3]))
        ftxhigh.append(float(aa[i][2]))
        ftxstarttime.append((dt.datetime.fromtimestamp(int(str((aa[i][6]))[:-3]))))
    df = pd.DataFrame({
    'Close' : ftxclose,
    'Open' : ftxopen,
    'Low' : ftxlow,
    'High' : ftxhigh,
    }, index = ftxstarttime)
    return df
def bb_drawer_binance(stock,islong,positivetrend):
        df = get_binance(stock)
        if len(df) >= 280:
            period = 20
            multiplier = 2
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
            df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
            df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df = df.iloc[-180:]
            apd = fplt.make_addplot(df['LowerBand'], color='grey')
            apdd = fplt.make_addplot(df['UpperBand'], color='grey')
            if df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]] and islong and positivetrend:
                apdddddd = fplt.make_addplot(df['ema50'])
                apddddddd = fplt.make_addplot(df['ema100'])
                apdddddddd = fplt.make_addplot(df['ema200'])
                fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                plt.savefig(path + stock + '1longbuy.png', dpi=250)
                a = serverurl + pathg + stock + '1longbuy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'long','entry' : df['Close'][df.index][-1], 'Graph' : a }, typecast=True)
            elif df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]] and islong and not(positivetrend):
                apdddddd = fplt.make_addplot(df['ema50'])
                apddddddd = fplt.make_addplot(df['ema100'])
                apdddddddd = fplt.make_addplot(df['ema200'])
                fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                plt.savefig(path + stock + '1longsell.png', dpi=250)
                a = serverurl + pathg + stock + '1longsell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
               'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'long', 'entry': df['Close'][df.index][-1],
               'Graph': a}, typecast=True)
def osc_drawer_binance(stock,islong,positivetrend):
    df = get_binance(stock)
    df['70'] = 70
    df['30'] = 30
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df['%K'] = STOK(df['Close'], df['Low'], df['High'], 10)
    df['%D'] = STOD(df['Close'], df['Low'], df['High'], 10)
    df = df.iloc[-180:]
    stoch1 = fplt.make_addplot(df['%K'], panel=1)
    stoch2 = fplt.make_addplot(df['%D'], panel=1)
    level70 = fplt.make_addplot(df['70'], panel=1, color='gray')
    level30 = fplt.make_addplot(df['30'], panel=1, color='gray')
    if df["%K"][df.index[-1]] < 30 and islong and positivetrend :
        df = df.iloc[-180:]
        stoch1 = fplt.make_addplot(df['%K'], panel=1)
        stoch2 = fplt.make_addplot(df['%D'], panel=1)
        level70 = fplt.make_addplot(df['70'], panel=1, color='gray')
        level30 = fplt.make_addplot(df['30'], panel=1, color='gray')
        ema50 = fplt.make_addplot(df['ema50'])
        ema100 = fplt.make_addplot(df['ema100'])
        ema200 = fplt.make_addplot(df['ema200'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[stoch1,stoch2, ema50, ema100, ema200, level30, level70], returnfig=True)
        plt.savefig(path + stock + '2longbuy.png', dpi=250)
        plt.close(fig)
        a = serverurl + pathg + stock + '2longbuy.png'
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Sell or Buy': 'Buy', 'Trend': 'long','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]],'Graph' : a},
                  typecast=True)
    elif df["%K"][df.index[-1]] > 70 and islong and not(positivetrend) :
        ema50 = fplt.make_addplot(df['ema50'])
        ema100 = fplt.make_addplot(df['ema100'])
        ema200 = fplt.make_addplot(df['ema200'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[stoch1,stoch2, ema50, ema100, ema200, level30, level70], returnfig=True)
        plt.savefig(path + stock + '2longsell.png', dpi=250)
        a = serverurl + pathg + stock + '2longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance', 'Sell or Buy' : 'Sell', 'Trend' : 'long','Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]] , 'Graph' : a},
            typecast=True)
def trap_drawer_binance(stock,islong,positivetrend):
    df = get_binance(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df = df.iloc[-180:]
    if df['Low'][df.index[-1]] < df['Low'][df.index[-2]] and df['Low'][df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] and positivetrend:
        apddd = fplt.make_addplot(df['ema10'])
        apdddd = fplt.make_addplot(df['ema20'])
        apddddd = fplt.make_addplot(df['ema30'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apddd, apdddd, apddddd], returnfig=True)
        plt.savefig(path + stock + '3buy.png', dpi=250)
        a = serverurl + pathg + stock + '3buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance','Strategies': 'Trap_bar', 'Sell or Buy': 'Buy', 'Trend': 'Short', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]] and not(positivetrend) :
        apddd = fplt.make_addplot(df['ema10'])
        apdddd = fplt.make_addplot(df['ema20'])
        apddddd = fplt.make_addplot(df['ema30'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apddd, apdddd, apddddd], returnfig=True)
        plt.savefig(path + stock + '3sell.png', dpi=250)
        a = serverurl + pathg + stock + '3sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]) , 'Graph' : a }, typecast=True)
def inside_drawer_binance(stock,islong,positivetrend):
    df = get_binance(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df = df.iloc[-180:]
    if df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]]  and positivetrend:
        apddd = fplt.make_addplot(df['ema10'])
        apdddd = fplt.make_addplot(df['ema20'])
        apddddd = fplt.make_addplot(df['ema30'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apddd, apdddd, apddddd], returnfig=True)
        plt.savefig(path + stock + '4buy.png', dpi=250)
        a = serverurl + pathg + stock + '4buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date' : str(dt.datetime.date(dt.datetime.today())), 'Markets' : 'binance', 'Strategies' : 'Inside_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'short','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a }, typecast= True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and not(positivetrend) :
        apddd = fplt.make_addplot(df['ema10'])
        apdddd = fplt.make_addplot(df['ema20'])
        apddddd = fplt.make_addplot(df['ema30'])
        fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        plt.savefig(path + stock + '4sell.png', dpi=250)
        a = serverurl + pathg + stock + '4sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend': 'short', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)