from cms.models import User
from django.forms import ModelForm
from django import forms

from log import models
from log.models import Workout, WorkoutType, Discipline, Performances
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
				return f"<td><div class='d-flex justify-content-between'><span class='date text-primary'><strong>{day}</strong></span>{Workout.get_date(self,self.year,self.month,day)}</div>{d}</td>"
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


		cal = f'<div  class="order-2">{self.formatmonthname(self.year, self.month, withyear=withyear)}</div></div>\n'
		cal += f'<div class="overflow-auto">\n'
		cal += f'<table class="table calendar">\n'
		cal += f'{self.formatweekheader()}\n'
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



class PerformancesForm(ModelForm):
	class Meta:
		model = Performances
		fields = ('performance','performedat','discipline_id')

	def __init__(self, *args, **kwargs):
		self.name = kwargs.pop('name')
		super(PerformancesForm, self).__init__(*args, **kwargs)
		self.fields['discipline_id'].queryset = Discipline.objects.filter(Q(user=self.name) | Q(user='1'))

	discipline_id = forms.ModelChoiceField(
		queryset=None,
		widget=forms.RadioSelect
	)


class DisciplineForm(forms.ModelForm):
	class Meta:
		model = Discipline
		fields = ('name','unit')

