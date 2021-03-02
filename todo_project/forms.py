from django import forms
from .models import Plandata,Completion

class PlandataForm(forms.ModelForm):
    class Meta:
        model = Plandata
        fields = ['toki','basho','naiyo']

class CompletionForm(forms.ModelForm):
    class Meta:
        model = Completion
        fields = ['toki','kanryo_day','basho','naiyo']

class Todo_addForm(forms.Form):
    toki = forms.DateField(label='日付',widget=forms.DateInput(attrs={"type":"date","placeholder":'例）1234-1-23'}))
    basho = forms.CharField(label='場所',widget=forms.Textarea(attrs={'rows':8, 'cols':50}),max_length=50)
    naiyo = forms.CharField(label='内容',widget=forms.Textarea(attrs={'rows':8, 'cols':50}),max_length=100)

