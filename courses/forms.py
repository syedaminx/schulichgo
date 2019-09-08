from django import forms
from django.forms import ModelChoiceField
from .models import Review, Course, Syllabus

class ReviewForm(forms.ModelForm):

    choices=(
        ('EXAMPLE', 'example'),
    )

    instructor = forms.ChoiceField(choices=choices)

    def __init__(self, *args, **kwargs):
        instructors = kwargs.pop('instructors')
        super(ReviewForm, self).__init__(*args, **kwargs)
        instructors = instructors
        instructors = tuple(zip(instructors, instructors))
        self.fields['instructor'].choices = instructors

    class Meta:
        model = Review
        fields = ('usefulness_rating', 'difficulty_rating', 'instructor_rating', 'comment', 'instructor', 'taken_season', 'taken_year', 'anonymous')

class SyllabusForm(forms.ModelForm):

    class Meta:
        model = Syllabus
        fields = ('syllabus',)
