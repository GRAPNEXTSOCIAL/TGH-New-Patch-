from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from .models import *
from .forms import *
from django.db.models import Q
from django.http import JsonResponse
# For Function based login view
from django.contrib.auth.decorators import login_required
# For Class based login view
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from .models import Product, Cart, Customer, OrderPlaced, User

import json




def home(request):
    # view = ProductView()
    # return view.get(request)
    return redirect('login')
# Admin Views

class CustomLoginView(auth_views.LoginView):
    template_name = 'app/login.html'
    success_url = '/dologin'

#login page
def login(request):
    if request.user.is_superuser:
        return redirect('admin-home')
    elif request.user.staff_category == MANAGER:
        return render(request, 'staff/staff_home.html')
    elif request.user.staff_category == CASHIER:
        return render(request, 'cash_counter/cashier_home.html')
    elif request.user.staff_category == ACCOUNTANT:
        return render(request, 'accountant_app/accountant_home.html')
    else:
        return redirect('home')


def dashboard(request):
    product = Product.objects.all()
    supplier = Supplier.objects.all()
    return render(request, 'admin_app/admin_home.html', {'product_list':product, 'supplier_list':supplier})


# All Lists (admin)
# Product View list(Admin)
def all_products(request):
    product_list = Product.objects.all()
    return render(request, 'admin_app/products.html', {'product_list':product_list})

# Cart View list(Admin)
def all_carts(request):
    cart_list = Cart.objects.all()
    return render(request, 'admin_app/carts.html', {'cart_list':cart_list})

# Customer View list(Admin)
def all_customer(request):
    customer_list = Customer.objects.all()
    return render(request, 'admin_app/customers.html', {'customer_list':customer_list})

# Order-Placed list(Admin)
def all_orderplaced(request):
    orderplaced_list = OrderPlaced.objects.all()
    return render(request, 'admin_app/order_placed.html', {'orderplaced_list':orderplaced_list})

# Users list(Admin)
def all_users(request):
    users_list = User.objects.all()
    # print(users_list)
    return render(request, 'admin_app/users.html', {'users_list':users_list})

# Coupon List(admin)
def all_coupon(request):
    coupon_list = Coupon.objects.all()
    return render(request, 'admin_app/coupon.html', {'coupon_list':coupon_list})

# Tax list(admin)
def all_tax(request):
    tax_list = Tax.objects.all()
    return render(request, 'admin_app/tax.html', {'tax_list':tax_list})

# Color list(admin)
def all_color(request):
    color_list = Color.objects.all()
    return render(request, 'admin_app/color.html', {'color_list':color_list})

# Size list(admin)
def all_size(request):
    size_list = Size.objects.all()
    return render(request, 'admin_app/size.html', {'size_list':size_list})

# Group list(admin)
def all_group(request):
    group_list = Itemgroup.objects.all()
    return render(request, 'admin_app/group.html', {'group_list':group_list})

# Category list(admin)
def all_category(request):
    category_list = Category.objects.all()
    return render(request, 'admin_app/category.html', {'category_list':category_list})

# Purchase List(admin)
def all_purchase(request):
    purchase_list = Purchase.objects.all()
    return render(request, 'admin_app/purchase.html', {'purchase_list':purchase_list})

# Purchase product list(admin)
def all_purchase_product(request):
    purchase_product_list = PurchaseProduct.objects.all()
    return render(request, 'admin_app/purchase_products.html', {'purchase_product_list':purchase_product_list})
    

# Supplier list(admin)
def all_supplier(request):
    supplier_list = Supplier.objects.all()
    return render(request, 'admin_app/supplier.html', {'supplier_list':supplier_list})

# Hold bill(admin)
def all_hold_bills(request):
    hold_bill_list = Cart.objects.filter(hold=True)
    return render(request, 'admin_app/hold_bill_list.html', {'hold_bill_list':hold_bill_list})

# Success bill(admin)
def all_success_bills(request):
    success_bill = Cart.objects.filter(hold=False)
    return render(request, 'admin_app/success_bill_list.html', {'success_bill':success_bill})


