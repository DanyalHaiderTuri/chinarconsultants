# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BoardOfDirector(models.Model):
    bod_id = models.IntegerField(db_column='BOD_ID', primary_key=True)  # Field name made lowercase.
    bod_name = models.CharField(db_column='BOD_name', max_length=20)  # Field name made lowercase.
    bod_tagline = models.CharField(db_column='BOD_TAGLINE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bod_quote = models.CharField(db_column='BOD_QUOTE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    bod_pic = models.CharField(db_column='BOD_PIC', max_length=567, blank=True, null=True)  # Field name made lowercase.
    bod_qualification = models.CharField(db_column='BOD_QUALIFICATION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bod_social = models.CharField(db_column='BOD_Social', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Board_of_director'


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=20, blank=True, null=True)
    no_of_members = models.IntegerField(blank=True, null=True)
    project_assigned = models.IntegerField(db_column='Project_assigned', blank=True, null=True)  # Field name made lowercase.
    dept_location = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Department'


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
