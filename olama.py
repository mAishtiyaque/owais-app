from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#@app.route('/about_us/')
#def about_us():
#    return render_template('about_us.html')

app.run(debug=True)