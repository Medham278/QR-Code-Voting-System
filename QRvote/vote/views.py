from django.http import HttpResponse
from django.shortcuts import render
from .models import Voter
from django.core.files.storage import FileSystemStorage
from django import forms
from django.db import models
from django.forms import Textarea,TextInput,Select

class registerform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(registerform, self).__init__(*args, **kwargs) 
    class Meta:
        model=Voter
        fields=['name','email','gender','dob','religion','dp','address','aadhar','pan','ebill']
        widgets={
            'address': Textarea(attrs={'class':'form-control','cols':75, 'rows':1}),
            'aadhar': TextInput(attrs={'class':'form-control','id':'txtAadhar', 'size':75}),
            'pan': TextInput(attrs={'class':'form-control','id':'txtPANCard', 'size':75}),
            'name': TextInput(attrs={'class':'form-control','size':34}),
            'dob': TextInput(attrs={'class':'form-control','size':34}),
            'email': TextInput(attrs={'class':'form-control','size':34}),
            'gender': Select(attrs={'class':'form-control'}),
            'religion': Select(attrs={'class':'form-control'}),
        }
    def clean(self):
        super(registerform, self).clean()
        aadhar=self.cleaned_data.get('aadhar')
        pan=self.cleaned_data.get('pan')
        count=0
        while aadhar!=0:
            aadhar=aadhar//10
            count+=1
        if count==12 or count==16:
            pass
        else:
            self.errors['aadhar']=self.error_class(['Enter Valid Aadhar Number'])
        if len(pan)!=10:
            self.errors['pan']=self.error_class(['Enter Valid PAN Number'])
        else:
            alphas=pan[0:5]
            if not alphas.isalpha():
                self.errors['pan']=self.error_class(['Enter Valid PAN Number'])
            else:
                nums=pan[5:9]
                if not nums.isdigit():
                    self.errors['pan']=self.error_class(['Enter Valid PAN Number'])
                else:
                    lastalpha=pan[9:]
                    if not lastalpha.isalpha():
                        self.errors['pan']=self.error_class(['Enter Valid PAN Number'])
        return self.cleaned_data


# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        filledform=registerform(request.POST, request.FILES)
        if filledform.is_valid():
            post=filledform.save(commit=False)
            post.save()
            return HttpResponse("SSS Submitted!")
        else:
            return render(request,'tpregister.html',{'form':filledform})
    else:
        form=registerform()
        return render(request,'tpregister.html', {
        "form":form
    })