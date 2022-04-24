from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)
    return render_template('search.html')

if __name__ == "__main__":
    app.run()
