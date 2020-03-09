from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success', methods=['GET','POST'])
def success():
    return render_template('success.html')

@app.route('/bankingone.html', methods=['GET','POST'])
def bankingone():
    return render_template('bankingone.html')

@app.route('/bankingtwo.html', methods=['GET','POST'])
def bankingtwo():
    return render_template('bankingtwo.html')

@app.route('/bankingthree.html', methods=['GET','POST'])
def bankingthree():
    return render_template('bankingthree.html')

@app.route('/bankingfour.html', methods=['GET','POST'])
def bankingfour():
    return render_template('bankingfour.html')

@app.route('/bankingfive.html', methods=['GET','POST'])
def bankingfive():
    return render_template('bankingfive.html')

@app.route('/bankingsix.html', methods=['GET','POST'])
def bankingsix():
    return render_template('bankingsix.html')

@app.route('/bankingseven.html', methods=['GET','POST'])
def bankingseven():
    return render_template('bankingseven.html')

@app.route('/bankingeight.html', methods=['GET','POST'])
def bankingeight():
    return render_template('bankingeight.html')

@app.route('/bankingnine.html', methods=['GET','POST'])
def bankingnine():
    return render_template('bankingnine.html')

@app.route('/bankingten.html', methods=['GET','POST'])
def bankingten():
    return render_template('bankingten.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin@admin.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('success.html', error=error)

if __name__ == "__main__":
        app.run(debug=True)