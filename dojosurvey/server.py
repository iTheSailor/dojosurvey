from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    print(request.form)

    session['your_name'] = request.form['your_name']
    session['dojo'] = request.form['dojo']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")


if __name__=="__main__":
    app.run(debug=True)