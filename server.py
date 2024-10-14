from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
    if 'back_color' in session:
        back_color = session['back_color']
    else:
        back_color = "#FFF"
    if 'text_color' in session:
        text_color = session['text_color']
    else:
        text_color = "#000"
    return render_template('index.html', back_color=back_color, text_color=text_color)

@app.route('/red_back')
def red_back():
    session['back_color'] = '#F00'
    return redirect('/')

@app.route('/blue_back')
def blue_back():
    session['back_color'] = '#00F'
    return redirect('/')

@app.route('/green_back')
def green_back():
    session['back_color'] = '#0F0'
    return redirect('/')

@app.route('/default_back')
def default_back():
    del session['back_color']
    return redirect('/')

@app.route('/red_text')
def red_text():
    session['text_color'] = '#F00'
    return redirect('/')

@app.route('/blue_text')
def blue_text():
    session['text_color'] = '#00F'
    return redirect('/')

@app.route('/green_text')
def green_text():
    session['text_color'] = '#0F0'
    return redirect('/')

@app.route('/default_text')
def default_text():
    del session['text_color']
    return redirect('/')

app.run(debug=True)