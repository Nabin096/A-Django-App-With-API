from django.shortcuts import render
from .models import profiles
from .forms import AlbumRegister,Code1, Code2, Code3, Code4, Code5, Code6

def register(request):
    all_profiles = profiles.objects.all()
    username = ""
    password = ""
    context = {

    }
    if request.method == 'POST':
        myForm = AlbumRegister(request.POST)
        if myForm.is_valid():
            username = myForm.cleaned_data['username']
            password = myForm.cleaned_data['password']
            flag = 0
            dbuser = profiles()
            for i in range(len(all_profiles)):
                if all_profiles[i].username == username and all_profiles[i].password == password:
                    dbuser = profiles.objects.filter(password=password)
                    flag = 1
            request.session['username'] = username
            if flag == 1:
                context = {
                    'user': dbuser[0]
                }
                if dbuser[0].filled:
                    return render(request, 'login/profileview.html', context)
                else:
                    context3 = {
                        'status': dbuser[0].status
                    }
                    return render(request,'login/'+ str(dbuser[0].status) +'.html', context3)
            else:
                new_profile = profiles()
                new_profile.username = username
                new_profile.password = password
                new_profile.save()

                context={'new_profile':new_profile}
                return render(request,'login/dashboard.html',context)
    else:
        myForm = AlbumRegister(request.GET)
        return render(request, 'login/index.html')

def dashboard(request,status):
    code1=""
    code2 = ""
    code3 = ""
    code4 = ""
    code5 = ""
    code6 = ""
    context2 = {

    }
    dbuser = profiles()
    if request.method == 'POST':
        if request.session.has_key('username'):
            username = request.session['username']
            dbuser = profiles.objects.filter(username=username)
            context2 = {
                'status': status
            }
            user = profiles.objects.get(username=username)

            if user.status == 1:
                MyForm2 = Code1(request.POST)
                if MyForm2.is_valid():
                    code1 = MyForm2.cleaned_data['code1']
                    print("yo")
                    user.code1 = code1
            if user.status == 2:
                MyForm3 = Code2(request.POST)
                if MyForm3.is_valid():
                    code2 = MyForm3.cleaned_data['code2']
                    user.code2 = code2
            if user.status == 3:
                MyForm4 = Code3(request.POST)
                if MyForm4.is_valid():
                    code3 = MyForm4.cleaned_data['code3']
                    user.code3 = code3
            if user.status == 4:
                MyForm5 = Code4(request.POST)
                if MyForm5.is_valid():
                    code4 = MyForm5.cleaned_data['code4']
                    user.code4 = code4
            if user.status == 5:
                MyForm6 = Code5(request.POST)
                if MyForm6.is_valid():
                    code5 = MyForm6.cleaned_data['code5']
                    user.code5 = code5
            if user.status == 6:
                MyForm7 = Code6(request.POST)
                if MyForm7.is_valid():
                    code6 = MyForm7.cleaned_data['code6']
                    user.code6 = code6
            user.status += 1
            user.save()
            return render(request, 'login/'+ str(user.status) +'.html',context2)
    else:
        if request.method == 'GET':
            if request.session.has_key('username'):
                username = request.session['username']
                user = profiles.objects.get(username=username)
                context2 = {
                    'status': status
                }
                if user.status == 1:
                    MyForm2 = Code1(request.GET)
                if user.status == 2:
                    MyForm2 = Code2(request.GET)
                if user.status == 3:
                    MyForm2 = Code3(request.GET)
                if user.status == 4:
                    MyForm2 = Code4(request.GET)
                if user.status == 5:
                    MyForm2 = Code5(request.GET)
                if user.status == 6:
                    MyForm2 = Code6(request.GET)
                return render(request,'login/'+ str(user.status) +'.html',context2)

def logout(request):
    try:
        del request.session['username']
    except:
        pass

    return render(request,'login/index.html',{})