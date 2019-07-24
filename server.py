from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder='app/')
app.static_folder = 'app/static'

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)