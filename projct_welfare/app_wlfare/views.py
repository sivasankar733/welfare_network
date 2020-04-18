from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from.models import RegistrationModel,UserthoughtsModel,EventsModel,WorkexperienceModel,PropertyModel
from.models import SharemarketModel,ReferencesModel,matrimonialModel,TechnicalModel,TravelModel,CelebrationsModel
from.forms import SharemarketForm,ReferenceForm,matrimonialForm,CelebrationForm,TravelForm
from.forms import RegisterForm,UserthoughtsForm,EventForm,TechnicalForm,WorkexperienceForm,PropertyForm

class showindex(View):
    def get(self,request):
        return render(request,"loging.html")
class adminloging(View):
    def post(self,request):
        us=request.POST.get("t1")
        ps=request.POST.get("t2")
        select=request.POST.get("t3")
        if select=="admin":
            if us=="admin" and ps=="admin":
                return render(request,"adminhome.html")
            else:
                messages.success(request,"invalid user name and password")
                return redirect("index")
        else:
            try:
                RegistrationModel.objects.get(name=us,pas=ps)
                return render(request,"user.html")
            except RegistrationModel.DoesNotExist:
                messages.success(request,"invalid details")
                return redirect("index")

class RegisterUser(View):
    def get(self,request):
        rgm=RegistrationModel()
        return render(request,"register.html",{"rf":RegisterForm(),"rm":rgm})
    def post(self,request):
        rgf=RegisterForm(request.POST)
        if rgf.is_valid():
            db=rgf.save(commit=False)
            db.status="pending"
            db.save()
            messages.success(request,"details was saved")
            return redirect("registeruser")
        else:
            rgm=RegistrationModel(request.POST)
            return render(request,"register.html",{"rf":rgf,"rm":rgm})

class AddThoughts(View):
    def get(self,request):
        utm=UserthoughtsModel()
        return render(request,"addthoughts.html",{"utf":UserthoughtsForm(),"um":utm})
    def post(self,request):
        uf=UserthoughtsForm(request.POST)
        if uf.is_valid():
            uf.save()
            messages.success(request,"details was saved")
            return redirect("addthoughts")
        else:
            utm=UserthoughtsModel(request.POST)
            return render(request,"addthoughts.html",{"utf":uf,"um":utm})

class ViewThoughts(View):
    def get(self,request):
        usm=UserthoughtsModel.objects.all()
        return render(request,"viewthoughts.html",{"usm":usm})

class AddEvents(View):
    def get(self,request):
        evm=EventsModel
        return render(request,"addevents.html",{"ef":EventForm(),"em":evm})
    def post(self,request):
        ef=EventForm(request.POST)
        if ef.is_valid():
            ef.save()
            messages.success(request,"details was saved")
            return redirect("addevents")
        else:
            evm=EventsModel(request.POST)
            return render(request,"addevents.html",{"ef":ef,"em":evm})

class ViewEvents(View):
    def get(self,request):
        evm=EventsModel.objects.all()
        return  render(request,"viewevents.html",{"em":evm})

class TechnicalAdd(View):
    def get(self,request):
        tcm=TechnicalModel
        return render(request,"technicaladd.html",{"tf":TechnicalForm(),"tm":tcm})
    def post(self,request):
        tcf=TechnicalForm(request.POST)
        if tcf.is_valid():
            tcf.save()
            messages.success(request,"technical details was saved")
            return redirect("technicaladd")
        else:
            tcm=TechnicalModel(request.POST)
            return render(request,"technicaladd.html",{"tf":tcf,"tm":tcm})


class ViewTechnical(View):
    def get(self,request):
        tcm=TechnicalModel.objects.all()
        return render(request,"viewtechnical.html",{"tm":tcm})


class WorkExperience(View):
    def get(self,request):
        wem=WorkexperienceModel
        return render(request,"workexperience.html",{"wf":WorkexperienceForm(),"wm":wem})
    def post(self,request):
        wef=WorkexperienceForm(request.POST)
        if wef.is_valid():
            wef.save()
            messages.success(request,"work experience  details was saved")
            return redirect("workexperience")
        else:
            wem=WorkexperienceModel(request.POST)
            return render(request,"workexperience.html",{"wf":wef,"wm":wem})


class ViewWorkExperience(View):
    def get(self,request):
        wm=WorkexperienceModel.objects.all()
        return render(request,"viewworkexp.html",{"wm":wm})


