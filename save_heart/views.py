"""views.py"""
import numpy as np
from django.shortcuts import render
from joblib import load

clf = load("Notebooks/dt_model.joblib")


def index(req):
    """View function for home page of site."""
    return render(req, "index.html")


def result(pred):
    """View function for result page of site."""
    data = predict(pred)
    return render(pred, "result.html", {"data": data})


def predict(req):
    """View function for prediction page of site."""
    age = req.POST["age"]
    sex = req.POST["sex"]
    cp_ = req.POST["cp"]
    trestbps = req.POST["trestbps"]
    chol = req.POST["chol"]
    fbs = req.POST["fbs"]
    thalach = req.POST["thalach"]
    exang = req.POST["exang"]
    thal = req.POST["thal"]
    x_test = [[age, sex, cp_, trestbps, chol, fbs, thalach, exang, thal]]
    x_test = np.array(x_test).reshape(1, 9)
    x_test = np.array(x_test, dtype=float)
    y_pred = clf.predict(x_test).tolist()
    ans = y_pred[0]
    return ans
