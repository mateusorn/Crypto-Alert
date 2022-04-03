import fileinput
from playsound import playsound
import pyttsx3
from time import sleep
import json
import requests
import datetime
import os
from colorama import Fore, Back, Style

symbol_input = input("Crypto Symbol [SLPBUSD - BTCUSDT - ETHBUSD]:").upper()
price_input = float(input("Alert the price when it reach [1245.5$]:"))
key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol_input
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

repeat = 0
while repeat <= 1:
    #Function to capture time of the computer and format it
    time = datetime.datetime.now().strftime("%d/%m/%y [%H:%M:%S]")
    # requesting data from url
    # completing API for request
    data = requests.get(key)  
    data = data.json()
    
    # transforms a dictionary into a list
    symbol_convertor = list(data.values())
    
    if type(symbol_convertor[0]) == int:
        print(Fore.RED + 'You probably inputed the wrong coin Symbol make sure that you are not using special characters or you wrote something wrong.')
        break
    
    # Edit "BUSD" TO "-BUSD" to look better: "SLPBUSD">"SLP"
    symbol_convertor[0] = symbol_convertor[0].replace("BUSD"," ").replace("USDT"," ").replace("USDC"," ")
    # "0.02110000" > "0.0211"
    symbol_convertor[1] = float(symbol_convertor[1])
    print(f"\U0001F514[${price_input}] \U0001F4C9{time} - {symbol_convertor[0]} ${symbol_convertor[1]}", end="\r")
    sleep(0.2)
    if symbol_convertor[1] >= price_input:
        print("\U0001F612")
        # The text that you want to convert to audio
        engine = pyttsx3.init()
        engine.setProperty('voice', en_voice_id)
        engine.say(f"{symbol_convertor[0]} reach the alert price of ${symbol_convertor[1]}")
        engine.setProperty('rate', 110)    # Speed percent (can go over 100)
        engine.runAndWait()
        sleep(10)
    elif symbol_convertor[1] == price_input:
        print(Fore.RED + f"The currency {symbol_convertor[0]} already hit this price!")
