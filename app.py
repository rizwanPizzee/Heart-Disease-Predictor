from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

features = [
    "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol",
    "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        data = {}
        for feat in features:
            val = request.form.get(feat)
            if val is None:
                return render_template('index.html', prediction_text="Error: missing form field "+feat)
            
            if feat in ["Age", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "Oldpeak"]:
                if feat == "Oldpeak":
                    data[feat] = float(val)
                elif feat == "FastingBS":
                    data[feat] = int(val)
                else:
                    if "." in val:
                        data[feat] = float(val)
                    else:
                        data[feat] = int(val)
            else:
                data[feat] = val

        input_df = pd.DataFrame([data], columns=features)

        prediction = model.predict(input_df)
        pred = int(prediction[0])

        if pred == 1:
            text = "Prediction: Heart Disease"
        else:
            text = "Prediction: Heart Normal"

        return render_template('index.html', prediction_text=text)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error during prediction: {e}")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
