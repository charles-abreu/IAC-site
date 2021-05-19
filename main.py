from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory
import os, json, sys, datetime, shutil
from glob import glob
import pandas as pd

app = Flask(__name__)
#get_config(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/disciplinas')
def disciplinas():
    return render_template('disciplinas.html.jinja')

@app.route('/professores')
def professores():
    return render_template('professores.html.jinja')

@app.route('/info')
def info():
    return render_template('info.html.jinja')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
