from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__, template_folder='app/')
app.static_folder = 'app/static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_data/', methods=['post'])
def new_data():
    userid = request.form.get('userid')
    password = request.form.get('passid')
    name = request.form.get('username')
    address = request.form.get('address')
    country = request.form.get('country')
    zipcode = request.form.get('zip')
    email = request.form.get('email')
    sex = request.form.get('sex')
    language = request.form.get('lang')
    about = request.form.get('desc')

    insert_stmt = (
        "INSERT INTO students (userid, password, "
        "name, address, country, "
        "zipcode, email, sex, language, about) "
        "VALUES (?, ?, ?, ?, "
        "?, ?, ?, ?, ?, ?)"
    )
    data = (userid, password,
            name, address, country,
            zipcode, email, sex,
            language, about)

    conn = sqlite3.connect('data/database.db')
    cur = conn.cursor()

    cur.execute(insert_stmt, data)
    conn.commit()
    print("Did we do it?")
    return jsonify(data)


app.run(debug=True)
conn.close()