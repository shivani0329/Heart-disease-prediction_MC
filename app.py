from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("MODEL_PROJECT.pkl")


@app.route("/", methods=["GET", "POST"])
def predict():

    predicted_result = ""
    prediction_color = ""

    if request.method == "POST":
        try:
            gender = float(request.form["gender"])
            impluse = float(request.form["impluse"])
            pressurehigh = float(request.form["pressurehight"])
            pressurelow = float(request.form["pressurelow"])
            glucose = float(request.form["glucose"])
            kcm = float(request.form["kcm"])
            troponin = float(request.form["troponin"])

            features = np.array([[
                gender,
                impluse,
                pressurehigh,
                pressurelow,
                glucose,
                kcm,
                troponin
            ]])

            prediction = model.predict(features)[0]

            # Change this if your labels are reversed
            if int(prediction) == 1:
                predicted_result = "❤️✅Heart Disease Detected"
                prediction_color = "red"
            else:
                predicted_result = "💚❌ No Heart Disease"
                prediction_color = "green"

        except Exception as e:
            predicted_result = f"Error: {e}"
            prediction_color = "orange"

    return render_template(
        "forms.html",
        predicted_result=predicted_result,
        prediction_color=prediction_color
    )


if __name__ == "__main__":
    app.run(debug=True)
