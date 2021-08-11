
from django import forms
from models.models import Patient,DiabetesPatient

class PatientRegistration(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'anaemia', 'crePhos', 'diab', 'ejecFrac', 'highbp', 'platecount', 'serumcre', 'serumsod','sex' ,'smoke', 'time']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n1'}),
            'anaemia': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n2'}),
            'crePhos': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n3'}),
            'diab': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n4'}),
            'ejecFrac': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n5'}),
            'highbp': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n6'}),
            'platecount': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n7'}),
            'serumcre': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n8', 'step':'0.1'}),
            'serumsod': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n9'}),
            'sex': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n10'}),
            'smoke': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n11'}),
            'time': forms.NumberInput(attrs={'class': 'form-control','id': 'age','name': 'n12'}),
        }

class PatientRegistration1(forms.ModelForm):
    class Meta:
        model = DiabetesPatient
        fields = ['preg', 'gluc', 'bp', 'skinthick', 'insul', 'bmi', 'diabpedfun', 'age']
        widgets = {
            'preg': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n1'}),
            'gluc': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n2'}),
            'bp': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n3'}),
            'skinthick': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n4'}),
            'insul': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n5'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n6', 'step':'0.1'}),
            'diabpedfun': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n7', 'step':'0.1'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'name': 'n8'}),
        }



