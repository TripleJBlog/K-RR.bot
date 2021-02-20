import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import csv
import pandas as pd

f_path = "~/Documents/PriceLogger/price_list.csv"
last_row = pd.read_csv(f_path).iloc[-1]
oil_price = "{:,}".format(int(last_row[1]))
ore_price = "{:,}".format(int(last_row[2]))
uranium_price = "{:,}".format(int(last_row[3]))
diamonds_price = "{:,}".format(int(last_row[4]))
helium_price = "{:,}".format(int(last_row[5]))
rivalium_price = "{:,}".format(int(last_row[6]))
tanks_price = "{:,}".format(int(last_row[7]))
aircrafts_price = "{:,}".format(int(last_row[8]))
missiles_price = "{:,}".format(int(last_row[9]))
bombers_price = "{:,}".format(int(last_row[10]))
drones_price = "{:,}".format(int(last_row[11]))

now = datetime.now()


def price(item):
    global now
    global last_row

    if datetime.now() > now + timedelta(minutes=10):
        last_row = pd.read_csv(f_path).iloc[-1]
        oil_price = "{:,}".format(int(last_row[1]))
        ore_price = "{:,}".format(int(last_row[2]))
        uranium_price = "{:,}".format(int(last_row[3]))
        diamonds_price = "{:,}".format(int(last_row[4]))
        helium_price = "{:,}".format(int(last_row[5]))
        rivalium_price = "{:,}".format(int(last_row[6]))
        tanks_price = "{:,}".format(int(last_row[7]))
        aircrafts_price = "{:,}".format(int(last_row[8]))
        missiles_price = "{:,}".format(int(last_row[9]))
        bombers_price = "{:,}".format(int(last_row[10]))
        drones_price = "{:,}".format(int(last_row[11]))
        now = datetime.now()

    m = f"현재 시각 {last_row[0]}\n"
    if item == "oil":
        m = m + f"{int(last_row[1]):,}"
    elif item == "ore":
        m = m + "{:,}".format(int(last_row[2]))

    return message


app = commands.Bot(command_prefix='!')


@app.event
async def on_ready():
    print(f'다음으로 로그인합니다: {app.user.name}')
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')


@app.command()
async def 가격(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[
        0] + " 자원 시세\n석유: " + oil_price + "\n광물: " + ore_price + "\n우라늄: " + uranium_price + "\n다이아몬드: " + diamonds_price + "\n헬륨: " + helium_price + "\n라이발륨: " + rivalium_price + "\n탱크: " + tanks_price + "\n전투기: " + aircrafts_price + "\n미사일:" + missiles_price + "\n폭격기: " + bombers_price + "\n드론: " + drones_price)


@app.command()
async def 석유(ctx):
    m = price("oil")
    await ctx.send(m)


@app.command()
async def 광물(ctx):
    await ctx.send(price("ore"))


@app.command()
async def 우라늄(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + uranium_price)


@app.command()
async def 다이아몬드(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + diamonds_price)


@app.command()
async def 헬륨(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + helium_price)


@app.command()
async def 라이발륨(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + rivalium_price)


@app.command()
async def 탱크(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + tanks_price)


@app.command()
async def 전투기(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + aircrafts_price)


@app.command()
async def 미사일(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + missiles_price)


@app.command()
async def 폭격기(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + bombers_price)


@app.command()
async def 드론(ctx):
    price()
    await ctx.send("현재 시각 " + last_row[0] + "\n" + drones_price)


@app.command()
async def 도움말(ctx):
    await ctx.send(
        "RR 실시간 자원 시세 알리미 봇무장관은 석유님의 데이터베이스를 기반으로 하여 10분마다 자동 업데이트 되지만 서버 사정으로 업데이트가 지연될 수 있으니 양해바랍니다.\n불편하신 점이나 개선 사항은 석유님에게 DM바랍니다.\n명령어 모음: \n!가격: 전체 실시간 RR 인게임 자원 시세를 확인합니다.\n!석유:석유의 실시간 시세를 확인합니다.\n!광물: 광물의 실시간 시세를 확인합니다.\n!우라늄:우라늄의 실시간 시세를 확인합니다.\n!다이아몬드: 다이아몬드의 실시간 시세를 확인합니다.\n!헬륨: 헬륨의 실시간 시세를 확인합니다.\n!라이발륨:라이발륨의 실시간 시세를 확인합니다.\n!탱크: 탱크의 실시간 시세를 확인합니다.\n!전투기: 전투기의 실시간 시세를 확인합니다.\n미사일: 미사일의 실시간 시세를 확인합니다.\n!폭격기: 폭격기의 실시간 시세를 확인합니다.\n!드론: 드론의 실시간 시세를 확인합니다.\nMade By. RR 한국과학기술원")


file = open('../token.txt', 'r')
token = file.read()
app.run(token)