class AddProperty(View):
    def get(self,request):
        ppm=PropertyModel
        return render(request,"addproperty.html",{"pf":PropertyForm(),"pm":ppm})
    def post(self,request):
        ppf=PropertyForm(request.POST)
        if ppf.is_valid():
            ppf.save()
            messages.success(request,"Property details was saved")
            return redirect("property")
        else:
            ppm=PropertyModel(request.POST)
            return render(request,"addproperty.html",{"pf":ppf,"pm":ppm})


class ViewProperty(View):
    def get(self,request):
        ppm=PropertyModel.objects.all()
        return render(request,"viewproperty.html",{"ppm":ppm})

class AddShareMarket(View):
    def get(self,request):
        shm=SharemarketModel
        return render(request,"addsharemarket.html",{"sf":SharemarketForm(),"sm":shm})
    def post(self,request):
        shf=SharemarketForm(request.POST)
        if shf.is_valid():
            shf.save()
            messages.success(request,"Share Market details saved")
            return redirect("addsharemarket")
        else:
            shm=SharemarketModel(request.POST)
            return render(request,"addsharemarket.html",{"sf":shf,"sm":shm})

class ViewShareMarket(View):
    def get(self,request):
        smm=SharemarketModel.objects.all()
        return render(request,"viewsharemarket.html",{"sm":smm})

class AddReference(View):
    def get(self,request):
        rfm=ReferencesModel
        return render(request,"addreference.html",{"rf":ReferenceForm(),"rm":rfm})
    def post(self,request):
        ref=ReferenceForm(request.POST)
        if ref.is_valid():
            ref.save()
            messages.success(request,"Reference details was saved")
            return redirect("addreference")
        else:
            rm=ReferencesModel(request.POST)
            return render(request,"addreference.html",{"rf":ref,"rm":rm})

class ViewReferences(View):
    def get(self, request):
        rm=ReferencesModel.objects.all()
        return render(request, "viewreference.html", {"rm": rm})


class AddMatrimonial(View):
    def get(self, request):
        mm=matrimonialModel
        return render(request,"addmatrimonial.html",{"mf":matrimonialForm(),"mm":mm})

    def post(self, request):
        mtf=matrimonialForm(request.POST)
        if mtf.is_valid():
            mtf.save()
            messages.success(request,"matrimonialdetails was saved")
            return redirect('addmatrimonial')
        else:
            mm=matrimonialModel(request.POST)
            return render(request,"addmatrimonial.html",{"mf":mtf,"mm":mm})

class ViewMatrimonial(View):
    def get(self,request):
        mm=matrimonialModel.objects.all()
        return render(request,"viewmatrimonial.html",{"mm":mm})


class AddCelebrations(View):
    def get(self, request):
        ctm=CelebrationsModel
        return render(request, "addcelebrations.html", {"cf":CelebrationForm(),"cm":ctm})
    def post(self, request):
        ctf=CelebrationForm(request.POST)
        if ctf.is_valid():
            ctf.save()
            messages.success(request, "celebrations details was saved")
            return redirect("addcelebrations")
        else:
            cm=CelebrationsModel(request.POST)
            return render(request, "addcelebrations.html", {"cf":ctf,"cm":cm})


class ViewCelebrations(View):
    def get(self,request):
        cm=CelebrationsModel.objects.all()
        return render(request,"viewcelebrations.html",{"cm":cm})


class AddTravel(View):
    def get(self, request):
        tvm=TravelModel
        return render(request, "addtravel.html", {"tf":TravelForm(),"tm":tvm})
    def post(self, request):
        tvf=TravelForm(request.POST)
        if tvf.is_valid():
            tvf.save()
            messages.success(request, "travel details was saved")
            return redirect("addtravel")
        else:
            tvm=TravelModel(request.POST)
            return render(request, "addtravel.html", {"tf":tvf,"tm":tvm})


class ViewTravel(View):
    def get(self,request):
        tvm=TravelModel.objects.all()
        return render(request,"viewtravel.html",{"tm":tvm})


def approvaldetails(request):
    rsm=RegistrationModel.objects.filter(status='pending')
    return render(request,"approval.html",{"rm":rsm})

def accept_user(request):
    rno=request.GET.get('rno')
    RegistrationModel.objects.filter(idno=rno).update(status="accepted")
    return redirect('approval')

def reject_user(request):
    rno=request.GET.get('rno')
    RegistrationModel.objects.filter(idno=rno).update(status="rejected")
    return redirect('approval')


def show_accept_user(request):
    rm=RegistrationModel.objects.filter(status='accepted')
    return render(request,"accept_show.html",{"rm":rm})

def show_reject_user(request):
    rm=RegistrationModel.objects.filter(status='rejected')
    return render(request,"reject_show.html",{"rm":rm})