from cms.models import User
from django.forms import ModelForm
from django import forms

from log import models
from log.models import Workout, WorkoutType
from calendar import HTMLCalendar
from datetime import date
from colorfield.widgets import ColorWidget
from django.db.models import Q


class WorkoutForm(ModelForm):
	class Meta:
		model = Workout
		fields = ('date','time','workouttype','name','description','feeling','effort','notes')

	def __init__(self, *args, **kwargs):
		self.name = kwargs.pop('name')
		super(WorkoutForm, self).__init__(*args, **kwargs)
		#workouts = WorkoutType.objects.filter(Q(user=self.name) | Q(user='1'))
		#workouttypes = [(i.id,i.name) for i in workouts]
		#self.fields['workouttype'] = forms.ModelChoiceField(choices=workouttypes)
		self.fields['workouttype'].queryset = WorkoutType.objects.filter(Q(user=self.name) | Q(user='1'))



	workouttype = forms.ModelChoiceField(
		queryset=None,
		widget=forms.RadioSelect
	)


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, current=None):
		self.year = year
		self.month = month
		self.current = current
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(date__day=day)
		d = ''
		for event in events_per_day:
			d += f' {event.get_html_url}'

		if day != 0:
			if date.today() == date(self.year, self.month, day):
				return f"<td class='bg-light'><div class='d-flex justify-content-between'><span class='date'>{day}</span>{Workout.get_date(self,self.year,self.month,day)}</div>{d}</td>"
			return f"<td><div class='d-flex justify-content-between'><span class='date'>{day}</span>{Workout.get_date(self,self.year,self.month,day)}</div>{d}</td>"
		return '<td class="bg-light"></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Workout.objects.filter(date__year=self.year, date__month=self.month,user=self.current)

		if self.month == 1 :
			cal = f'<div class="order-2">Leden {self.year}</div></div>'
		elif self.month == 2 :
			cal = f'<div class="order-2">Únor {self.year}</div></div>'
		elif self.month == 3 :
			cal = f'<div class="order-2">Březen {self.year}</div></div>'
		elif self.month == 4 :
			cal = f'<div class="order-2">Duben {self.year}</div></div>'
		elif self.month == 5 :
			cal = f'<div class="order-2">Květen {self.year}</div></div>'
		elif self.month == 6 :
			cal = f'<div class="order-2">Červen {self.year}</div></div>'
		elif self.month == 7 :
			cal = f'<div class="order-2">Červenec {self.year}</div></div>'
		elif self.month == 8 :
			cal = f'<div class="order-2">Srpen {self.year}</div></div>'
		elif self.month == 9 :
			cal = f'<div class="order-2">Září  {self.year}</div></div>'
		elif self.month == 10:
			cal = f'<div class="order-2">Říjen  {self.year}</div></div>'
		elif self.month == 11:
			cal = f'<div class="order-2">Listopad   {self.year}</div></div>'
		elif self.month == 12:
			cal = f'<div class="order-2">Prosinec  {self.year}</div></div>'
		else :
			cal = f'<div  class="order-2">  {self.year}</div></div>'

		cal += f'<div class="overflow-auto">\n'
		cal += f'<table class="table calendar">\n'
		cal += f'<tr><th class="mon">Pondělí</th><th class="tue">Úterý</th><th class="wed">Středa</th><th class="thu">Čtvrtek</th><th class="fri">Pátek</th><th class="sat">Sobota</th><th class="sun">Neděle</th></tr>'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal
	
	
	
class TypesForm(ModelForm):
	class Meta:
		model = WorkoutType
		fields = ('name','color')
		widgets = {
			'color': ColorWidget,
		}

	def __init__(self, *args, **kwargs):
		super(TypesForm, self).__init__(*args, **kwargs)

