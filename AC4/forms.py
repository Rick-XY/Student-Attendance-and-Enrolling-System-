from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , BooleanField, SubmitField,DateTimeField,DateField,SelectField,IntegerField
from wtforms.validators import DataRequired , Length , Email , EqualTo
# from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields.html5 import DateTimeLocalField
# from wtform import Form
from datetime import datetime
from wtforms.validators import NumberRange
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import sys
# from apps.shared.models import db
# from myapp import models
# from wtforms import validators
from wtforms_sqlalchemy.orm import model_form

class RegisterationForm(FlaskForm):
	username = StringField('User Name:', validators=[DataRequired(),Length(min=1,max=25)])
	email = StringField('Email:',validators=[DataRequired()],render_kw={"Placeholder": "email@sth.com"})
	password = PasswordField('Password:' , validators=[DataRequired()])
	confirm_passwod = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('GO')

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired()],render_kw={"Placeholder": "email@sth.com"})
	password = PasswordField('Password' , validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('GO')
	
class updateprofileForm(FlaskForm):
	username = StringField('username', validators=[DataRequired(),Length(min=1,max=25)])
	email = StringField('email',validators=[DataRequired()],render_kw={"placeholder": "email@sth.com"})
	password = StringField('password',validators=[DataRequired()])

class uploadfileForm(FlaskForm):
	xlsxfile = FileField('File',validators=[FileRequired()])

class StudentaddForm(FlaskForm):
	id = IntegerField('Id', validators=[DataRequired(), NumberRange(min=1, max=99999999)])
	surname = StringField('Surname', validators=[DataRequired(),Length(min=1,max=80)])
	title = SelectField('Title',choices=[('Miss'), ('Mr'),('Mrs'),('Ms'),('Mx'),('Dr')])
	gname = StringField('Given name', validators=[DataRequired(),Length(min=1,max=80)])
	teachperiod = StringField('Teach Period', validators=[DataRequired(),Length(min=1,max=80)])
	# unitcode = StringField('unitcode', validators=[DataRequired(),Length(min=1,max=80)])
	unitcode = SelectField('Unit Code', validators=[])
	# unitcode = QuerySelectField(query_factory=unit.objects.all,get_pk=lambda a: a.unitcode,get_label=lambda a: a.unitcode)
	unitmode = SelectField('Unit Mode',choices=[('On'),('Off')], validators=[])
	unitstatus =SelectField('Unit Status',choices=[('ENROLLED'),('not ENROLLED')], validators=[])
	crsstatus = SelectField('Crs Status',choices=[('ENROLLED'),('not ENROLLED')], validators=[])
	email = StringField('Email', validators=[DataRequired(),Length(min=1,max=200)],render_kw={"placeholder": "email@sth.com"})
	unittitle = StringField('Unit Title', validators=[DataRequired(),Length(min=1,max=80)])
	pgname = StringField('Preferred Given name', validators=[Length(min=0,max=80)])
	crsscode = StringField('Crs Code', validators=[DataRequired(),Length(min=1,max=80)])



class UpdateStudentForm(FlaskForm):
	id = IntegerField('Id', validators=[DataRequired(),NumberRange(min=1,max=99999999)])
	surname = StringField('Surname', validators=[DataRequired(),Length(min=1,max=80)])
	title = SelectField('Title',choices=[('Miss'), ('Mr'),('Mrs'),('Ms'),('Mx'),('Dr')])
	gname = StringField('Given Name', validators=[DataRequired(),Length(min=1,max=80)])
	teachperiod = StringField('Teach Period', validators=[DataRequired(),Length(min=1,max=80)])
	unitcode = SelectField('Unit Code', validators=[])
	unitmode = SelectField('Unit Mode',choices=[('On'),('Off')])
	unitstatus =SelectField('Unit Status',choices=[('ENROLLED'),('not ENROLLED')])
	crsstatus = SelectField('Crs Status',choices=[('ENROLLED'),('not ENROLLED')])
	email = StringField('Email', validators=[DataRequired(),Length(min=1,max=200)],render_kw={"placeholder": "email@sth.com"})
	unittitle = StringField('Unit Title', validators=[Length(min=1,max=80)])
	pgname = StringField('Prefered Given Name', validators=[Length(min=0,max=80)])
	crsscode = StringField('Crs Code', validators=[Length(min=1,max=80)])


class UnitaddForm(FlaskForm):
	unitcode = StringField('Unit Code', validators=[DataRequired(),Length(min=1,max=25)])
	instructorname = StringField('Instructor Name', validators=[DataRequired(),Length(min=1,max=80)])
	instructoremail = StringField('Instructor Email', validators=[DataRequired(),Length(min=1,max=180)])

class UpdateUnitForm(FlaskForm):
	unitcode = StringField('Id', validators=[DataRequired(),Length(min=1,max=25)])
	instructorname = StringField('Surname', validators=[DataRequired(),Length(min=1,max=80)])
	instructoremail = StringField('Title', validators=[DataRequired(),Length(min=1,max=80)])

class AbsenceForm(FlaskForm):
	# SomeModel.query.with_entities(SomeModel.col1, SomeModel.col2)
	# id =  StringField('id',validators=[DataRequired(),Length(min=1,max=25)])
	studentid =  StringField('Student Id',validators=[DataRequired(),Length(min=1,max=25)])
	gname =  StringField('Given Name',validators=[DataRequired(),Length(min=1,max=25)])
	surname =  StringField('Surname',validators=[DataRequired(),Length(min=1,max=25)])
	date =  DateField('Date(MM DD YYYY)', format='%m %d %Y', default=datetime.now())
	unitcode =  SelectField('Unit Code', choices= [] , validators=[])
	classtype =  SelectField('Class Type',choices=[('Lecture'),('Clinic'),('Lab'),('Tutorial'),('Workshop'),('Placement'),('Other')])
	# SelectField('crsstatus',choices=[('ENROLLED'),('not ENROLLED')])
	reason =  SelectField('Reason',choices=[('Medical'),('Commitment'),('Personal/Family'),('Other'),('No Reason'),('Event'),])
	note =  StringField('Note',validators=[DataRequired(),Length(min=1,max=25)])

# (g.id, g.name) for g in Group.query.order_by('name')

class AbsenceFilterForm(FlaskForm):
	treshhold =  StringField('Threshhold', default=3)	
	studentid =  StringField('Student Id',validators=[Length(min=1,max=25)])
	gname =  StringField('Given name',validators=[Length(min=1,max=25)])
	surname =  StringField('Surname',validators=[Length(min=1,max=25)])
	datefrom =  DateField('Date From', format='%m %d %Y', default=datetime.now())
	dateto =  DateField('Date Until', format='%m %d %Y', default=datetime.now())
	unitcode =  StringField('Unit Code',validators=[Length(min=1,max=25)])
	classtype =  SelectField('Class Type',choices=[(''),('Lecture'),('Clinic'),('Lab'),('Tutorial'),('Workshop'),('Placement'),('Other'),])
	# classtype =  StringField('classtype',validators=[Length(min=1,max=25)])
	reason =  SelectField('reason',choices=[(''),('Medical'),('Commitment'),('Personal/Family'),('Other'),('No Reason'),('Event'),])
	# reason =  StringField('reason',validators=[Length(min=1,max=25)])
	note =  StringField('note',validators=[Length(min=1,max=25)])
	save = SubmitField('Filter')
	publish = SubmitField('Generate Letter')