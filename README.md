# Crypto-Alert
 A code that will return you the price of a specific coin every second and when It reachs a price that you seletected it will make a sound alert!

When you run the py file it basically request you 2 inputs.

symbol_input = input("Crypto Symbol [SLPBUSD - BTCUSDT - ETHBUSD]:")
 It basically is only going to accept Binance cryptocurrency simbols, like in the examples inside the []
 
price_input = float(input("Alert the price when it reach [1245.5$]:"))
 You must setup a price, when the crypto reach the value that you decided, It's going to play an audio alert:
 
mytext = f"{symbol_convertor[0]} reach the alert price of ${symbol_convertor[1]}"
OUTPUT EXAMPLE: SLP reach the alert price of $0.1 - But with a google translator voice, of course.

I have been studying python for less than 1 week and then I enjoyed my first project, and I decided to share cause It's a project that I want to upgrade soon.

Coming Soon:
- GUI, some kind of panel better than a ugly console
- A way to let users input multiple coins and multiple alerts at the same time
