from __future__ import unicode_literals
import json
import requests
import pandas as pd

from flask import Flask, request, Response, render_template, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def scrape():

    params = {
        'spider_name': 'quotescraper',
        'start_requests': True,
     
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    return data
       
if __name__ == '__main__':
    app.run(debug=True, port=1234)