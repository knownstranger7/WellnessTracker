from flask import Flask
from flask_restful import Resource, Api, reqparse
import random

app= Flask(__name__)
api=Api(app)

MedRecN = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5, 37.5), 1)),
    "Blood Pressure":random.randint(80,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(60,100),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(95,100),
}

Diabetes = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5,37.5),1)),
    "Blood Pressure":random.randint(80,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(200,350),
    "Heart Rate":random.randint(60,100),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(95,100)
    
}

Prediabetes = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5,37.5),1)),
    "Blood Pressure":random.randint(80,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(140,199),
    "Heart Rate":random.randint(60,100),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(95,100)
    
}

Bronchiectasis = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5, 37.5), 1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(40,60),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(60,100),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(95,100),
}

CongenitalHeartDefect = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5, 37.5), 1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(45,60),
    "Cholesterol":random.randint(200,270),
    "Oxygen Saturation":random.randint(95,100),
}

Hypoxemia = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5, 37.5), 1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(12,16),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(60,100),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(50,96),
}

AcuteAsthma = {
    "Steps":random.randint(4000, 10000),
    "Body Temperature":(round(random.uniform(35.5, 37.5), 1)),
    "Blood Pressure":random.randint(90,120),
    "Respiration":random.randint(20,30),
    "Glucose":random.randint(72,140),
    "Heart Rate":random.randint(100,125),
    "Cholesterol":random.randint(125,200),
    "Oxygen Saturation":random.randint(92,95),
}

parser=reqparse.RequestParser()

class MedicalData(Resource):
    def post(self):
        parser.add_argument("state")
        args = parser.parse_args()
        _state=args["state"]
        diseases = {'A': AcuteAsthma, 'B': Bronchiectasis,'C':CongenitalHeartDefect,'D':Diabetes,'H':Hypoxemia,'N':MedRecN,'P':Prediabetes}
        return diseases.get(_state, 'default')
    
 
api.add_resource(MedicalData,'/medidata/')

if __name__ == "__main__":    
    app.run()