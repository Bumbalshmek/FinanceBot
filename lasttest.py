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
import matplotlib
from decimal import Decimal
import matplotlib.ticker as ticker
import base64
import json
import requests
from base64 import b64encode
from discord_webhook import DiscordWebhook
import datetime as dt
import airtable
import matplotlib
pathdel = '/var/www/html/images/'
pathg = '/images/'
path = r'/var/www/html/images/'
serverurl = 'http://ec2-3-128-90-98.us-east-2.compute.amazonaws.com'
long_usa_bb = 'https://discord.com/api/webhooks/797804598366175263/Jb0rg2WCWRRmljCDK08xg-sdBq601ZnzSCKCgUMYl_ivEefcd-nIkZ1uGp0jfJ4JgPJ-'
long_usa_stoch = 'https://discord.com/api/webhooks/797805113074778182/FJ82LcoWCtwSIWPdsfC4DHqZJkKolgE_r27VMdjttlXzGI9Ti7IO9UsoyDALoCQTb5Be'
long_usa_trap = 'https://discord.com/api/webhooks/797804893846896670/CAkDcOpnbzgJfTVhDa7U7JfKrkVCPNKoMbVlxnjJybmSVjyzXwpJWx8Iawye83lKS0-W'
long_usa_inside = 'https://discord.com/api/webhooks/797805251071180800/f0SYI3NeezioyTiLW0dHN3n4Rdv3KsOySefO7ykcLv397F4Hj1nxSjeVxSO_XOt8SL1_'
short_usa_bb = 'https://discord.com/api/webhooks/797805892057694208/h15lbZTkxMrVxZgMmlVEa4jGhJOf7F8qZaR0FzEGocMFtAQ713qXbvv762G-gLRzqA_J'
short_usa_stoch = 'https://discord.com/api/webhooks/797805990900793350/3bApb2HFi2IBKj3y4UoE-ncs2SXAKCU1Gr1TTbL9wUSMIMgLHRx3Lt8r22_naBEmXM4H'
short_usa_trap = 'https://discord.com/api/webhooks/797806057207889942/3a4pe5wngQlMWAhPF2sWe-PcDa3iYKiQF2-hkyUjnQfOpQq-dUys0fK0FFv0ttLsfnVq'
short_usa_inside = 'https://discord.com/api/webhooks/797806149160140820/vaO8QJz_GyPEbMH4L1z6CeaNyyoRfA06f8wqSVbLh11NVPt_jpP2nUQWoRYoOTZGKcdj'
long_br_bb = 'https://discord.com/api/webhooks/797806633660842016/VsOQEHkV6CDewbCYgVwOtDMxB8Vfc-FrtZVFvbPMzM7RsruZ7ZC2EBWBfw-j1Xod9o8b'
long_br_stoch = 'https://discord.com/api/webhooks/797806724454678548/oE6NL4bv6OTpqwPs-bfYR6YoAX3NX-Nrj1i5I-RxRvPaEKoD64qo-ibYqtfMA3RuyVsO'
long_br_trap = 'https://discord.com/api/webhooks/797806874346258452/hlUMiomlSRwXfGTHSx9VsecnhT00KUcWTRvLV9OQ9zSe0gKyTTcKqldfqKf8DG-LX7Ps'
long_br_inside = 'https://discord.com/api/webhooks/797806952196734976/ND7uqe9TWfqRLRRGOVZOTbHSL9pD2AZ32X3vZo89pu_6PK108YrB5LADCQziyQMUKg_u'
short_br_bb = 'https://discord.com/api/webhooks/797807019817304104/NZgNzG4I99KTBGOn1eUM3D_45qRQaWPLMANsOL35UjCzuE6KvBhj-c6Axr5rdclwngdy'
short_br_stoch = 'https://discord.com/api/webhooks/797807082527129630/02VF-b-jdlHnylsnzX9A3pGf7shppbnTFlHrZ4ArwdJbDpSWQrbYTa5SGO3rmvFnMOh1'
short_br_trap = 'https://discord.com/api/webhooks/797807315503153162/oLveIewwzLctnUdYKMZnuePZrL-hHXgdijrHjF4pE4pPZKenVOeyIYCsYecYfS2HjohK'
short_br_inside = 'https://discord.com/api/webhooks/797807148397494272/eAht1PTe7o4tDAO9HvCfp48WK1D6O2AxgfyKlMoOxBb5ETP24ioDg-Zay_DozA6NloZ8'
long_ftx_bb = 'https://discord.com/api/webhooks/797807577559728159/XoqCbJuciR0tyJvWAdsAqCo2CGao64xQJlEdtsU9nZ98E8Xi_TjxdwbmT7C8TzJulu1y'
long_ftx_stoch = 'https://discord.com/api/webhooks/797807654528483328/XyV322IteMf368q_oQa5UB1zxCVZsFHDJZVO7c03yNPUTLkFJ1Op83KAitcsZ7HBMRn3'
long_ftx_trap = 'https://discord.com/api/webhooks/797807711600508929/E1FMkpP9jcg1eD2s1nxfUKXoDmXel2X9XX2NBV16rOErJDHfpxuu42JIVMVxzcHIB7gj'
long_ftx_inside = 'https://discord.com/api/webhooks/797807774217142272/TBxgapTAPanMoDKMdgJCaLT4XlG7pEemRKE9yrhMzTR68gNqADL0S5xbktzO-HUiwpKR'
short_ftx_bb = 'https://discord.com/api/webhooks/797808005839454209/kNvcrIAYtRI266HrdPYdDXVar3z9X_-pITz2SjjVCMd9xm08Zd0Q875G35MsfX1Y717O'
short_ftx_stoch = 'https://discord.com/api/webhooks/797825507491315752/UlycIpHotDmJgngk6xFXQvUZT6cci8w906lqrNwBJWKdJrHx_eVlhDWIYBROMZYUnCgS'
short_ftx_trap = 'https://discord.com/api/webhooks/797825619744260156/5_66Um8cj5-VbWJB8T63Dj7s4fQRPdQJTMyRo9d3dnN9SoqAzdZKewLVx3pYDwDQ8ebR'
short_ftx_inside = 'https://discord.com/api/webhooks/797825798803292193/cDXCtDR9PaMMo67qtQbr_C4pi8BBq9Zl79yCgDa3IHzw3CJ4Y7UcYvxbujy7a3ADVQ-2'
long_binance_bb = 'https://discord.com/api/webhooks/797826078243553280/dx9yUQO859yYXfwqKCnCgV7ReuhoXBUpp1_syzHdpe-If_VEh9xhNw973u8kzIlRd0vN'
long_binance_stoch = 'https://discord.com/api/webhooks/797826154907303946/q5fgDYeuZDVfbDZfJzwycF0pjzg_WlaY7iDLNQstWhw3YZD-LscYPufhZcFbV6j_WF8M'
long_binance_trap = 'https://discord.com/api/webhooks/797826219567218699/3x3Cwz21CcZlv8iHXMq5Igs4nbSMdrDa4m2byKm2_4U0YZomQ5of9XyEKZPLm3cdXuLl'
long_binance_inside = 'https://discord.com/api/webhooks/797826283077763102/oKF0swmRb0v-au132BihX_emUh_F9803lZMPH1KP8ZoF8HkCMwlm_O15F2nAOUChfZVf'
short_binance_bb = 'https://discord.com/api/webhooks/797826785982939146/4eIob-9IrVGaPjPez2_qXUUg-MleESVDMcdZncIeU5TdjhiHCw9zb7Bfm7mAoeIYrkk1'
short_binance_stoch = 'https://discord.com/api/webhooks/797826847962169374/gD90STNg7oPw5siqZAUDKYZ2X7pd3FWy1zY0kIMq54oUpFrw5ybxZFrwDabkpx4t5YS1'
short_binance_trap = 'https://discord.com/api/webhooks/797826998957244426/iFzE0Z63p5hc66VbJk6TIQNOICXjnRbp9COhn0iaVQ8lccRPPObVn1NyRdqh_fFNhKfB'
short_binance_inside = 'https://discord.com/api/webhooks/797826906245562368/9jr7E89YxRk3SyzxaCBtXbCiZIrQrSgQsk8jOgYzZiMwBL8qxJlWW5dOPodv9tU2ekem'
filelist = [ f for f in os.listdir(pathdel) if f.endswith(".png") ]
for f in filelist:
    os.remove(os.path.join(pathdel, f))
