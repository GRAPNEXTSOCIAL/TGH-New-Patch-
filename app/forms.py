from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.forms import ModelForm
from .models import *


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pleade Enter the Username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Password'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Password Again'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Email'}))
    
    class Meta:
        model = User
        fields = ['username', 
        'email', 
        'password1', 
        'password2', 
        'staff_category'
        ]
        labels = {'email':'Email'}
        Widgets = {'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Username'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Please Enter the Username'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete": "current-password", 'class':'form-control', 'placeholder':'Please Enter the Password'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'autofocus':True,  
    'class':'form-control', 'placeholder':'Please Enter the Old Password'}))
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password Again'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs=
    {'autocomplete': 'email', 'class':'form-control', 'placeholder':'Please Enter the Email'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control', 'placeholder':'Please Enter the New Password Again'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
        ]
        widgets = {'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Name'}), 
                   'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Locality'}), 
                   'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the City'}), 
                   'zipcode':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Zipcode'}),
                   'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Please Enter the State'})
                }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'supplier', 
            'manufacturer',        
            'group',
            'category', 
            'brand', 
            'item_type',
            'barcode', 
            'title', 
            'hsn_no', 
            'item_size', 
            'item_color',
            'color_name',  
            'actual_mrp', 
            'purchase_price', 
            'selling_price', 
            'discounted_price',
            'tax_on', 
            'gst', 
            'purchase_tax_type',  
            'purchase_tax',
            'cess',  
            'selling_tax', 
            'product_purchase_date',
            'manufacture_date',  
            'expiry_date', 
            'alertment_date',
            'description', 
            'product_image'
        ]
        widgets = {
            'supplier' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'manufacturer' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Manufacturer'}), 
            'group' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'category' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'brand' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Brand Name'}), 
            'item_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Item Type'}),
            'barcode' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Barcode'}), 
            'title' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Product Name'}), 
            'hsn_no' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter the HSN_NO'}), 
            'item_size' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'item_color' :forms.Select(attrs={'class':'form-control form-control-color', 'placeholder':'Select'}), 
            'color_name' :forms.Select(attrs={'class':'form-control', 'placeholder':'Please Enter the Color_Name'}), 
            'purchase_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Purchase Price'}), 
            'actual_mrp' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Actual Mrp Rs.'}), 
            'selling_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Selling Price'}),
            'discounted_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Discounted Price'}),  
            'tax_on' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Tax_on'}), 
            'gst' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Gst'}), 
            'purchase_tax_type' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'purchase_tax' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Purchase Tax'}), 
            'cess' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter The Cess %'}), 
            'selling_tax' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Selling Tax'}), 
            'product_purchase_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'manufacture_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'expiry_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'alertment_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
            'description' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Description'}), 
            'product_image' :forms.ClearableFileInput(attrs={'class':'form-control'}), 
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'mobile_no', 
            'user', 
            'name', 
            'email', 
            'locality', 
            'city', 
            'zipcode', 
            'state'
        ]
        Widgets = {
            'mobile_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Mobile No'}), 
            'user' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Username'}), 
            'name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Fullname'}), 
            'email' :forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Email'}), 
            'locality' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Locality'}), 
            'city' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the City'}), 
            'zipcode' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Zipcode'}), 
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Select'})
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields =[
            'product', 
            'pimage'
        ]
        widgets = {
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'pimage' :forms.FileInput(attrs={'class':'form-control'})
        }

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = [
            'cart_id', 
            'customer', 
            'product', 
            'quantity'
        ]
        Widgets = {
            'cart_id' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Id No'}),
            'customer' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}),
            'quantity' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Quantity'})
        }

class OrderPlacedForm(ModelForm):
    class Meta:
        model = OrderPlaced
        fields = [
            'user', 
            'customer', 
            'product', 
            'quantity', 
            'order_date', 
            'status'
        ]
        widgets = {
            'user' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'customer' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'product' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'quantity' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Quantity'}), 
            'order_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'status' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'})
        }

class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = [
            'code', 
            'valid_from', 
            'valid_to', 
            'discount', 
            'active'
        ]                                   
        input_type = 'date'                                                                                                                                                                                                                                                                                                                                                                                                                        
        Widgets ={
            'code' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the CouponCode'}), 
            'valid_from' :forms.DateInput(attrs={'class':'form-control', 'type':'date', 'placeholder':'YYYY-MM-DD'}), 
            'valid_to' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}), 
            'discount' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Discount Value'}), 
            'active' :forms.CheckboxInput(attrs={'class':'form-control'})
        }

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields = [
            'tax_type', 
            'value'
        ]
        Widgets ={
            'tax_type' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Tax Type'}), 
            'value' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Tax Value in %'})
        }