# All Lists (staff)(manager)
# Staff view
def staff_dashboard(request):
    return render(request, 'staff/staff_home.html')

# Product View list(Staff)
def product_all(request):
    products_list = Product.objects.all()
    return render(request, 'staff/products.html', {'products_list':products_list})

# Cart View list(Staff)
def all_cart(request):
    carts_list = Cart.objects.all()
    return render(request, 'staff/carts.html', {'carts_list':carts_list})

# Customer View list(Staff)
def all_customeres(request):
    customers_list = Customer.objects.all()
    return render(request, 'staff/customers.html', {'customers_list':customers_list})

# Order-Placed list(Staff)
def all_orderplace(request):
    orderplace_list = OrderPlaced.objects.all()
    return render(request, 'staff/order_placed.html', {'orderplace_list':orderplace_list})

# Users list(Staff)
def all_user(request):
    user_list = User.objects.all()
    return render(request, 'staff/users.html', {'user_list':user_list})

# Category list(staff)
def category_all(request):
    category_list = Category.objects.all()
    return render(request, 'staff/category.html', {'category_list':category_list})

# Color list(staff)
def color_all(request):
    color_list = Color.objects.all()
    return render(request, 'staff/color.html', {'color_list':color_list})

# Size list(staff)
def size_all(request):
    size_list = Size.objects.all()
    return render(request, 'staff/size.html', {'size_list':size_list})

 # Group list(staff)
def group_all(request):
    group_list = Itemgroup.objects.all()
    return render(request, 'staff/group.html', {'group_list':group_list})

# Tax list(staff)
def tax_all(request):
    tax_list = Tax.objects.all()
    return render(request, 'staff/tax.html', {'tax_list':tax_list})

# Coupon List(staff)
def coupon_all(request):
    coupon_list = Coupon.objects.all()
    return render(request, 'staff/coupon.html', {'coupon_list':coupon_list})

# Customer View list(staff)
def customer_all(request):
    customer_list = Customer.objects.all()
    return render(request, 'staff/customers.html', {'customer_list':customer_list})

# Purchase List(staff)
def purchase_all(request):
    purchase_list = Purchase.objects.all()
    return render(request, 'staff/purchase.html', {'purchase_list':purchase_list})

# Supplier list(manager)
def supplier_all(request):
    supplier_list = Supplier.objects.all()
    return render(request, 'staff/supplier.html', {'supplier_list':supplier_list})


# Accoutant List
# Purchase List(accountant)
def purchase(request):
    purchase_list = Purchase.objects.all()
    return render(request, 'accountant_app/purchase.html', {'purchase_list':purchase_list})

# Coupon List(accountant)
def coupon(request):
    coupon_list = Coupon.objects.all()
    return render(request, 'accountant_app/coupons.html', {'coupon_list':coupon_list})

# Tax list(accountant)
def taxes(request):
    tax_list = Tax.objects.all()
    return render(request, 'accountant_app/taxes.html', {'tax_list':tax_list})

# Cashier view
def cashier_dashboard(request):
    return render(request, 'cash_counter/cashier_home.html')


# Product View list(cashier)
def all_productss(request):
    productss_list = Product.objects.all()
    return render(request, 'cash_counter/products.html', {'productss_list':productss_list})

# Admin insert
# Users insert(admin)
def user_insert(request):
    submitted = False
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_insert)
    else:
        form = CustomerRegistrationForm()
        if 'submitted' in request.GET:
            submitted =True
    return render(request, 'admin_app/userinsertform.html', {'form':form, 'submitted':submitted})


