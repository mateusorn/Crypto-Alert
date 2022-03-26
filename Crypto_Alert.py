import fileinput
from playsound import playsound
from gtts import gTTS
from time import sleep
import json
import requests
import datetime
import os

symbol_input = input("Crypto Symbol [SLPBUSD - BTCUSDT - ETHBUSD]:")
price_input = float(input("Alert the price when it reach [1245.5$]:"))
key = "https://api.binance.com/api/v3/ticker/price?symbol="+symbol_input


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
    # Edit "BUSD" TO "-BUSD" to look better: "SLPBUSD">"SLP"
    symbol_convertor[0] = symbol_convertor[0].replace("BUSD","").replace("USDT","").replace("USDC","")
    # "0.02110000" > "0.0211"
    symbol_convertor[1] = float(symbol_convertor[1])
    print(f"🔔 [${price_input}] 📈 {time} - {symbol_convertor[0]} ${symbol_convertor[1]}", end="\r")
    sleep(1)
    #if the actual price of a coin is higher or equal than the alert price, do:
    if symbol_convertor[1] >= price_input:
        # The text that you want to convert to audio
        mytext = f"{symbol_convertor[0]} reach the alert price of ${symbol_convertor[1]}"
        # Language in which you want to convert
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=True)
        # Saving the converted audio in a mp3 file named
        # alert 
        myobj.save("alert.mp3")
        # Playing the converted file
        playsound('alert.mp3')
##Code problems: For some reason when the price hits the alert, the code stop working due to problems with the audio file.
    
