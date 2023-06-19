from flask import Flask
import json
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/getRate', methods=['GET'])
def getRate():
    res = requests.get("https://www.lira-rate.com/lbprate.php")
    parsed_html = BeautifulSoup(res.text,"html.parser")
    return json.dumps({"rate":parsed_html(text=re.compile(r'.*LL$'))[0]})


if __name__ == "__main__":
    app.run()