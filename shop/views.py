from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView
from .models import Brands,Mobile,Order,Cart
from .forms import BrandForm,MobileForm,OrderForm,UserRegForm
from django.contrib.auth import authenticate,login,logout
# ======================================Start Brand section========================================
class BrandCreate(TemplateView):
    model=Brands
    form_class=BrandForm
    template_name = 'shop/brandcreate.html'
    context={}
    def get(self, request, *args, **kwargs):
        self.context['form']=self.form_class
        brands=self.model.objects.all()
        print(brands)
        self.context['brands']=brands
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        form.save()
        return redirect('brandcreate')

class BrandEdit(TemplateView):
    model=Brands
    form_class=BrandForm
    template_name = 'shop/brandedit.html'
    context={}
    def get_brand(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        brand=self.get_brand(kwargs['id'])
        form=self.form_class(instance=brand)
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        brand = self.get_brand(kwargs['id'])
        form=self.form_class(request.POST,instance=brand)
        form.save()
        return redirect('brandcreate')

class BrandDelete(TemplateView):
    model=Brands
    def get(self, request, *args, **kwargs):
        brand=self.model.objects.get(id=kwargs['id'])
        brand.delete()
        return redirect('brandcreate')

# ======================================end brand section=============================================

# ===============================================mobile section start=====================================

class MobileCreate(TemplateView):
    model=Mobile
    form_class=MobileForm
    template_name = 'shop/mobilecreate.html'
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('mobilelist')
        else:
           self.context['form']=form
           return render(request,self.template_name,self.context)

class MobileList(TemplateView):
    model=Mobile
    template_name = 'shop/mobilelist.html'
    context={}
    def get(self, request, *args, **kwargs):
        mobiles=Mobile.objects.all()
        self.context['mobiles']=mobiles
        return render(request,self.template_name,self.context)

# =============================================mobile section end=========================================
# user section
def user_registration(request):
    form=UserRegForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
        else:
            form=UserRegForm(request.POST)
            context['form']=form
            return render(request, 'shop/userreg.html', context)

    return render(request,'shop/userreg.html',context)

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('mobilelist')
        else:
            return render(request, 'shop/login.html')


    return render(request,'shop/login.html')

def user_logout(request):
    logout(request)
    return redirect('userlogin')
# end user section



# order section
class OrderCreate(TemplateView):
    model=Order
    form_class=OrderForm
    template_name = 'shop/ordercreate.html'
    context={}
    def get(self, request, *args, **kwargs):
        mobile=Mobile.objects.get(id=kwargs['id'])

        form=self.form_class(initial={'product':mobile,'user':request.user})
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orderlist')

class Orderlist(TemplateView):
    model=Order
    template_name = 'shop/orderlist.html'
    context={}
    def get(self, request, *args, **kwargs):
        orders=self.model.objects.all().filter(user=request.user)
        self.context['orders']=orders
        return render(request,self.template_name,self.context)

class OrderCancel(TemplateView):
    model=Order
    def get(self, request, *args, **kwargs):
        product=self.model.objects.get(id=kwargs['pk'])
        product.delete()
        return redirect('orderlist')

class OrderDetails(TemplateView):
    model=Order
    template_name = 'shop/orderdetail.html'
    context={}
    def get(self, request, *args, **kwargs):
        item=self.model.objects.get(id=kwargs['pk'])
        self.context['item']=item
        return render(request,self.template_name,self.context)

# order section end

# cart section start
class AddToCart(TemplateView):
    model=Cart
    # context={}
    # template_name = 'shop/cart.html'
    def get(self, request, *args, **kwargs):
        mobile=Mobile.objects.get(id=kwargs['id'])
        # product=mobile.mobile_name
        # price=mobile.price
        item=self.model(user=request.user,product=mobile)
        item.save()
        # self.context['item']=item
        return redirect('cartview')



class Cartview(TemplateView):
    model=Cart
    template_name = 'shop/cart.html'
    context={}
    def get(self, request, *args, **kwargs):
        items=self.model.objects.all().filter(user=request.user)
        print(items)
        self.context['items']=items
        return render(request,self.template_name,self.context)
class CartDelete(TemplateView):
    model=Cart
    def get(self, request, *args, **kwargs):
        item=self.model.objects.get(id=kwargs['pk'])
        item.delete()
        return redirect('cartview')




