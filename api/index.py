from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = dict()
    # Preformat the data before sending the request to this endpoint
    data['history'] = request.args.get('history')
    data['summary'] = request.args.get('summary')
    data['customer_name'] = request.args.get('customer_name')
    data['customer_id'] = request.args.get('customer_id')
    data['customer_email'] = request.args.get('customer_email')
    data['escalation_reason'] = request.args.get('escalation_reason')
    data['best_solution'] = request.args.get('best_solution')
    data['other_solutions'] = request.args.get('other_solutions')
    return render_template('index.html', data = data)


@app.route('/result')
def result():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('result.html', result = dict)
