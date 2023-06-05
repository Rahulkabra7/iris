from flask import Flask, jsonify, render_template, request

from project_app.utils import Titanic

# Creating instance here
app = Flask(__name__)

# Home API
@app.route("/")
def hello_flask():
    print("Welcome to IRIS Prediction System")
    return render_template("index.html")

# @app.route("/predict_charges")  #postman test
@app.route("/predict_charges", methods = ["POST", "GET"])
def get_predicted_charges():
    if request.method == "GET":
        print("We are in a GET Method")

    Pclass = request.args.get("Pclass")
    Gender = request.args.get("Gender")
    Age = request.args.get("Age")
    SibSp = request.args.get("SibSp")
    Parch = request.args.get("Parch")
    Fare = request.args.get("Fare")
    Embarked = request.args.get("Embarked")


    titanic = Titanic(Pclass, Gender, Age, SibSp, Parch, Fare, Embarked)
    prediction = Titanic.get_predicted_charges(titanic)
    return render_template("index.html", prediction = prediction)
    # print("prediction", prediction)
    # return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."}) #postman test

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters