from flask import Flask, render_template, request
from src.calculator import Calculator
print(1)
print(2)
cal = Calculator()
app = Flask(__name__)
print(3)


@app.route("/", methods=["GET", "POST"])
def index():
    result = 0
    print(4)
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operator = request.form["operator"]
        print(5)
        if operator == "+":
            result = cal.add(num1, num2)
        elif operator == "-":
            result = cal.substract(num1, num2)
        elif operator == "*":
            result = cal.multiply(num1, num2)
        else:
            result = cal.divide(num1, num2)
        print(6)
    return render_template("index.html", result=int(result))


print(7)


@app.route("/health")
def health():
    return "I am healthy"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