matplotlib.use('Agg')
end = dt.datetime.date(dt.datetime.today())
dayss = dt.timedelta(280)
start = end - dayss
days = dt.timedelta(1)
at = airtable.Airtable('appyNonWWt3lSoTfP','Signals', 'keyBEQtPBFnA0s8IA')
at2 = airtable.Airtable('appyNonWWt3lSoTfP','Assets', 'keyBEQtPBFnA0s8IA')
long_term_positive = []
short_term_positive = []
long_term_negative = []
short_term_negative = []
def format_price(x, _=None):
    x = Decimal(x)
    return x.quantize(Decimal(1)) if x == x.to_integral() else x.normalize()
def bb_drawer_usa(stock,islong,start_time = start, end_time = end):
        df = yf.download(stock ,start= start_time, end = end_time)
        if len(df) >= 193:
            period = 20
            multiplier = 2
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
            df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
            df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
            df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
            df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
            df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
            df = df.iloc[-180:]
            if df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longsell.png', dpi=250)
                a = serverurl + pathg + stock + '1longsell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'long' , 'entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longbuy.png', dpi=250)
                a = serverurl + pathg + stock + '1longbuy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'long','entry' : df['Close'][df.index][-1], 'Graph' : a }, typecast=True)
            elif df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1sell.png', dpi=250)
                a = serverurl + pathg + stock + '1sell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph': a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1buy.png', dpi=250)
                a = serverurl + pathg + stock + '1buy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
