from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(db_column='Emp_ID', primary_key=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=20)  # Field name made lowercase.
    social_media = models.CharField(db_column='Social_Media', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emp_pic = models.CharField(db_column='Emp_Pic', max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=220, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=40, blank=True, null=True)  # Field name made lowercase.
    seniority = models.CharField(db_column='Seniority', max_length=20, blank=True, null=True)  # Field name made lowercase.
    joining_date = models.DateField(db_column='Joining_Date', blank=True, null=True)  # Field name made lowercase.
    pay_scale = models.IntegerField(db_column='Pay_Scale', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    allowed_holidays = models.IntegerField(db_column='Allowed_holidays', blank=True, null=True)  # Field name made lowercase.
    availed_holidays = models.IntegerField(db_column='Availed_holidays', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'
