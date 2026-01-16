import joblib
from flask import Flask,request,jsonify
import numpy as np
import os
app=Flask(__name__)


model=joblib.load("./model.pkl")  
@app.route("/")
def home():
           return jsonify({"message":"ML model API Running"})

@app.route("/predict",methods=["POST"])   
def predict():
        try:
           data=request.get_json()
           if not data:
                 return jsonify({"error":"No JSON provided"}),400
           hours=data["hours"]
           attendance=data["attendance"]
           if hours is None or attendance is None:
                 return jsonify({"error":"hours and attendance are required"}),400
           features=np.array([[hours,attendance]])
         
           prediction=model.predict(features)
           return jsonify({"prediciton":int(prediction[0])})
        except Exception as e:
              return jsonify({"error":str(e)}),500
if __name__=="__main__":
 app.run(debug=True)