def osc_drawer_usa(stock,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df['%K'] = STOK(df['Close'], df['Low'], df['High'], 10)
    if df["%K"][df.index[-1]] > 70 and islong:
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longsell.png', dpi=250)
        a = serverurl + pathg + stock + '2longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks', 'Sell or Buy' : 'Sell', 'Trend' : 'long','Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]] , 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] > 70 :
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2sell.png', dpi=250)
        plt.close(fig)
        a = serverurl + pathg + stock + '2sell.png'
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks', 'Sell or Buy' : 'Sell', 'Trend' : 'short', 'Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] < 30 and islong:
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longbuy.png', dpi=250)
        plt.close(fig)
        a = serverurl + pathg + stock + '2longbuy.png'
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Sell or Buy': 'Buy', 'Trend': 'long','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]],'Graph' : a},
                  typecast=True)
    elif df["%K"][df.index[-1]] < 30 :
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2buy.png', dpi=250)
        plt.close(fig)
        a = serverurl + pathg + stock + '2buy.png'
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Sell or Buy': 'Buy', 'Trend': 'short','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
def trap_drawer_usa(stock,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['Low'][df.index[-1]] <df['Low'][df.index[-2]] and df['Low'][
        df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longbuy.png', dpi=250)
        plt.close(fig)
        a = serverurl + pathg + stock + '3longbuy.png'
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Strategies': 'Trap_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'long', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]) , 'Graph' : a }, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longsell.png', dpi=250)
        a = serverurl + pathg + stock + '3longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'long','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['Low'][df.index[-1]] < df['Low'][df.index[-2]] and df['Low'][df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] :
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3buy.png', dpi=250)
        a = serverurl + pathg + stock + '3buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Buy', 'Trend': 'Short', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]]:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3sell.png', dpi=250)
        a = serverurl + pathg + stock + '3sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]) , 'Graph' : a }, typecast=True)
def inside_drawer_usa(stock,isbuy,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    if df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4buy.png', dpi=250)
        a = serverurl + pathg + stock + '4buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date' : str(dt.datetime.date(dt.datetime.today())), 'Markets' : 'Usa_stocks', 'Strategies' : 'Inside_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'short','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a }, typecast= True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]]:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4sell.png', dpi=250)
        a = serverurl + pathg + stock + '4sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend': 'short', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '4longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Buy', 'Trend' : 'long','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longsell.png', dpi=250)
        a = serverurl + pathg + stock + '4longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Usa_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend' : 'long', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
def STOK(close, low, high, n):
 STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
 mam = STOK.rolling(3).mean()
 return mam
def ema_calc(stock,start_time=start,end_time=end):
    df = yf.download(stock ,start= start_time, end = end_time)
    spisok = []
    print(len(df))
    print(df)
    endik = str(end - dt.timedelta(1))
    if len(df) >= 180:
        df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
        df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
        df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
        df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
        df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
        df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
        print(df)
        indexesForRemove = []
        for i in range(len(df)):
            if len(str(df['Open'][i])) == 3:
                indexesForRemove.append(df.index[i])
        for index in indexesForRemove:
            df = df.drop(index)
        print(df)
        try:
            if endik in df['ema50']:
                if df['ema50'][endik] > df['ema100'][endik] > df['ema200'][endik]:
                    spisok.append(1)
                if df['ema10'][endik] > df['ema20'][endik] > df['ema30'][endik]:
                     spisok.append(2)
                if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
                     spisok.append(3)
                if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
                    spisok.append(4)
        except:
            pass
    return spisok
def bb_drawer_br(stock,islong,start_time = start, end_time = end):
        df = yf.download(stock ,start= start_time, end = end_time)
        if len(df) >= 180:
            period = 20
            multiplier = 2
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
            df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
            df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
            df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
            df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
            df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df = df.iloc[-180:]
            if df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longsell.png', dpi=250)
                a = serverurl + pathg + stock + '1longsell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'long' , 'entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longbuy.png', dpi=250)
                a = serverurl + pathg + stock + '1longbuy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'long','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1sell.png', dpi=250)
                a = serverurl + pathg + stock + '1sell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
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
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1buy.png', dpi=250)
                a = serverurl + pathg + stock + '1buy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
