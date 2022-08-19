import imp
from django.shortcuts import render
import pandas as pd
import numpy as np
from joblib import load

clf = load("Notebooks/lr_model.joblib")
def index(req):
    return render(req,'index.html')

def result(pred):
    data = predict(pred)
    return render(pred,'result.html', {'data':data})

def predict(req):
    age = req.POST['age']
    sex = req.POST['sex']
    cp = req.POST['cp']
    trestbps = req.POST['trestbps']
    chol = req.POST['chol']
    fbs = req.POST['fbs']
    thalach = req.POST['thalach']
    exang = req.POST['exang']
    thal = req.POST['thal']
    X=[[age, sex, cp, trestbps, chol, fbs, thalach, exang, thal]]
    X=np.array(X).reshape(1, 9)
    X=np.array(X, dtype=float)
    y_pred=clf.predict(X).tolist()
    ans=y_pred[0]
    return ans
