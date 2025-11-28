from django.db import models

# Create your models here.
class Person(models.Model):
    fullname = models.CharField(max_length=100)
    account_number = models.CharField(primary_key=True)
    gender = models.CharField(choices=[('Male','Male'),('Female','Female')])
    education = models.CharField(choices=[('Graduate','Graduate'),('No Graduate','No Graduate')])
    marital_status = models.CharField(choices=[('Yes','Yes'),('No','No')])
    dependents = models.CharField(choices=[('Male','Male'),('Female','Female')])
    employment_status = models.CharField(choices=[('Employed','Employed'),('Self Employed','Self Employed'),('NotEmployed','Not Employed')])
    property_area = models.CharField(max_length=100)
    credit_score = models.IntegerField(default=0.0)
    applicants_monthly_income = models.IntegerField(default=0.0)
    co_applicants_monthly_income = models.IntegerField(default=0.0)
    loan_amount =models.IntegerField(default=0.0)
    loan_duration = models.CharField(choices=[('2 Months','2 Months'),('6 Months','6 Months'),('8 Months','8 Months'),('1 Year','1 Year'),('16 Months','16 Months')])

    def __str__(self):
        return f"{self.fullname} {self.account_number} {self.gender} {self.education} {self.marital_status} {self.dependents} {self.employment_status} {self.property_area} {self.credit_score} {self.applicants_monthly_income} {self.co_applicants_monthly_income} {self.loan_amount} {self.loan_duration}"