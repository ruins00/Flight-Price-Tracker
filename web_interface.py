from flask import Flask, render_template, redirect, send_file
from selenium1 import check
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

headings = ['Index', 'Date', 'Time', 'Price']

def get_rec_details():
    recs = list()
    with open('./prices.txt', 'r', encoding="utf-8") as rec_file:
        records = rec_file.readlines()
        [recs.append(record.split('|')) for record in records]
    return recs

@app.route('/recs')
def recs():
    try:
        return render_template('index.html', title='Flight Price Records', med_status='active', headings=headings, data=get_rec_details())
    except FileNotFoundError as e:
        file = open("./prices.txt","w")
        file.close()
        return redirect('/recs')


@app.route('/css', methods=['GET'])
def bootstrap_css():
    filename = './assets/css/bootstrap.min.css'
    return send_file(filename)

@app.errorhandler(404)
def error_route(err):
    return redirect('/recs')

@app.route('/check_now')
def check_now():
    try:
        check()
    except NoSuchElementException as e:
        return render_template('network_error.html')
    return redirect('/recs')

@app.route('/img_view')
def img_view():
    return render_template('img_viewer.html')


app.run('0.0.0.0', 3000, debug=True)

