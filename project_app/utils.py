import pandas as pd
import numpy as np
import pickle
import json
import warnings
warnings.filterwarnings('ignore')
import os
import config

class Titanic():
    def __init__(self, Pclass, Gender, Age, SibSp, Parch, Fare, Embarked):

        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        self.Embarked = Embarked

    def load_models(self):
        with open('project_app\Logistic model.pkl','rb') as f:
            self.logistic_model = pickle.load(f)

        with open('project_app\project_data.json', 'r')as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_models()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array

        test_array[0] = self.Pclass
        # test_array[1] = self.json_data['Gender'][self.Gender]
        test_array[1] = self.json_data['Gender'][self.Gender]
        test_array[2] = self.Age
        test_array[3] = self.SibSp
        test_array[4] = self.Parch
        test_array[5] = self.Fare
        test_array[6] = self.json_data['Embarked'][self.Embarked]

        # prediction = self.logistic_model.predict([test_array])
        charges=round(self.logistic_model.predict([test_array])[0],2)
        if charges==1:
            return "Survieved"
        else:
            return "Not Survieved"


if __name__ == "__main__":
    Pclass = 3.00
    Gender = "male"
    Age = 25.00
    SibSp = 0.00
    Parch = 0.00
    Fare = 7.25
    Embarked = "S"

    titanic = Titanic(Pclass, Gender, Age, SibSp, Parch, Fare, Embarked)
    prediction = irTitanicis.get_predicted_charges([titanic])
    print("prediction", prediction)