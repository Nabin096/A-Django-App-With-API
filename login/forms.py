from django import forms

class AlbumRegister(forms.Form):
    username= forms.CharField(max_length=250)
    password= forms.CharField(max_length=50)

class Code1(forms.Form):
    code1 = forms.CharField(max_length=250)

class Code2(forms.Form):
    code2 = forms.CharField(max_length=250)

class Code3(forms.Form):
    code3 = forms.CharField(max_length=250)

class Code4(forms.Form):
    code4 = forms.CharField(max_length=250)

class Code5(forms.Form):
    code5 = forms.CharField(max_length=250)

class Code6(forms.Form):
    code6 = forms.CharField(max_length=250)