# Product insert(Admin)
def productinsert(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(productinsert)
    else:
        form = ProductForm()
        if 'submitted' in request.GET:    
            submitted = True
    return render(request, 'admin_app/productinsertform.html', {'form':form, 'submitted':submitted})

# Customer insert(Admin)
def customerinsert(request):
    if not request.user.is_superuser:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    submitted = False
    if request.method  == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(customerinsert)
    else:
        form = CustomerForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/customerinsertform.html', {'form':form, 'submitted':submitted})

# Cart insert(Admin)
def cartinsert(request):
    submitted = False
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cartinsert)
    else:
        form = CartForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/cartinsertform.html', {'form':form, 'submitted':submitted})

# Orderplaced insert(Admin)
def order_placed(request):
    submitted = False
    if request.method == "POST":
        form = OrderPlacedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order_olaced?submitted=True')
    else:
        form = OrderPlacedForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/opinsert.html', {'form':form, 'submitted':submitted})

# Group insert(Admin)
def group_insert(request):
    submitted = False
    if request.method == "POST":
        forms = ItemgroupForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect(group_insert)
    else:
        forms = ItemgroupForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/group_insert.html', {'forms':forms, 'submitted':submitted})

# Category insert(Admin)
def category_insert(request):
    submitted = False
    if request.method == "POST":
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(category_insert)
    else:
        forms = CategoryForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/category_insert.html', {'forms':forms, 'submitted':submitted})

# Purchase insert(Admin)
def purchase_insert(request):
    submitted = False
    if request.method == "POST":
        forms = PurchaseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(purchase_insert)
    else:
        forms = PurchaseForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/purchase_insert.html', {'forms':forms, 'submitted':submitted})

# Purchase Product Insert(Admin)
def purchase_product_insert(request):
    submitted = False
    if request.method == "POST":
        forms = PurchaseProductForm(request.POST)
        return redirect(purchase_product_insert)
    else:
        forms = PurchaseProductForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/purchase_product_insert.html', {'forms':forms, 'submitted':submitted})

# Coupon insert(Admin)
def coupon_insert(request):
    submitted = False
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(coupon_insert)
    else:
        form = CouponForm()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'admin_app/coupon_insert.html', {'form':form, 'submitted':submitted})

# Tax insert(Admin)
def tax_insert(request):
    submitted = False
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tax_insert)
    else:
        form = TaxForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/tax_insert.html', {'form':form, 'submitted':submitted})

# color insert(Admin)
def color_insert(request):
    submitted = False
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(color_insert)
    else:
        form = ColorForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/color_insert.html', {'form':form, 'submitted':submitted}) 

# Supplier insert(Admin)
def supplier_insert(request):
    submitted = False
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(supplier_insert)
    else:
        form = SupplierForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/supplier_insert.html', {'form':form, 'submitted':submitted})

# Size Insert(Admin)
def size_insert(request):
    submitted = False
    if request.method == "POST":
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(size_insert)
    else:
        form = SizeForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/size_insert.html', {'form':form, 'submitted':submitted})


# Manage Insert
# Product insert(manager)
def prod_insert(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(prod_insert)
    else:
        form = ProductForm()
        if 'submitted' in request.GET:    
            submitted = True
    return render(request, 'staff/productinsertform.html', {'form':form, 'submitted':submitted})

# Category insert(manager)
def insert_category(request):
    submitted = False
    if request.method == "POST":
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(insert_category)
    else:
        forms = CategoryForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/category_insert.html', {'forms':forms, 'submitted':submitted})

# color insert(manager)
def insert_color(request):
    submitted = False
    if request.method == "POST":
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_color)
    else:
        form = ColorForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/color_insert.html', {'form':form, 'submitted':submitted}) 

# Size Insert(manager)
def insert_size(request):
    submitted = False
    if request.method == "POST":
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_size)
    else:
        form = SizeForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/size_insert.html', {'form':form, 'submitted':submitted})

# Group insert(manager)
def insert_group(request):
    submitted = False
    if request.method == "POST":
        forms = ItemgroupForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect(insert_group)
    else:
        forms = ItemgroupForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/group_insert.html', {'forms':forms, 'submitted':submitted})

# Tax insert(manager)
def insert_taxes(request):
    submitted = False
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_taxes)
    else:
        form = TaxForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/tax_insert.html', {'form':form, 'submitted':submitted})

