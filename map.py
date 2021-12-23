from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import urllib.request as urllib
import threading

app = Flask(__name__)
app.config.from_pyfile('config.py')

"""Change to 'dev' or 'prod'"""
ENV = 'prod'

if ENV == 'dev':
    app.logger.info('testing info log')
    app.config.from_object('config.DevConfig')
else:
    app.config.from_object('config.ProdConfig')

app.config.from_object('config.BaseConfig')

db=SQLAlchemy(app)

@app.route('/')

def index():
    return render_template('index.html')

@app.route("/getData", methods=['GET'])
def getData():
    url_series = []
    url_outline = []

    result = db.session.execute(text("select * from user_info"))
    for row in result:
        if not row['url_series'] in url_series and row['url_series'] != '':
            url_series.append(row['url_series'])
        if not row['url_outline'] in url_outline and row['url_outline'] != '':
            url_outline.append(row['url_outline'])

    return jsonify(url_series, url_outline)



if __name__ == '__main__':
    app.run(debug = True)
