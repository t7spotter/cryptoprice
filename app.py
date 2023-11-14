from flask import Flask, jsonify
import requests

from name_to_id import name_to_id

app = Flask(__name__)

@app.route("/<sym>")
def main(sym):
    
    def captalize(a):
        if a.islower():
            return a.upper()
        else:
            return a
        
    
    coin_symbol = captalize(sym)
    
    if coin_symbol in name_to_id:
        coin_id = name_to_id[f'{coin_symbol}'] 
    else:
        return jsonify(message="Enter the valid coin symbol")
    
    r = requests.get(f'https://cryptobubbles.net/backend/data/charts/hour/{coin_id}/USD.json')
    response_json = r.json()
    last_price = (response_json[-1])['p']