# Coupon insert(manager)
def add_coupon_insert(request):
    submitted = False
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(add_coupon_insert)
    else:
        form = CouponForm()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'staff/coupon_insert.html', {'form':form, 'submitted':submitted})

# Customer insert(manager)
def insert_customer(request):
    if not request.user.is_superuser:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    submitted = False
    if request.method  == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_customer)
    else:
        form = CustomerForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/customerinsertform.html', {'form':form, 'submitted':submitted})

# Purchase insert(Admin)
def add_purchase_insert(request):
    submitted = False
    if request.method == "POST":
        forms = PurchaseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(add_purchase_insert)
    else:
        forms = PurchaseForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/purchase_insert.html', {'forms':forms, 'submitted':submitted})

# Supplier insert(manager)
def insert_supplier(request):
    submitted = False
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_supplier)
    else:
        form = SupplierForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'staff/supplier_insert.html', {'form':form, 'submitted':submitted})



# Payment mode Insert
def payment_mode_insert(request):
    submitted = False
    if request.method == "POST":
        form = PaymentModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(bill_print)
    else:
        form = PaymentModeForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'payment_mode.html', {'form':form, 'submitted':submitted})


# Accountant insert
# Purchase insert(Accountant)
def insert_purchase(request):
    submitted = False
    if request.method == "POST":
        forms = PurchaseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(insert_purchase)
    else:
        forms = PurchaseForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'accountant_app/purchase_insert.html', {'forms':forms, 'submitted':submitted})

# Purchase Product Insert(Accountant)
def purchase_product_inserts(request):
    submitted = False
    if request.method == "POST":
        forms = PurchaseProductForm(request.POST)
        return redirect(purchase_product_inserts)
    else:
        forms = PurchaseProductForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'accountant_app/purchase_product_insert.html', {'forms':forms, 'submitted':submitted})


# Coupon insert(Accountant)
def insert_coupon(request):
    submitted = False
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_coupon)
    else:
        form = CouponForm()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'accountant_app/coupon_insert.html', {'form':form, 'submitted':submitted})

# Tax insert(accountant)
def insert_tax(request):
    submitted = False
    if request.method == "POST":
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(insert_tax)
    else:
        form = TaxForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'accountant_app/tax_insert.html', {'form':form, 'submitted':submitted})





# User Views
#Home/Product view
class ProductView(View):
    def get(self, request):
        category_group = Itemgroup.objects.all()
        category = Category.objects.all()
        product = Product.objects.all()
        return render(request, 'app/home.html', {'product':product, 
        'category_group':category_group, 'category':category
        })

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        category_group = Itemgroup.objects.all()
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product) & Q(customer__user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'category_group':category_group}) 

# search Function
def searchbar(request):
    if request.method =='GET':
        search = request.GET.get('search')
        prod = Product.objects.all().filter(title=search)
        return render(request, 'app/searchbar.html', {'prod':prod})

#add to cart
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    customer = Customer.objects.filter(user=user).first()
    Cart(customer=customer, product=product).save()
    return redirect('/cart')

#view cart
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.filter(user=user).first()
        cart = Cart.objects.filter(customer=customer)
        # print(cart)

        #calculation/no product in cart
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.customer == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')
            
# Plus cart quantity & amount
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

# Minus cart quantity & amount
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

#  Minus cart quantity & amount
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

#buy now function
def buy_now(request):
    return render(request, 'app/buynow.html')

#address view
@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

# Orders
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})

#procuct view
#mobile Cold Drinks
# def mobile(request, data=None):
#     mobiles = []
#     if data == None:
#         mobiles = Product.objects.filter(category='M')
#     elif data == 'Redmi' or data == 'Samsung' or data == 'Iphone' or data == 'Vivo' or data == 'Oppo':
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     elif data =='Below':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
#     elif data =='Above':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
#     return render(request, 'app/mobile.html', {'mobiles':mobiles})

