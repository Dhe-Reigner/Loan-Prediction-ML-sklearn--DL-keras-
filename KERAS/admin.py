from django.contrib import admin
from .models import Person

# Register your models here.

class adminPerson(admin.ModelAdmin):
    list_display = ('fullname','account_number','gender','education','marital_status','dependents','employment_status','property_area','credit_score','applicants_monthly_income','co_applicants_monthly_income','loan_amount','loan_duration')
admin.site.register(Person,adminPerson)
