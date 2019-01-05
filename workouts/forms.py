from django.forms import ModelForm
from workouts.models import Exercise

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_nm', 'ex_type_cd']