def osc_drawer_br(stock,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df['%K'] = STOK(df['Close'], df['Low'], df['High'], 10)
    if df["%K"][df.index[-1]] > 70 and islong:
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longsell.png', dpi=250)
        a = serverurl + pathg + stock + '2longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks', 'Sell or Buy' : 'Sell', 'Trend' : 'long','Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] > 70 :
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2sell.png', dpi=250)
        a = serverurl + pathg + stock + '2sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks', 'Sell or Buy' : 'Sell', 'Trend' : 'short', 'Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] < 30 and islong:
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '2longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Sell or Buy': 'Buy', 'Trend': 'long','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
    elif df["%K"][df.index[-1]] < 30 :
        df = df.iloc[-180:]
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2buy.png', dpi=250)
        a = serverurl + pathg + stock + '2buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Sell or Buy': 'Buy', 'Trend': 'short','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
def trap_drawer_br(stock,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['Low'][df.index[-1]] <df['Low'][df.index[-2]] and df['Low'][
        df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '3longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Strategies': 'Trap_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'long', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a }, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longsell.png', dpi=250)
        a = serverurl + pathg + stock + '3longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'long','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['Low'][df.index[-1]] < df['Low'][df.index[-2]] and df['Low'][df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] :
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3buy.png', dpi=250)
        a = serverurl + pathg + stock + '3buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Buy', 'Trend': 'Short', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]]:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3sell.png', dpi=250)
        a = serverurl + pathg + stock + '3sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]) , 'Graph' : a }, typecast=True)
def inside_drawer_br(stock,isbuy,islong,start_time = start, end_time = end):
    df = yf.download(stock ,start= start_time, end = end_time)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    if df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4buy.png', dpi=250)
        a = serverurl + pathg + stock + '4buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date' : str(dt.datetime.date(dt.datetime.today())), 'Markets' : 'Br_stocks', 'Strategies' : 'Inside_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'short','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a }, typecast= True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]]:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4sell.png', dpi=250)
        a = serverurl + pathg + stock + '4sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend': 'short', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '4longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Buy', 'Trend' : 'long','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and islong:
        df = df.iloc[-180:]
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longsell.png', dpi=250)
        a = serverurl + pathg + stock + '4longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'Br_stocks',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend' : 'long', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
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
            if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
                spisok.append(3)
            if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
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
def bb_drawer_binance(stock,islong):
        df = get_binance(stock)
        if len(df) >= 280:
            period = 20
            multiplier = 2
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
            df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
            df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
            df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
            df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
            df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df = df.iloc[-180:]
            if df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longsell.png', dpi=250)
                a = serverurl + pathg + stock + '1longsell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'long' , 'entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longbuy.png', dpi=250)
                a = serverurl + pathg + stock + '1longbuy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'long','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1sell.png', dpi=250)
                a = serverurl + pathg + stock + '1sell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1buy.png', dpi=250)
                a = serverurl + pathg + stock + '1buy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
def osc_drawer_binance(stock,islong):
    df = get_binance(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df['%K'] = STOK(df['Close'], df['Low'], df['High'], 10)
    df = df.iloc[-180:]
    if df["%K"][df.index[-1]] > 70 and islong:
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longsell.png', dpi=250)
        a = serverurl + pathg + stock + '2longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance', 'Sell or Buy' : 'Sell', 'Trend' : 'long','Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] > 70 :
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2sell.png', dpi=250)
        a = serverurl + pathg + stock + '2sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance', 'Sell or Buy' : 'Sell', 'Trend' : 'short', 'Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] < 30 and islong:
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '2longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Sell or Buy': 'Buy', 'Trend': 'long','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
    elif df["%K"][df.index[-1]] < 30 :
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2buy.png', dpi=250)
        a = serverurl + pathg + stock + '2buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Sell or Buy': 'Buy', 'Trend': 'short','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
def trap_drawer_binance(stock,islong):
    df = get_binance(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['Low'][df.index[-1]] <df['Low'][df.index[-2]] and df['Low'][
        df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '3longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Strategies': 'Trap_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'long', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a }, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longsell.png', dpi=250)
        a = serverurl + pathg + stock + '3longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'long','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['Low'][df.index[-1]] < df['Low'][df.index[-2]] and df['Low'][df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] :
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3buy.png', dpi=250)
        a = serverurl + pathg + stock + '3buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance','Strategies': 'Trap_bar', 'Sell or Buy': 'Buy', 'Trend': 'Short', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]]:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3sell.png', dpi=250)
        a = serverurl + pathg + stock + '3sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a }, typecast=True)
def inside_drawer_binance(stock, isbuy, islong):
    df = get_binance(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4buy.png', dpi=250)
        a = serverurl + pathg + stock + '4buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date' : str(dt.datetime.date(dt.datetime.today())), 'Markets' : 'binance', 'Strategies' : 'Inside_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'short','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a }, typecast= True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]]:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4sell.png', dpi=250)
        a = serverurl + pathg + stock + '4sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend': 'short', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)

    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '4longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Buy', 'Trend' : 'long','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a}, typecast=True)

    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longsell.png', dpi=250)
        a = serverurl + pathg + stock + '4longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'binance',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend' : 'long', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
