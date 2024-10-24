from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    arrival_rate = float(request.form['arrival_rate'])
    service_rate = float(request.form['service_rate'])

    if service_rate == 0:
        error_message = "Service rate cannot be zero. Please enter a valid value."
        return render_template('index.html', error=error_message)

    utilization = arrival_rate / service_rate
    if utilization >= 1:
        error_message = "Utilization rate must be less than 1. Please enter valid values."
        return render_template('index.html', error=error_message)

    avg_num_customers = utilization / (1 - utilization)
    avg_wait_time = avg_num_customers / arrival_rate
    prob_n_customers = lambda n: (1 - utilization) * (utilization ** n)
    
    n = int(request.form['n'])
    probability = prob_n_customers(n)

    return render_template('result.html', utilization=utilization, avg_num_customers=avg_num_customers, avg_wait_time=avg_wait_time, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
