from flask import Flask, jsonify, request
from server.controller.income_controller import incomeController;

app = Flask(__name__)

@app.route("/income_list", methods=['GET'])
def get_income_list():
    income_controller = incomeController()
    incomes = income_controller.getIncomesList()
    response = jsonify(incomes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

@app.route("/income_list", methods=["POST"])
def add_new_income():
    income_controller = incomeController()
    response = jsonify(request)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)