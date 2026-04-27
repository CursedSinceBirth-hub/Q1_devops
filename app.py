from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']

    users.append([name, email])

    return "<h2>Form Registered Successful</h2><a href='/'>Go Back go back go</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
