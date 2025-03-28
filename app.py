import json
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def index():
    # return json.dumps({'name': 'alice',
    #                    'email': 'alice@outlook.com'})
    params="7crore"
    return render_template('index.html',params=params)
app.run(debug=True)