def ema_calc_ftx(stock):
 df = getftx_for_ema(stock)
 df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
 df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
 df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
 df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
 df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
 df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
 endik = str(end - dt.timedelta(1))
 spisok = []
 try:
    if endik in df['ema50'] and len(df) >= 280:
        if df['ema50'][endik] > df['ema100'][endik] > df['ema200'][endik]:
            spisok.append(1)
        if df['ema10'][endik] > df['ema20'][endik] > df['ema30'][endik]:
            spisok.append(2)
        if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
            spisok.append(3)
        if df['ema10'][endik] > df['ema10'][endik] > df['ema10'][endik]:
            spisok.append(4)
        print(spisok)
 except:
     pass
 return spisok
def bb_drawer_ftx(stock,islong):
        df = getftx(stock)
        if len(df) >= 280:
            period = 20
            multiplier = 2
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
            df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
            df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
            df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
            df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
            df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
            df['UpperBand'] = df['Close'].rolling(period).mean() + df['Close'].rolling(period).std() * multiplier
            df['LowerBand'] = df['Close'].rolling(period).mean() - df['Close'].rolling(period).std() * multiplier
            df = df.iloc[-180:]
            if df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longsell.png', dpi=250)
                a = serverurl + pathg + stock + '1longsell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'long' , 'entry' : df['Close'][df.index][-1], 'Grapg' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]] and islong:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1longbuy.png', dpi=250)
                a = serverurl + pathg + stock + '1longbuy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'long','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] > df['UpperBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1sell.png', dpi=250)
                a = serverurl + pathg + stock + '1sell.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
            elif df['Close'][df.index[-1]] < df['LowerBand'][df.index[-1]]:
                apd = fplt.make_addplot(df['LowerBand'])
                apdd = fplt.make_addplot(df['UpperBand'])
                if islong:
                    apdddddd = fplt.make_addplot(df['ema50'])
                    apddddddd = fplt.make_addplot(df['ema100'])
                    apdddddddd = fplt.make_addplot(df['ema200'])
                    print(df)
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apdddddd, apdddddddd, apddddddd], returnfig=True)
                else:
                    apddd = fplt.make_addplot(df['ema10'])
                    apdddd = fplt.make_addplot(df['ema20'])
                    apddddd = fplt.make_addplot(df['ema30'])
                    fig, axlist = fplt.plot(
                        df,
                        type="candle",
                        title=stock,
                        ylabel='Price($)',
                        style='charles',
                        addplot=[apd, apdd, apddd, apdddd, apddddd], returnfig=True)
                ax1 = axlist[0]
                ax1_minor_yticks = ax1.get_yticks(True)
                ax1_major_yticks = ax1.get_yticks(False)
                ax1.set_yscale('log')
                ax1.set_yticks(ax1_major_yticks, True)
                ax1.set_yticks(ax1_minor_yticks, False)
                ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
                ax1.yaxis.grid(True, which='minor')
                plt.savefig(path + stock + '1buy.png', dpi=250)
                a = serverurl + pathg + stock + '1buy.png'
                plt.close(fig)
                at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                           'Strategies': 'Bollinger', 'Sell or Buy': 'Buy', 'Trend': 'Short','entry' : df['Close'][df.index][-1], 'Graph' : a}, typecast=True)
def osc_drawer_ftx(stock,islong):
    df = getftx(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df['%K'] = STOK(df['Close'], df['Low'], df['High'], 10)
    df = df.iloc[-180:]
    if df["%K"][df.index[-1]] > 70 and islong:
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longsell.png', dpi=250)
        a = serverurl + pathg + stock + '2longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX', 'Sell or Buy' : 'Sell', 'Trend' : 'long','Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] > 70 :
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2sell.png', dpi=250)
        a = serverurl + pathg + stock + '2sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX', 'Sell or Buy' : 'Sell', 'Trend' : 'short', 'Strategies' : 'stoch', 'entry': df['High'][df.index[-1]], 'close' : df['Low'][df.index[-1]], 'Graph' : a},
            typecast=True)
    elif df["%K"][df.index[-1]] < 30 and islong:
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '2longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Sell or Buy': 'Buy', 'Trend': 'long','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
    elif df["%K"][df.index[-1]] < 30 :
        apd = fplt.make_addplot(df['%K'])
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
            apddd = fplt.make_addplot(df['ema10'])
            apdddd = fplt.make_addplot(df['ema20'])
            apddddd = fplt.make_addplot(df['ema30'])
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apd, apddd, apdddd, apddddd], returnfig=True)
        ax1 = axlist[0]
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '2buy.png', dpi=250)
        a = serverurl + pathg + stock + '2buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Sell or Buy': 'Buy', 'Trend': 'short','Strategies' : 'stoch', 'entry': df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a},
                  typecast=True)
