from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    type = request.form['type']
    amount = float(request.form['amount'])
    old_balance = float(request.form['old_balance'])
    new_balance = float(request.form['new_balance'])
    prediction = model.predict([[type, amount, old_balance, new_balance]])

    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)