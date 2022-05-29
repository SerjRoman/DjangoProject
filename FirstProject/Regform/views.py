from django.shortcuts import render

# Create your views here.
def regForm(request):
    return render(request, 'appRegform/reg.html') 


class RegisterUser(TemplateView):
    template_name = "appLogikaStats/registration.html"
    errortext = 0
    #
    def dispatch(self, request):
        #
        try:
            #
            if request.method == "POST":#Information that get from POST request
                username = request.POST.get("user_name") #user_name
                password1 = request.POST.get("password_1") #pass
                password2 = request.POST.get("password_2") #re_pass
                if password1 == password2: #checking pass = re_pass
                    User.objects.create_user(username, password1, password2) #
                    self.errortext = 0 #
                    return redirect("login") #pass != re_pass
                else: #
                    self.errortext =" Пароли не совпадают!" #
        except:
            self.errortext = "Данные введены некоректно!!!" #
        #
        return render(request, self.template_name, context= {"errortext": self.errortext})
#