def trap_drawer_ftx(stock,islong):
    df = getftx(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['Low'][df.index[-1]] <df['Low'][df.index[-2]] and df['Low'][
        df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '3longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Strategies': 'Trap_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'long', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph' : a }, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3longsell.png', dpi=250)
        a = serverurl + pathg + stock + '3longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'long','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a}, typecast=True)
    elif df['Low'][df.index[-1]] < df['Low'][df.index[-2]] and df['Low'][df.index[-1]] < df['Low'][df.index[-3]] and df['Close'][df.index[-1]] >= df['Open'][df.index[-1]] :
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3buy.png', dpi=250)
        a = serverurl + pathg + stock + '3buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX','Strategies': 'Trap_bar', 'Sell or Buy': 'Buy', 'Trend': 'Short', 'entry' : str(df['Low'][df.index[-1]]), 'close' : str(df['High'][df.index[-1]]), 'Graph': a}, typecast=True)
    elif df['High'][df.index[-1]] > df['High'][df.index[-2]] and df['High'][df.index[-1]] > df['High'][df.index[-3]] and df['Close'][df.index[-1]] <= df['Open'][df.index[-1]]:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '3sell.png', dpi=250)
        a = serverurl + pathg + stock + '3sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX','Strategies': 'Trap_bar', 'Sell or Buy': 'Sell', 'Trend': 'Short','entry' : str(df['High'][df.index[-1]]) , 'close' : str(df['Low'][df.index[-1]]), 'Graph' : a }, typecast=True)
def inside_drawer_ftx(stock, isbuy, islong):
    df = getftx(stock)
    df['ema10'] = pd.Series.ewm(df['Close'], span=10, adjust=False).mean()
    df['ema20'] = pd.Series.ewm(df['Close'], span=20, adjust=False).mean()
    df['ema30'] = pd.Series.ewm(df['Close'], span=30, adjust=False).mean()
    df['ema50'] = pd.Series.ewm(df['Close'], span=50, adjust=False).mean()
    df['ema100'] = pd.Series.ewm(df['Close'], span=100, adjust=False).mean()
    df['ema200'] = pd.Series.ewm(df['Close'], span=200, adjust=False).mean()
    df = df.iloc[-180:]
    if df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4buy.png', dpi=250)
        a = serverurl + pathg + stock + '4buy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date' : str(dt.datetime.date(dt.datetime.today())), 'Markets' : 'FTX', 'Strategies' : 'Inside_bar', 'Sell or Buy' : 'Buy', 'Trend' : 'short','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a }, typecast= True)

    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]]:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4sell.png', dpi=250)
        a = serverurl + pathg + stock + '4sell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend': 'short', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and isbuy and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longbuy.png', dpi=250)
        a = serverurl + pathg + stock + '4longbuy.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Buy', 'Trend' : 'long','entry' : df['Low'][df.index[-1]], 'close' : df['High'][df.index[-1]], 'Graph' : a}, typecast=True)

    elif df['High'][df.index[-1]] <= df['High'][df.index[-2]] and df['Low'][df.index[-1]] >= df['Low'][df.index[-2]] and islong:
        if islong:
            apdddddd = fplt.make_addplot(df['ema50'])
            apddddddd = fplt.make_addplot(df['ema100'])
            apdddddddd = fplt.make_addplot(df['ema200'])
            print(df)
            fig, axlist = fplt.plot(
                df,
                type="candle",
                title=stock,
                ylabel='Price($)',
                style='charles',
                addplot=[apdddddd, apdddddddd, apddddddd], returnfig=True)
        else:
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
        ax1_minor_yticks = ax1.get_yticks(True)
        ax1_major_yticks = ax1.get_yticks(False)
        ax1.set_yscale('log')
        ax1.set_yticks(ax1_major_yticks, True)
        ax1.set_yticks(ax1_minor_yticks, False)
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.set_minor_formatter(ticker.FuncFormatter(format_price))
        ax1.yaxis.grid(True, which='minor')
        plt.savefig(path + stock + '4longsell.png', dpi=250)
        a = serverurl + pathg + stock + '4longsell.png'
        plt.close(fig)
        at.insert({'ID': str(stock), 'Date': str(dt.datetime.date(dt.datetime.today())), 'Markets': 'FTX',
                   'Strategies': 'Inside_bar', 'Sell or Buy': 'Sell', 'Trend' : 'long', 'entry' : df['High'][df.index[-1]] , 'close' : df['Low'][df.index[-1]], 'Graph' : a}, typecast=True)
