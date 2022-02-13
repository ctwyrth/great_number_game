from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'All 4 one, 1 FOR all'

import random

@app.route('/')
def index():
    if 'secret_number' in session:
        if session['did_win'] == True:
            x = session['guess_count'] + 1
            y = session['secret_number']
            session.clear()
            return render_template('index.html', winner = True, count = x, number = y)
        else:
            pass
    else:
        session['secret_number'] = random.randint(1, 100)
        session['guess_count'] = 0
        session['did_win'] = False
    return render_template('index.html', winner = session['did_win'])

@app.route('/guess', methods= ['POST'])
def guess_number():
    guess = int(request.form['guess'])
    if guess == session['secret_number']:
        session['did_win'] = True
        return redirect('/')
    else:
        session['guess_count'] += 1
        if session['guess_count'] == 5:
            x = session['secret_number']
            session.clear()
            return render_template('index.html', number = x, failure = True)
        if guess > session['secret_number']:
            session['vary'] = 'too high'
        else:
            session['vary'] = 'too low'
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
