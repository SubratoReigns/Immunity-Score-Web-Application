
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from models.models import Patient,DiabetesPatient
from django.contrib import messages
from django.contrib.auth.models import User
from models.forms import PatientRegistration,PatientRegistration1

@login_required(login_url="/")
def modelhome(request):
    return render(request, 'models/model.html')

@login_required(login_url="/")
def ddisease(request):
    return render(request, 'models/diabetes.html')

@login_required(login_url="/")
def dform(request):
    fm = PatientRegistration1()
    pat_info1 = Patient.objects.all()
    return render(request, 'models/diabetesf.html', {'form':fm, 'pat_info1':pat_info1,})

@login_required(login_url="/")
def hform(request):
    return render(request, 'models/heartf.html')
@login_required(login_url="/")
def hform1(request):
    fm = PatientRegistration()
    pat_info = Patient.objects.all()
    return render(request, 'models/heartf1.html', {'form':fm, 'pat_info':pat_info,})

def result3(request):
    heart=pd.read_csv(r'C:\Users\User\Desktop\Project_1\heart_failure_clinical_records_dataset.csv')
    heart_train_set, heart_test_set=train_test_split(heart,test_size=0.3,random_state=42)
    # print(f"{len(heart_train_set)}\n{len(heart_test_set)}")
    heart_train_set_label=np.asarray(heart_train_set['DEATH_EVENT'])
    heart_train_set=np.asarray(heart_train_set.drop('DEATH_EVENT',1))
    heartcheck=LogisticRegression()
    heartcheck.fit(heart_train_set, heart_train_set_label)
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    val9 = float(request.GET['n9'])
    val10 = float(request.GET['n10'])
    val11 = float(request.GET['n11'])
    val12 = float(request.GET['n12'])
    
    pred_1=heartcheck.predict([[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12]])
    
    result2=""
    if pred_1==[1]:
        result2="positive"
    else:
        result2="negative"
    
    user = request.user
    heart_result = result2
    immunity_status = "crictical"
    result_store = Patient(user=user, Heart_Result=heart_result, Immunity_Status=immunity_status)
    result_store.save()
    return render(request,'models/heartf.html',{"result3":result2})



def result2(request):
    if(request.method == 'POST'):
        fm = PatientRegistration1(request.POST)
        if fm.is_valid():
            diabetes=pd.read_csv(r'C:\Users\User\Desktop\Project_res\diabetes.csv')
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
            val1 = float(fm.cleaned_data['preg'])
            val2 = float(fm.cleaned_data['gluc'])
            val3 = float(fm.cleaned_data['bp'])
            val4 = float(fm.cleaned_data['skinthick'])
            val5 = float(fm.cleaned_data['insul'])
            val6 = float(fm.cleaned_data['bmi'])
            val7 = float(fm.cleaned_data['diabpedfun'])
            val8 = float(fm.cleaned_data['age'])
        
            pred = diabetescheck.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
            result1 = ""
            if pred==[1]:
                result1 = "Positive"
            else:
                result1 = "Negative"

            user = request.user
            diabetes_result = result1
            immunity_status = ""

            total = (float)((val8 + val3 + val6)/3.0)

            if(total > 69.63):
                immunity_status="High Risk"
            elif(total > 52.23 and total <= 69.63):
                immunity_status="Moderate"
            elif(total > 50.56 and total <= 52.23):
                immunity_status="Low"
            elif(total <= 50.56 and total >= 38.83):
                immunity_status="Minimal"
            
            total = 100.0 - total

            result_store = DiabetesPatient(user=user, preg=val1, gluc=val2,bp=val3,skinthick=val4,insul=val5,bmi=val6,diabpedfun=val7, age=val8,Diabetes_Result=diabetes_result,Immunity_Status=immunity_status)
            result_store.save()
            fm = PatientRegistration1()
            return render(request, 'models/diabetesf.html', {'form': fm,"result3":result1,"Immunity_Score":total, })

    else:
        fm = PatientRegistration1()
        return render(request, 'models/diabetesf.html', {'form': fm,})

        

    


def result4(request):
    if request.method == 'POST':

        """ 
        pi = User.objects.get(pk=id)
        fm = PatientRegistration(request.POST, instance=pi)
        """
        fm = PatientRegistration(request.POST)
        
        if fm.is_valid():
            heart=pd.read_csv(r'C:\Users\User\Desktop\Project_res\heart_failure_clinical_records_dataset.csv')
            heart_train_set, heart_test_set=train_test_split(heart,test_size=0.3,random_state=42)
            print(f"{len(heart_train_set)}\n{len(heart_test_set)}")
            heart_train_set_label=np.asarray(heart_train_set['DEATH_EVENT'])
            heart_train_set=np.asarray(heart_train_set.drop('DEATH_EVENT',1))
            heartcheck=LogisticRegression()
            heartcheck.fit(heart_train_set, heart_train_set_label)
            val1 = float(fm.cleaned_data['age'])
            val2 = float(fm.cleaned_data['anaemia'])
            val3 = float(fm.cleaned_data['crePhos'])
            val4 = float(fm.cleaned_data['diab'])
            val5 = float(fm.cleaned_data['ejecFrac'])
            val6 = float(fm.cleaned_data['highbp'])
            val7 = float(fm.cleaned_data['platecount'])
            val8 = float(fm.cleaned_data['serumcre'])
            val9 = float(fm.cleaned_data['serumsod'])
            val10 = float(fm.cleaned_data['sex'])
            val11 = float(fm.cleaned_data['smoke'])
            val12 = float(fm.cleaned_data['time'])
    
            pred_1=heartcheck.predict([[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12]])
    
            result2=""
            if pred_1==[1]:
                result2="positive"
            else:
                result2="negative"
            user = request.user
            heart_result = result2
            immunity_status = ""

            if(val10 == 0):
                genv = 61.8
            else:
                genv = 38.2

            print(val1 + genv + val7 / 10000)
            if(val4 == 1):
                total = (float)((val1 + genv + val7 / 10000.0)/3.0)
                
                if(total > 60.0):
                    immunity_status = "High Risk"

                elif(total > 56.0 and total <=60.0):
                    immunity_status = "Moderate"

                elif(total >= 50.0 and total <= 56.0):
                    immunity_status = "Low"
                elif(total < 50.0):
                    immunity_status = "Minimal"

            else:
                total = (float)((val1 + genv + val7 /10000.0 + val5 + val8 * 10.0)/5.0)
                
                if(total > 53.2):
                    immunity_status = "High Risk"
                elif(total > 51.2 and total <= 53.2):
                    immunity_status = "Moderate"
                elif(total > 47.2 and total <= 51.2):
                    immunity_status = "Low"
                elif(total <= 47.2):
                    immunity_status = "Minimal"

            
            total = 100.0 - total
            
            result_store = Patient(user=user, age=val1, anaemia=val2,crePhos=val3,diab=val4,ejecFrac=val5,highbp=val6,platecount=val7, serumcre=val8,serumsod=val9,sex=val10,smoke=val11,time=val12, Heart_Result=heart_result, Immunity_Status=immunity_status)
            result_store.save()
            fm = PatientRegistration()
            return render(request, 'models/heartf1.html', {'form': fm,"result3":result2,"Immunity_Score":total, })
    else:
        """
        pi = Patient.objects.get(pk=id)

        """
        fm = PatientRegistration()
    
        
        return render(request, 'models/heartf1.html', {'form': fm,})
        
    