def getftx(stock):
    ff = requests.get('https://ftx.com/api/markets/'+stock+'/candles?resolution=86400&limit=280')
    ff = json.loads(ff.text)
    ftxclose = []
    ftxopen = []
    ftxlow = []
    ftxhigh = []
    ftxstarttime = []
    for i in range(len(ff['result'])):
        ftxclose.append(ff['result'][i]['close'])
        ftxopen.append(ff['result'][i]['open'])
        ftxlow.append(ff['result'][i]['low'])
        ftxhigh.append(ff['result'][i]['high'])
        ff['result'][i]['startTime'] = ff['result'][i]['startTime'].replace('T', ' ')
        ftxstarttime.append(dt.datetime.strptime(ff['result'][i]['startTime'][:-6], '%Y-%m-%d %H:%M:%S'))
    df = pd.DataFrame({
        'Close' : ftxclose,
        'Open' : ftxopen,
        'Low' : ftxlow,
        'High' : ftxhigh,
        }, index = ftxstarttime)
    return df
def getftx_for_ema(stock):
    ff = requests.get('https://ftx.com/api/markets/'+stock+'/candles?resolution=86400&limit=280')
    ff = json.loads(ff.text)
    ftxclose = []
    ftxopen = []
    ftxlow = []
    ftxhigh = []
    ftxstarttime = []
    for i in range(len(ff['result'])):
        ftxclose.append(ff['result'][i]['close'])
        ftxopen.append(ff['result'][i]['open'])
        ftxlow.append(ff['result'][i]['low'])
        ftxhigh.append(ff['result'][i]['high'])
        ftxstarttime.append(ff['result'][i]['startTime'][:-15])
    df = pd.DataFrame({
        'Close' : ftxclose,
        'Open' : ftxopen,
        'Low' : ftxlow,
        'High' : ftxhigh,
        }, index = ftxstarttime)
    return df
def discorder(webhook,content):
    a = DiscordWebhook(
    url= webhook,
    content=str(content))
    return a
bub = at2.get_all()
stocks = []
for i in range(len(bub)):
   if bub[i]['fields']['Category'] == 'USA stocks':
      stocks.append(bub[i]['fields']['Name'])
for i in stocks:
    ema = ema_calc(i)
    if 1 in ema:
        long_term_positive.append(i)
    if 2 in ema:
        short_term_positive.append(i)
    if 3 in ema:
        long_term_negative.append(i)
    if 4 in ema:
        short_term_negative.append(i)
for i in long_term_positive:
    bb_drawer_usa(i,True)
    osc_drawer_usa(i, True)
    trap_drawer_usa(i,True)
    inside_drawer_usa(i, True, True)
for i in short_term_positive:
    bb_drawer_usa(i, False)
    osc_drawer_usa(i, False)
    trap_drawer_usa(i,False)
    inside_drawer_usa(i,False, True)
for i in long_term_negative:
    bb_drawer_usa(i,True)
    osc_drawer_usa(i,True)
    trap_drawer_usa(i,True)
    inside_drawer_usa(i, True, False)
for i in short_term_negative:
    bb_drawer_usa(i,False)
    osc_drawer_usa(i,False)
    trap_drawer_usa(i,False)
    inside_drawer_usa(i,False, False)
del (stocks[:])
del (long_term_positive[:])
del (long_term_negative[:])
del (short_term_positive[:])
del (short_term_negative[:])
for i in range(len(bub)):
   if bub[i]['fields']['Category'] == 'BR stocks':
      stocks.append(bub[i]['fields']['Name'])
for i in stocks:
    ema = ema_calc(i)
    if 1 in ema:
        long_term_positive.append(i)
    if 2 in ema:
        short_term_positive.append(i)
    if 3 in ema:
        long_term_negative.append(i)
    if 4 in ema:
        short_term_negative.append(i)
for i in long_term_positive:
    bb_drawer_br(i,True)
    osc_drawer_br(i, True)
    trap_drawer_br(i,True)
    inside_drawer_br(i, True, True)
for i in short_term_positive:
    bb_drawer_br(i, False)
    osc_drawer_br(i, False)
    trap_drawer_br(i,False)
    inside_drawer_br(i,False, True)
for i in long_term_negative:
    bb_drawer_br(i,True)
    osc_drawer_br(i,True)
    trap_drawer_br(i,True)
    inside_drawer_br(i, True, False)
for i in short_term_negative:
    bb_drawer_br(i,False)
    osc_drawer_br(i,False)
    trap_drawer_br(i,False)
    inside_drawer_br(i,False, False)
del (stocks[:])
del (long_term_positive[:])
del (long_term_negative[:])
del (short_term_positive[:])
del (short_term_negative[:])
for i in range(len(bub)):
   if bub[i]['fields']['Category'] == 'Binance':
      stocks.append(bub[i]['fields']['Name'])
for i in stocks:
    ema = ema_calc_binance(i)
    if 1 in ema:
        long_term_positive.append(i)
    if 2 in ema:
        short_term_positive.append(i)
    if 3 in ema:
        long_term_negative.append(i)
    if 4 in ema:
        short_term_negative.append(i)
for i in long_term_positive:
    bb_drawer_binance(i,True)
    osc_drawer_binance(i, True)
    trap_drawer_binance(i,True)
    inside_drawer_binance(i, True, True)
