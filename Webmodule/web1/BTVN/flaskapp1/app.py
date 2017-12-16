from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<int:wei>/<int:hei>')
def bmi(wei,hei):
    bmi = wei/((hei/100)**2)
    print("your BMI: ", str(bmi))
    if bmi < 16:
        return "you are severely underweight"
    elif bmi < 18:
        return "you are underweight"
    elif bmi < 25:
        return "you are normal"
    elif bmi < 30:
        return "you are overweight"
    else:
        return "you are obese"


if __name__ == '__main__':
  app.run(debug=True)
