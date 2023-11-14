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