for i in short_term_positive:
    bb_drawer_binance(i, False)
    osc_drawer_binance(i, False)
    trap_drawer_binance(i,False)
    inside_drawer_binance(i,False, True)
for i in long_term_negative:
    bb_drawer_binance(i,True)
    osc_drawer_binance(i,True)
    trap_drawer_binance(i,True)
    inside_drawer_binance(i, True, False)
for i in short_term_negative:
    bb_drawer_binance(i,False)
    osc_drawer_binance(i,False)
    trap_drawer_binance(i,False)
    inside_drawer_binance(i,False, False)
del (stocks[:])
del (long_term_positive[:])
del (long_term_negative[:])
del (short_term_positive[:])
del (short_term_negative[:])
for i in range(len(bub)):
   if bub[i]['fields']['Category'] == 'FTX':
      stocks.append(bub[i]['fields']['Name'])
for i in stocks:
    ema = ema_calc_ftx(i)
    if 1 in ema:
        long_term_positive.append(i)
    if 2 in ema:
        short_term_positive.append(i)
    if 3 in ema:
        long_term_negative.append(i)
    if 4 in ema:
        short_term_negative.append(i)
for i in long_term_positive:
    bb_drawer_ftx(i,True)
    osc_drawer_ftx(i, True)
    trap_drawer_ftx(i,True)
    inside_drawer_ftx(i, True, True)
for i in short_term_positive:
    bb_drawer_ftx(i, False)
    osc_drawer_ftx(i, False)
    trap_drawer_ftx(i,False)
    inside_drawer_ftx(i,False, True)
for i in long_term_negative:
    bb_drawer_ftx(i,True)
    osc_drawer_ftx(i,True)
    trap_drawer_ftx(i,True)
    inside_drawer_ftx(i, True, False)
for i in short_term_negative:
    bb_drawer_ftx(i,False)
    osc_drawer_ftx(i,False)
    trap_drawer_ftx(i,False)
    inside_drawer_ftx(i,False, False)
bub = at.get_all()
for i in range(len(bub)):
    if bub[i]['fields']['Markets'][0].lower() == 'usa_stocks':
        if bub[i]['fields']['Trend'][0].lower() == 'short':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_usa_stoch, bub[i]['fields']['ID'] +'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) + bub[i]['fields']['Graph'] )
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_usa_stoch,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_usa_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_usa_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) )
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_usa_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_usa_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_usa_inside,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_usa_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
        elif bub[i]['fields']['Trend'][0].lower() == 'long':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_usa_stoch,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_usa_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_usa_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_usa_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_usa_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_usa_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_usa_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_usa_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
    elif bub[i]['fields']['Markets'][0].lower() == 'br_stocks':
        if bub[i]['fields']['Trend'][0].lower() == 'short':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_br_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_br_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_br_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_br_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_br_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_br_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_br_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_br_inside,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
        elif bub[i]['fields']['Trend'][0].lower() == 'long':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_br_stoch,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_br_stoch,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_br_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_br_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_br_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_br_trap, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_br_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_br_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
    elif bub[i]['fields']['Markets'][0].lower() == 'binance':
        if bub[i]['fields']['Trend'][0].lower() == 'short':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_binance_stoch,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_binance_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_binance_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_binance_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_binance_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_binance_trap, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_binance_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_binance_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
        elif bub[i]['fields']['Trend'][0].lower() == 'long':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_binance_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_binance_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_binance_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_binance_bb,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_binance_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_binance_trap, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_binance_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_binance_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
    elif bub[i]['fields']['Markets'][0].lower() == 'ftx':
        if bub[i]['fields']['Trend'][0].lower() == 'short':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_ftx_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_ftx_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_ftx_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_ftx_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_ftx_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_ftx_trap, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(short_ftx_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(short_ftx_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
        elif bub[i]['fields']['Trend'][0].lower() == 'long':
            if bub[i]['fields']['Strategies'].lower() == 'stoch':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_ftx_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_ftx_stoch, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']) )
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'bollinger':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_ftx_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
                elif  bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_ftx_bb, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'trap_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_ftx_trap,'['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_ftx_trap, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
            elif bub[i]['fields']['Strategies'].lower() == 'inside_bar':
                if bub[i]['fields']['Sell or Buy'].lower() == 'buy':
                    a = discorder(long_ftx_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Buy - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
                elif bub[i]['fields']['Sell or Buy'].lower() == 'sell':
                    a = discorder(long_ftx_inside, '['+bub[i]['fields']['ID'] +']'+'('+ bub[i]['fields']['Graph']+')'+'- Recommendation : Sell - Entry at : '+ str(bub[i]['fields']['entry']) + '- Close at :' +str(bub[i]['fields']['close']))
                    rofl = a.execute()
                    time.sleep(2)
bub = at.get_all()
for i in range(len(bub)):
   p = bub[i]['id']
   at.delete(str(p))