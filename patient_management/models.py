from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Mapping(models.Model):
    patient = models.ForeignKey('patient_management.Patient', on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey('doctor_management.Doctor', on_delete=models.CASCADE, related_name='mappings')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
