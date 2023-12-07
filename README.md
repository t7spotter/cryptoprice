₿ 💲

Real-time cryptocurrency price converter:
Get the latest 💲`USD` and `IRR` value of any coin symbol instantly. Stay updated with this code snippet.

Real-time Cryptocurrency Price Converter This is a simple web flask app that retrieves the current 💲`USD` & `IRR` value of a given cryptocurrency symbol and returns it in `JSON` format and real-time. It allows developers and cryptocurrency enthusiasts to obtain up-to-date price data for their applications or projects.

## Usage:

To use the code, follow these steps:

 - Run it with Docker!

 - It will be run on your localhost and port 5000: ```http://localhost:5000```

 - for each coin or token you want to find out the real-time prices, you should add desired coin symbol at the end of the url  (```http://localhost:5000/<coin_symbol>```).

    for example you need to know the real-time ₿itcoin price, you need to input ```http://localhost:5000/btc``` in your web-browser url bar.
    and response will be like this:
   ```
   {
   "coin":"BTC",
   "irr_price":21858576659.034008,
   "usd_price":43211.577857139484
   }
   ```



