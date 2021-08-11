from django.contrib import admin
from models.models import Patient,DiabetesPatient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'user','age', 'anaemia', 'crePhos', 'diab', 'ejecFrac', 'highbp', 'platecount', 'serumcre','serumsod', 'sex', 'smoke', 'time' ,'Heart_Result', 'Immunity_Status', 'timestamp')


@admin.register(DiabetesPatient)
class PatientAdmin1(admin.ModelAdmin):
    list_display = ('patient_id', 'user','preg', 'gluc', 'bp', 'skinthick', 'insul', 'bmi', 'diabpedfun', 'age','Diabetes_Result', 'Immunity_Status', 'timestamp')