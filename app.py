from flask import Flask, jsonify
import requests

from name_to_id import name_to_id

app = Flask(__name__)