def admin_home(request):
    return render(request, 'admin_app/admin_home.html')

def staff_home(request):
    return render(request, 'staff/staff_home.html')

def cashier_home(request):
    return render(request, 'cash_counter/cashier_home.html')

#registration page
class CustomerRegistrationFormView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations..! Registered Successfully')
        return render(request, 'app/customerregistration.html', {'form':form})    

#checkout page
@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(customer=add.first())
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = cart_items
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    customer = Customer.objects.filter(user=user).first()
    cart = Cart.objects.filter(customer=customer)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

# user profile page
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations..!! ProfileUpdated Successfully.')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

def insertdata(request):
    if request.method == 'POST':
        if request.POST.get('trans_date') and request.POST.get('supplier') and request.POST.get('bill_type') and request.POST.get('bill_no') and request.POST.get('ledger_acc') and request.POST.get('bill_date') and request.POST.get('gstin'):
            toBeSaved = Purchase()
            toBeSaved.trans_date = request.POST.get('trans_date')
            toBeSaved.supplier_name = request.POST.get('supplier')
            toBeSaved.pur_bill_no = request.POST.get('bill_no')
            toBeSaved.bill_type = request.POST.get('bill_type')
            toBeSaved.save()
            messages.success(request, "Purchase Product Data Inserted Successfully..!")
            return render(request, 'purchase_bills.html')

# Bill-page
def bill_page(request):
    return render(request, 'bills.html')

def purchase_bill(request):
    if request.method == 'POST':
        purchase = json.loads(request.POST.get('purchase'))
        purchase['supplier_name'] = Supplier.objects.get(pk=int(purchase['supplier_name']))
        purchase = Purchase(**purchase)
        purchase.save()

        products = json.loads(request.POST.get('products'))
        for product in products:
            purchaseProductduct = PurchaseProduct(**product, pur_bill_no=purchase)
            purchaseProductduct.save()
            

        return JsonResponse({'msg': 'success'})
    else:
        supplier_all = Supplier.objects.all()
        return render(request, 'purchase_bills.html', {'supplier_all':supplier_all})

def exit_bill(request):
    return render(request, 'app/home.html')

def bill_print(request):
    return render(request, 'bill_print.html')

# Hold bill(accountant)
def hold_bills(request):
    hold_bill_list = Cart.objects.filter(hold=True)
    return render(request, 'cash_counter/hold_bill_list.html', {'hold_bill_list':hold_bill_list})

# Success bill(accountant)
def success_bills(request):
    success_bill = Cart.objects.filter(hold=False)
    return render(request, 'accountant_app/success_bill_list.html', {'success_bill':success_bill})

def navbar_list(request):
    nav_list = Itemgroup.objects.all()
    return render(request, 'app/base.html', {'nav_list':nav_list})

def show_category(request):
    product = Product.objects.all()
    category_group = Itemgroup.objects.all()
    return render(request, 'app/categorydetails.html', {'category_group':category_group, 'product':product})


# Update functions(Admin)
# product Update(admin)
def update_data(request, id):
    if request.method == 'POST':
        pu = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=pu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        pu = Product.objects.get(pk=id)
        fm = ProductForm(instance=pu)
    return render(request, 'admin_app/update_product.html', {'form':fm})

