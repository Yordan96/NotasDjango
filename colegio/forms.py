from django import forms

from .models import Materia, Grado

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre', 'seccion','materias')
    def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Seleccione las materias del grado"
        self.fields["materias"].queryset = Materia.objects.all()
