from flask import Flask, render_template, request
from sklearn.metrics import mean_squared_error
import pickle
import math
from dateutil.relativedelta import relativedelta

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    prediction = ""
    minutes = ""
    if request.method == "POST":
        model = pickle.load(open('linear_reg.pkl', 'rb'))
        user_input_feature_1 = request.form.get('size')

        try:
            user_input_feature_1 = float(user_input_feature_1)
            prediction = model.predict([[user_input_feature_1]])[0]
            rt = relativedelta(seconds=math.trunc(prediction))
            minutes = '{:02d}:{:02d}:{:02d}'.format(int(rt.hours), int(rt.minutes), int(rt.seconds))
        except ValueError:
            print("Cannot make a prediction out of a string")

    return render_template('dashboard.html', prediction=minutes)

if __name__ == '__main__':
    app.run(debug=True)
