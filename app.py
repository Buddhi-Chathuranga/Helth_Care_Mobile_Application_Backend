import random

from flask import Flask, request, jsonify

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pickle

app = Flask(__name__)


cred = credentials.Certificate('health-band-cb631-firebase-adminsdk-gw4q7-1a59724dd3.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://health-band-cb631-default-rtdb.firebaseio.com/'})

@app.route('/prediction', methods=['GET', 'POST'])
def diabetes_prediction():

    highBP = db.reference('prediction_input/HighBP')
    highChol = db.reference('prediction_input/HighChol')
    bmi = db.reference('prediction_input/BMI')
    smoker = db.reference('prediction_input/Smoker')
    heartDiseaseorArrack = db.reference('prediction_input/HeartDiseaseorArrack')
    fruits = db.reference('prediction_input/Fruits')
    age = db.reference('prediction_input/Age')
    veggies = db.reference('prediction_input/Veggies')
    gender = db.reference('prediction_input/Gender')

    if gender == "Male":
        gen = 1
    else:
        gen = 0

    if (18 <= int(age.get()) <= 24):
        F_Age = 1
    elif (25 <= int(age.get()) <= 29):
        F_Age = 2
    elif (30 <= int(age.get()) <= 34):
        F_Age = 3
    elif (35 <= int(age.get()) <= 39):
        F_Age = 4
    elif (40 <= int(age.get()) <= 44):
        F_Age = 5
    elif (45 <= int(age.get()) <= 49):
        F_Age = 6
    elif (50 <= int(age.get()) <= 54):
        F_Age = 7
    elif (55 <= int(age.get()) <= 59):
        F_Age = 8
    elif (60 <= int(age.get()) <= 64):
        F_Age = 9
    elif (65 <= int(age.get()) <= 69):
        F_Age = 10
    elif (70 <= int(age.get()) <= 74):
        F_Age = 11
    elif (75 <= int(age.get()) <= 79):
        F_Age = 12
    elif (int(age.get()) >= 80):
        F_Age = 13

    loaded_model_diabetes = pickle.load(open('Diabetes.pickle', 'rb'))

    predicted_value_diabetes = int(loaded_model_diabetes.predict([[
        int(highBP.get()),
        int(highChol.get()),
        int(bmi.get()),
        int(smoker.get()),
        int(heartDiseaseorArrack.get()),
        int(fruits.get()),
        int(veggies.get()),
        int(gen),
        int(F_Age)]]))


    if predicted_value_diabetes == 0:
        return_value_diabetes = "low"
    elif predicted_value_diabetes == 1:
        return_value_diabetes = "medium"
    elif predicted_value_diabetes == 2:
        return_value_diabetes = "high"

    update_ref_diabetes = db.reference('/')
    update_ref_diabetes.update({'diabetic_prediction': return_value_diabetes})

    # return jsonify(
    #     status_code=200,
    #     msg="Successfully Updated Firebase",
    #     data={
    #         'predicted_value': return_value_diabetes,
    #         'original_value': predicted_value_diabetes
    #     }
    # )

# @app.route('/stress_prediction', methods=['GET', 'POST'])
# def stress_prediction():

    humidity = db.reference('prediction_input/Humidity')
    temp = db.reference('prediction_input/Temp')
    step_count = db.reference('prediction_input/StepCount')
    body_temp = db.reference('prediction_input/body_temp')

    loaded_model_stress = pickle.load(open('Stress.pickle', 'rb'))


    predicted_value_stress = int(loaded_model_stress.predict([[
        int(humidity.get()),
        int(body_temp.get()),
        int(step_count.get())]]))

    if predicted_value_stress == 0:
        return_value_stress = "low"
    elif predicted_value_stress == 1:
        return_value_stress = "normal"
    elif predicted_value_stress == 2:
        return_value_stress = "high"

    update_ref = db.reference('/')
    update_ref.update({'stress_prediction': return_value_stress})

    # return jsonify(
    #     status_code=200,
    #     msg="Successfully Updated Firebase",
    #     data={
    #         'predicted_value': return_value_stress,
    #         'original_value': predicted_value_stress
    #     }
    # )

