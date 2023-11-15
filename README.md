₿ 💲

Real-time cryptocurrency price converter:
Get the latest 💲`USD` and `IRR` value of any coin symbol instantly. Stay updated with this code snippet.

Real-time Cryptocurrency Price Converter This is a simple web flask app that retrieves the current 💲`USD` & `IRR` value of a given cryptocurrency symbol and returns it in `JSON` format and real-time. It allows developers and cryptocurrency enthusiasts to obtain up-to-date price data for their applications or projects.

Usage:

To use the code, follow these steps:

1. clone this repo to your local machine:
   ```git clone https://github.com/t7spotter/cryptoprice.git```

2. Install the required dependencies:
   ```pip install -r requirements.txt```

3. Run the flask app:
   ```flask --debug -A app run```

It will be run on your localhost and port 5000: ```http://localhost:5000```

for each coin or token you want to find out the real-time prices, you should add desired coin symbol at the end of the url  (```http://localhost:5000/<coin_symbol>```).

for example you need to know the real-time ₿itcoin price, you need to input ```http://localhost:5000/btc``` in your web-browser url bar.