class ColorForm(ModelForm):
    class Meta:    
        model = Color
        fields = [
            'color_code',
            'color_name',  
            'item_color'
        ]
        widgets = {
            'color_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Color Code'}), 
            'color_name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Color-Name'}), 
            'item_color' :forms.TextInput(attrs={'class':'form-control form-control-color', 'placeholder':'Please Enter the Color'})
        }

class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = [
            'size_code', 
            'item_size'
        ]
        Widgets = {
            'size_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Size Code'}), 
            'item_size' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Size'})
        }
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'supplier_code', 
            'supplier', 
            'address', 
            'contact_no', 
            'supplier_email', 
            'gstin_no', 
            'state', 
            'pin'
        ]
        widgets = {
            'supplier_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Supplier Code'}), 
            'supplier' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Name'}), 
            'address' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Sup. Address'}), 
            'contact_no' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Contact No'}), 
            'supplier_email' :forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Supplier Email'}), 
            'gstin_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the GSTIN No'}), 
            'state' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'pin' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Pincode'})
        }

class ItemgroupForm(ModelForm):
    class Meta:
        model = Itemgroup
        fields = [
            'item_group_code', 
            'item_group_name', 
            'item_group_description', 
            'item_group_image'
        ]
        widgets = {
            'item_group_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Code'}), 
            'item_group_name' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Name'}), 
            'item_group_description' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Group Description'}),
            'item_group_image' :forms.ClearableFileInput(attrs={'class':'form-control'}), 
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'item_group_name', 
            'category_code', 
            'category'
        ]
        widgets = {
           'item_group_name' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
           'category_code' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Category Code'}), 
           'category' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Category Name'}), 
        }

class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = [
            'trans_date', 
            'gstin', 
            'pur_bill_no', 
            'bill_type', 
            'supplier_name', 
            'total_qty', 
            'gross_amt', 
            'disc_amt', 
            'gst_amt', 
            'tcs', 
            'o_charge', 
            'o_disc', 
            'grand_total'
        ]
        widgets = {
            'trans_date' :forms.DateInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}),
            'gstin' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter the Gstin no'}), 
            'pur_bill_no' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Bill No'}), 
            'bill_type' :forms.Select(attrs={'class':'form-control', 'placeholder':'Slect'}), 
            'supplier_name' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'total_qty' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'gross_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Gross Amount'}), 
            'disc_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discounted Amount'}), 
            'gst_amt' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The GST Amount'}), 
            'tcs' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The TCS Amount'}), 
            'o_charge' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Overall Charge'}), 
            'o_disc' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Overall Discount'}), 
            'grand_total' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Grand Total'})
        }

class PurchaseProductForm(ModelForm):
    class Meta:
        model = PurchaseProduct
        fields = [
            'pur_bill_no', 
            'barcode', 
            'product_description', 
            'article_no', 
            'size', 
            'qty', 
            'free', 
            'p_price', 
            'mrp', 
            'tax', 
            'disc1', 
            'd_Amt1', 
            'disc2', 
            'd_Amt2', 
            'l_Cost', 
            'tot_Cost', 
            's_Price', 
            'total', 
            'marg'
        ]
    widgets = {
            'pur_bill_no' :forms.Select(attrs={'class':'form-control', 'placeholder':'Select'}), 
            'barcode' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Barcode'}), 
            'product_description' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Product_Description'}), 
            'article_no' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Article No'}), 
            'size' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Size'}), 
            'qty' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Quantity'}), 
            'free' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Please Enter The Free Amount'}), 
            'p_price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Product Price'}), 
            'mrp' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Mrp'}), 
            'tax' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Tax'}), 
            'disc1' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discount1 in %'}), 
            'd_Amt1' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discoun Amount1'}), 
            'disc2' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discount2 in %'}), 
            'd_Amt2' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Discount Amount2 in %'}), 
            'l_Cost' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The L_Cost'}), 
            'tot_Cost' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Cost'}), 
            's_Price' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Selling Price'}), 
            'total' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Price'}), 
            'marg' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Margine in %'})   
    }

class PaymentModeForm(ModelForm):
    class Meta:
        model = PaymentMode
        fields = [
            'by_cash', 
            'by_card', 
            'by_credit', 
            'sdx_fin', 
            'by_upi'
        ]

        widgets = {
            'By_Cash' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'By_Card' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'By_Credit' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'Sdx_Fin' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'}), 
            'By_UPI' :forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Please Enter The Total Quantity'})
        }