# @app.route('/bodyperformance_prediction', methods=['GET','POST'])
# def bodyperformance_prediction():

    age = db.reference('prediction_input/Age')
    gender = db.reference('prediction_input/Gender')
    height = db.reference('prediction_input/Hight_cm')
    weight = db.reference('prediction_input/Weight_kg')
    sit_and_bend = db.reference('prediction_input/SitandBend')
    situp_count = db.reference('prediction_input/Situps')

    if gender == "Male":
        gen = 1
    else:
        gen = 0

    loaded_model_bodyPerformance = pickle.load(open('BodyPerformance.pickle', 'rb'))


    predicted_value_bodyPerformance = int(loaded_model_bodyPerformance.predict([[
        int(age.get()),
        int(gen),
        int(height.get()),
        int(weight.get()),
        int(sit_and_bend.get()),
        int(situp_count.get())]]))

    if predicted_value_bodyPerformance == 0:
        return_value_bodyPerformance = "worst"
    elif predicted_value_bodyPerformance ==1:
        return_value_bodyPerformance = "normal"
    elif predicted_value_bodyPerformance == 2:
        return_value_bodyPerformance = "best"

    update_ref = db.reference('/')
    update_ref.update({'bodyperformance_prediction': return_value_bodyPerformance})

    # return jsonify(
    #     status_code=200,
    #     msg="Successfully Updated Firebase",
    #     data={
    #         'predicted_value': return_value_bodyPerformance,
    #         'original_value': predicted_value_bodyPerformance
    #     }
    # )

# @app.route('/heartrate_prediction', methods=['GET', 'POST'])
# def heartrate_prediction():

    gender = db.reference('prediction_input/Gender')
    age = db.reference('prediction_input/Age')
    smoker = db.reference('prediction_input/Smoker')
    bmi = db.reference('prediction_input/BMI')
    heartrate = db.reference('prediction_input/Heartrate')
    highChol = db.reference('prediction_input/HighChol')

    loaded_model_heart = pickle.load(open('Heart.pickle', 'rb'))

    if gender == "Male":
        gen = 1
    else:
        gen = 0


    predicted_value_heart = int(loaded_model_heart.predict([[
        int(gen),
        int(age.get()),
        int(smoker.get()),
        int(highChol.get()),
        int(bmi.get()),
        int(heartrate.get())]]))

    if predicted_value_heart == 0:
        return_value_heart = "low"
    elif predicted_value_heart == 1:
        return_value_heart = "high"

    update_ref_heart = db.reference('/')
    update_ref_heart.update({'heartrate_prediction': return_value_heart})

    # return jsonify(
    #     status_code=200,
    #     msg="Successfully Updated Firebase",
    #     data={
    #         'original_value': return_value_heart
    #     }
    # )

# @app.route('/calories_prediction', methods=['GET', 'POST'])
# def calories_prediction():

    workout_type = db.reference('prediction_input/WorkoutType')
    workout_time = db.reference('prediction_input/WorkoutTime')
    heart_rate = db.reference('prediction_input/Spo2')
    body_temp = db.reference('prediction_input/body_temp')
    temp = db.reference('prediction_input/Temp')
    gender = db.reference('prediction_input/Gender')
    age = db.reference('prediction_input/Age')
    height = db.reference('prediction_input/Hight_cm')
    weight = db.reference('prediction_input/Weight_kg')

    if gender == "Male":
        gen = 1
    else:
        gen = 0

    loaded_model_calories = pickle.load(open('Calories.pickle', 'rb'))

    predicted_value_calories = int(loaded_model_calories.predict([[
        int(gen),
        int(age.get()),
        int(height.get()),
        int(weight.get()),
        int(workout_time.get()),
        int(heart_rate.get()),
        int(body_temp.get())]]))
    update_ref_calories = db.reference('/')
    update_ref_calories.update({'calories_prediction': predicted_value_calories})

    return jsonify(
        status_code=200,
        msg="Successfully Updated Firebase",
        data={
            'predicted_value_heart':str(predicted_value_heart),
            'predicted_value_diabetes':str(predicted_value_diabetes),
            'predicted_value_bodyPerformance':str(predicted_value_bodyPerformance),
            'predicted_value_stress':str(predicted_value_stress),
            'predicted_value_calories': str(predicted_value_calories),
        }
    )

@app.route('/')
def hello():
    return "Welcome..."
