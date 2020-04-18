from django import forms
from .models import RegistrationModel
from.models import UserthoughtsModel,EventsModel,TechnicalModel,WorkexperienceModel,PropertyModel
from.models import SharemarketModel,ReferencesModel,matrimonialModel,CelebrationsModel,TravelModel
import re

class RegisterForm(forms.ModelForm):
    idno=forms.IntegerField(min_value=100)
    pas=forms.CharField(widget=forms.PasswordInput)
    dob=forms.DateField(help_text="yyyy-mm-dd")
    con=forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model=RegistrationModel
        fields="__all__"
        exclude=('status','idno',)

    def clean_name(self):
        name=self.cleaned_data["name"]
        res=re.match("^[A-Za-z]*$",name)
        if res==None:
            raise forms.ValidationError("invalid name")
        else:
            return name


class UserthoughtsForm(forms.ModelForm):
    contact=forms.IntegerField(widget=forms.NumberInput,help_text="enter 10 digit number only")
    class Meta:
        model=UserthoughtsModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name

class EventForm(forms.ModelForm):
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    startdate = forms.DateField(help_text="yyyy-mm-dd")
    enddate = forms.DateField(help_text="yyyy-mm-dd")
    class Meta:
        model=EventsModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name
class TechnicalForm(forms.ModelForm):
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    class Meta:
        model=TechnicalModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name

class WorkexperienceForm(forms.ModelForm):
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    class Meta:
        model=WorkexperienceModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name
class PropertyForm(forms.ModelForm) :
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    area_size=forms.IntegerField(min_value=100)
    price=forms.FloatField(min_value=10000)
    class Meta:
        model=PropertyModel
        fields="__all__"
    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name

class SharemarketForm(forms.ModelForm):
    share_value=forms.IntegerField(min_value=10000)
    class Meta:
        model=SharemarketModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name
    def clean_description(self):
        des=self.cleaned_data["description"]
        de=re.match("^[A-Za-z]*$",des)
        if de==None:
            raise forms.ValidationError("invalid description")
        else:
            return des
class ReferenceForm(forms.ModelForm):
    lastdate=forms.DateField(help_text="yyyy-mm-dd")
    class Meta:
        model=ReferencesModel
        fields="__all__"
    def clean_name(self):
        name=self.cleaned_data["name"]
        res=re.match("^[A-Za-z]*$",name)
        if res==None:
            raise forms.ValidationError("invalid name")
        else:
            return name
class matrimonialForm(forms.ModelForm):
    gen=(
        ("male",'Male'),('female','Female'),('other','other'))

    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    dob=forms.DateField(help_text="yyyy-mm-dd")
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    class Meta:
        model=matrimonialModel
        fields="__all__"
    def clean_name(self):
        name=self.cleaned_data["name"]
        res=re.match("^[A-Za-z]*$",name)
        if res==None:
            raise forms.ValidationError("invalid name")
        else:
            return name
class CelebrationForm(forms.ModelForm):
    dob = forms.DateField(help_text="yyyy-mm-dd")
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    class Meta:
        model=CelebrationsModel
        fields="__all__"
    def clean_name(self):
        name=self.cleaned_data["name"]
        res=re.match("^[A-Za-z]*$",name)
        if res==None:
            raise forms.ValidationError("invalid name")
        else:
            return name
class TravelForm(forms.ModelForm):
    contactno = forms.IntegerField(widget=forms.NumberInput, help_text="enter 10 digit number only")
    travel_date= forms.DateField(help_text="yyyy-mm-dd")
    class Meta:
        model=TravelModel
        fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.match("^[A-Za-z]*$", name)
        if res == None:
            raise forms.ValidationError("invalid name")
        else:
            return name
