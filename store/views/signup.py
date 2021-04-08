from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password 
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self , request):
        return render(request, 'signup.html')
    def post(self , request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name =  postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        #validation
        value = {
            'first_name' :first_name,
            'last_name' :last_name,
            'phone' :phone,
            'email' :email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
    
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name , last_name , phone , email , password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
                
        else:
            data = {
                'error' : error_message,
                'values' : value
                
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self , customer):
        error_message = None;
        if(not customer.first_name):
            error_message = "First Name Reqired!!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif (not customer.last_name):
            error_message = "Last Name Reqired!!"
        elif len(customer.last_name) < 4:
            error_message = 'Lasr Name must be 4 char long or more'
        elif (not customer.phone):
            error_message = "Contact Number Reqired!!"
        elif len(customer.phone) < 10:
            error_message = 'Contact Number Must be 10 char long'
        elif len(customer.password) < 6:
            error_message = 'Password Must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email Must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Adress Already Registered...'
        return error_message
    



