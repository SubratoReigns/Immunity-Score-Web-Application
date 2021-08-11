
from django.shortcuts import render, HttpResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pandas.plotting import scatter_matrix


def modelhome(request):
    return render(request, 'model/model.html')

def ddisease(request):
    return render(request, 'model/diabetes.html')

def dform(request):
    return render(request, 'model/diabetesf.html')

def result2(request):

    diabetes=pd.read_csv(r'C:\Users\User\Downloads\diabetes.csv')
    # In[62]:
    diabetes_train_set, diabetes_test_set=train_test_split(diabetes, test_size=0.2,random_state=42)
    diabetes_train_set["Outcome"].value_counts()
    diabetes_test_set["Outcome"].value_counts()
    """
    corr_matrix=diabetes.corr()
    corr_matrix["Insulin"].sort_values(ascending=False)
    attributes=["Insulin","SkinThickness","Glucose","BMI","DiabetesPedigreeFunction","Outcome","BloodPressure","Age","Pregnancies"]
    scatter_matrix(diabetes[attributes], figsize=(12,8))
    diabetes.plot(kind="scatter",x="Age",y="BMI",alpha=0.80)
    diabetes["BMIa"]=diabetes["BMI"]/diabetes["Age"]
    corr_matrix=diabetes.corr()
    corr_matrix["DiabetesPedigreeFunction"].sort_values(ascending=False)
    """
    
    diabetes_train_set_label=np.asarray(diabetes_train_set["Outcome"])
    diabetes_train_set=np.asarray(diabetes_train_set.drop("Outcome",1))
    diabetes_test_set=np.asarray(diabetes_test_set.drop("Outcome",1))
    diabetes_train_set_label
    diabetescheck=LogisticRegression(solver='lbfgs', max_iter=1000)
    diabetescheck.fit(diabetes_train_set,diabetes_train_set_label)
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    pred = diabetescheck.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    result1 = ""
    if pred==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"
    return render(request, 'model/diabetesf.html', {"result2":result1})