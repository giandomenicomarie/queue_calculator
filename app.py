from flask import Flask, request, render_template
from queue_calculator import mm1_queue

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    lmbda = float(request.form['arrival_rate'])
    mu = float(request.form['service_rate'])
    results = mm1_queue(lmbda, mu)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True
