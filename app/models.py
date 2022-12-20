from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, date
from colorfield.fields import ColorField
from django.utils.safestring import mark_safe


MANAGER='MANAGER'
CASHIER='CASHIER'
ACCOUNTANT = 'ACCOUNTANT'

STATE_CHOICES = ( 
    ('Andhra Pradesh', 'Andhra Pradesh'), 
    ('Arunachal Pradesh', 'Arunachal Pradesh'), 
    ('Bihar', 'Bihar'), 
    ('Chhattisgarh', 'Chhattisgarh'), 
    ('Goa', 'Goa'), 
    ('Gujurat', 'Gujurat'), 
    ('Haryana', 'Haryana'), 
    ('Himachal Pradesh', 'Himachal Pradesh'), 
    ('Jharkhand', 'Jharkhand'), 
    ('Karnataka', 'Karnataka'), 
    ('Kerala', 'Kerala'), 
    ('Assam', 'Assam'), 
    ('Madhya Pradesh', 'Madhya Pradesh'), 
    ('Maharashtra', 'Maharashtra'), 
    ('Manipur', 'Manipur'), 
    ('Meghalaya', 'Meghalaya'), 
    ('Mizoram', 'Mizoram'), 
    ('Nagaland', 'Nagaland'), 
    ('Odisha', 'Odisha'), 
    ('Punjab', 'Punjab'), 
    ('Rajasthan', 'Rajasthan'), 
    ('Sikkim', 'Sikkim'), 
    ('Tamil Nadu', 'Tamil Nadu'), 
    ('Telangana', 'Telangana'), 
    ('Tripura', 'Tripura'), 
    ('Uttarakhand', 'Uttarakhand'), 
    ('Uttar Pradesh', 'Uttar Pradesh'), 
    ('West Bengal', 'West Benga'), 
)

STAFF_CATEGORY_CHOICES = (
    (MANAGER, 'Manager'),
    (CASHIER, 'Cashier'), 
    (ACCOUNTANT, 'Accountant')
)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'), 
    ('Packed', 'Packed'), 
    ('On The Way', 'On The Way'), 
    ('Delivered', 'Delivered'), 
    ('Cancel', 'Cancel')
)

TAX_TYPE_CHOICES = (
    ('CGST/SGST', 'CGST/SGST'), 
    ('CGST', 'CGST'), 
    ('SGST', 'SGST'), 
    ('IGST', 'IGST'), 
    ('UNREGD', 'UNREGD'), 
    ('COMPOSITE', 'COMPOSITE')
)

class Color(models.Model):
    color_code = models.CharField(max_length=5)
    item_color = ColorField()

    def __str__(self) -> str:
        return self.item_color

    def color_tag(self):
        if self.item_color is not None:
            return mark_safe('<div style="height: 30px; width: 40px; background-color: %s"></div>'%(self.item_color))

class Size(models.Model):
    size_code = models.CharField(max_length=5)
    item_size = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.item_size


class Supplier(models.Model):
    supplier_code = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=50)
    supplier_email = models.EmailField(null=True)
    gstin_no = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)
    pin = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.supplier

class User(AbstractUser):
    staff_category = models.CharField(choices=STAFF_CATEGORY_CHOICES, max_length=100)

class Customer(models.Model):
    mobile_no = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    state = models.CharField(choices=STATE_CHOICES, max_length=50, null=True)

    def __str__(self):
        return str(self.user)

class Itemgroup(models.Model):
    item_group_code = models.IntegerField()
    item_group_name = models.CharField(max_length=50)
    item_group_description = models.CharField(max_length=200)
    item_group_image = models.ImageField(upload_to='group_img')

    def __str__(self) -> str:
        return self.item_group_name
        

class Category(models.Model):
    item_group_name = models.ForeignKey(Itemgroup, on_delete=models.CASCADE, null=True)
    category_code = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    manufacturer = models.TextField()
    group = models.ForeignKey(Itemgroup, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=100)
    item_type = models.TextField()
    barcode = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    hsn_no = models.CharField(max_length=100)   
    item_size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    item_color = ColorField()    
    actual_mrp = models.FloatField()
    purchase_price = models.FloatField()
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    tax_on = models.CharField(max_length=50, default='BASIC')
    gst = models.FloatField()
    purchase_tax_type = models.CharField(choices=TAX_TYPE_CHOICES, max_length=50, null=True)
    purchase_tax = models.FloatField()
    cess = models.FloatField(null=True, default=0.0)
    selling_tax = models.FloatField()  
    product_purchase_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    manufacture_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    expiry_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    alertment_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    description = models.TextField()
    product_image = models.ImageField(upload_to='productimg')

    def color_tag(self):
        if self.item_color is not None:
            return mark_safe('<div style="height: 30px; width: 40px; background-color: %s"></div>'%(self.item_color))



class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pimage = models.ImageField(upload_to='productimage')

    def __str__(self):
        return str(self.id)

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    offer_applied = models.ForeignKey(Coupon, null=True, on_delete=models.CASCADE)
    hold = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateField(auto_now_add=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Tax(models.Model):
    tax_type = models.CharField(max_length=10, unique=True)
    value = models.FloatField()

class Purchase(models.Model):
    trans_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    gstin = models.CharField(max_length=100)
    pur_bill_no = models.CharField(max_length=50)
    bill_type = models.CharField(choices=TAX_TYPE_CHOICES, max_length=50)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    total_qty = models.IntegerField()
    gross_amt = models.FloatField()
    disc_amt = models.FloatField()
    gst_amt = models.FloatField()
    tcs = models.FloatField()
    o_charge = models.FloatField()
    o_disc = models.FloatField()
    grand_total = models.FloatField()

    def __str__(self) -> str:
        return self.pur_bill_no

class PurchaseProduct(models.Model):
    pur_bill_no = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100)
    product_description = models.CharField(max_length=250)
    article_no = models.IntegerField(null=True, default=0)
    hsn_no = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    qty = models.IntegerField(null=True)
    free = models.FloatField(null=True, default=0)
    p_price = models.FloatField(null=True)
    mrp = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    cess = models.FloatField(null=True)
    disc1 = models.FloatField(null=True, default=0)
    d_Amt1 = models.FloatField(null=True, default=0)
    disc2 = models.FloatField(null=True, default=0)
    d_Amt2 = models.FloatField(null=True, default=0)
    l_Cost = models.FloatField(null=True)
    tot_Cost = models.FloatField(null=True)
    s_Price = models.FloatField(null=True)
    total = models.FloatField(null=True)
    marg = models.FloatField(null=True)

class SalesRegister(models.Model):
    inv_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    inv_no = models.CharField(max_length=100)
    total_qty = models.FloatField(null=True)
    total_amt = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    gst_amt = models.FloatField(null=True)
    grand_total = models.FloatField(null=True)
    by_cash = models.FloatField(null=True, default=0.00)
    by_card = models.FloatField(null=True, default=0.00)
    by_credit = models.FloatField(null=True, default=0.00)
    sdx_fin = models.FloatField(null=True, default=0.00)
    by_upi = models.FloatField(null=True, default=0.00)
    redeem = models.FloatField(null=True, default=0.00)
    ct_amt = models.FloatField(null=True, default=0.00)
    refund = models.FloatField(null=True, default=0.00)

class PaymentMode(models.Model):
    by_cash = models.FloatField(null=True, default=0)
    by_card = models.FloatField(null=True, default=0)
    by_credit = models.FloatField(null=True, default=0)
    sdx_fin = models.FloatField(null=True, default=0)
    by_upi = models.FloatField(null=True, default=0)