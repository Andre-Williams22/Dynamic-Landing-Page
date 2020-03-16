from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        number = request.form['number']

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)