# Customer Update(admin)
def update_cust(request, id):
    if request.method == 'POST':
        cu = Customer.objects.get(pk=id)
        fm = CustomerForm(request.POST, instance=cu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        cu = Customer.objects.get(pk=id)
        fm = CustomerForm(instance=cu)
    return render(request, 'admin_app/update_customer.html', {'form':fm})

# Order_Placed Update(admin)
def op_update(request, id):
    if request.method == 'POST':
        opu = OrderPlaced.objects.get(pk=id)
        fm = OrderPlacedForm(request.POST, instance=opu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        opu = OrderPlaced.objects.get(pk=id)
        fm = OrderPlacedForm(instance=opu)
    return render(request, 'admin_app/update_order_place.html', {'form':fm})

# Coupon Update(admin)
def update_coupon(request, id):
    if request.method == 'POST':
        co = Coupon.objects.get(pk=id)
        fm = CouponForm(request.POST, instance=co)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        co = Coupon.objects.get(pk=id)
        fm = CouponForm(instance=co)
    return render(request, 'admin_app/update_coupon.html', {'form':fm})

# Tax Update(admin)
def update_tax(request, id):
    if request.method == 'POST':
        tu = Tax.objects.get(pk=id)
        fm = TaxForm(request.POST, instance=tu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        tu = Tax.objects.get(pk=id)
        fm = TaxForm(instance=tu)
    return render(request, 'admin_app/update_tax.html', {'form':fm})

# Supplier Update(admin)
def supplier_update(request, id):
    if request.method == 'POST':
        opu = Supplier.objects.get(pk=id)
        fm = SupplierForm(request.POST, instance=opu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        opu = Supplier.objects.get(pk=id)
        fm = SupplierForm(instance=opu)
    return render(request, 'admin_app/update_supplier.html', {'form':fm})

# Group Update(admin)
def update_group(request, id):
    if request.method =='POST':
        gr = Itemgroup.objects.get(pk=id)
        fm = ItemgroupForm(request.POST, instance=gr)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        gr = Itemgroup.objects.get(pk=id)
        fm = ItemgroupForm(instance=gr)
    return render(request, 'admin_app/update_group.html', {'form':fm})

# Category Update(admin)
def update_category(request, id):
    if request.method == 'POST':
        cat = Category.objects.get(pk=id)
        fm = CategoryForm(request.POST, instance=cat)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        cat = Category.objects.get(pk=id)
        fm = CategoryForm(instance=cat)
    return render(request, 'admin_app/update_category.html', {'form':fm})

# Purchase Update(admin)
def update_purchase(request, id):
    if request.method == 'POST':
        p = Purchase.objects.get(pk=id)
        fm = PurchaseForm(request.POST, instance=p)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        p = Purchase.objects.get(pk=id)
        fm = PurchaseForm(instance=p)
    return render(request, 'admin_app/update_purchase.html', {'form':fm})


# Delete Function(Admin)
# Product Delete(admin)
def delete_data(request, id):
    if request.method =='POST':
        pd=Product.objects.get(pk=id)
        pd.delete()
        return HttpResponseRedirect('admin_app/products.html')

# Cart Delete(admin)
def cart_delete(request, id):
    if request.method =='POST':
        cd=Cart.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/carts.html')

# Customer Delete(admin)
def customer_delete(request, id):
    if request.method =='POST':
        cd=Customer.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/customers.html')

# Order_Placed Delete(admin)
def op_delete(request, id):
    if request.method =='POST':
        cd=OrderPlaced.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/order_placed.html')

# Users Delete(admin)
def u_delete(request, id):
    if request.method =='POST':
        cd=User.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/users.html')

# Coupon Delete(admin)
def c_delete(request, id):
    if request.method =='POST':
        cd=Coupon.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/coupon.html')

# Tax delete(delete)
def tax_delete(request, id):
    if request.method =='POST':
        tx = Tax.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/tax.html')

# Supplier Delete(admin)
def supplier_delete(request, id):
    if request.method =='POST':
        cd=Supplier.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/supplier.html')

# Group Delete
def group_delete(request, id):
    if request.method == 'POST':
        gr = Itemgroup.objects.get(pk=id)
        gr.delete()
        return render(request, 'admin_app/group.html')

# color delete
def color_delete(request, id):
    if request.method =='POST':
        tx = Color.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/color.html')

# size delete
def size_delete(request, id):
    if request.method =='POST':
        tx = Size.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/size.html')

# Category delete
def category_delete(request, id):
    if request.method == 'POST':
        tx = Category.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/category.html')

# Purchase delete
def purchase_delete(request, id):
    if request.method == 'POST':
        tx = Purchase.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/purchase.html')
