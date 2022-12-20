from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = [
        'username', 
        'first_name', 
        'staff_category'
    ]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Staff Category"), {"fields": ("staff_category",)}),
    )

@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'color_code',
        'item_color',  
        'color_tag'
    ]

@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'size_code', 
        'item_size'
    ]
@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'supplier_code', 
        'supplier', 
        'address', 
        'contact_no', 
        'supplier_email', 
        'gstin_no', 
        'state', 
        'pin'
    ]

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'mobile_no', 
        'user', 
        'name', 
        'email', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
    ]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'supplier',
        'manufacturer',
        'group',
        'category',
        'brand', 
        'item_type',  
        'title', 
        'barcode',
        'hsn_no',  
        'item_size',
        'item_color',  
        'color_tag',
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

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'product', 
        'pimage'
    ]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'customer', 
        'product', 
        'quantity'
    ]

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'user', 
        'customer', 
        'product', 
        'quantity', 
        'order_date', 
        'status'
    ]

@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = [
        'code', 
        'valid_from', 
        'valid_to', 
        'discount', 
        'active'
    ]
    list_filter = [
        'active', 
        'valid_from', 
        'valid_to'
    ]
    search_fields = ['code']

@admin.register(Tax)
class TaxModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'tax_type', 
        'value'
    ]

@admin.register(Itemgroup)
class ItemgroupModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'item_group_code', 
        'item_group_name', 
        'item_group_description', 
        'item_group_image'
    ]

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'item_group_name', 
        'category_code', 
        'category'
    ]

@admin.register(Purchase)
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'trans_date', 
        'pur_bill_no', 
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

@admin.register(PurchaseProduct)
class PurchaseProductModelAdmin(admin.ModelAdmin):
    list_display = [
            'id', 
            'pur_bill_no', 
            'barcode', 
            'product_description', 
            'article_no', 
            'hsn_no', 
            'size', 
            'qty', 
            'free', 
            'p_price', 
            'mrp', 
            'tax',
            'cess',  
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

@admin.register(SalesRegister)
class SalesRegisterModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'inv_no', 
        'total_qty', 
        'total_amt', 
        'discount', 
        'gst_amt', 
        'grand_total', 
        'by_cash', 
        'by_card', 
        'by_credit', 
        'sdx_fin', 
        'by_upi', 
        'redeem', 
        'ct_amt', 
        'refund'
    ]

@admin.register(PaymentMode)
class PaymentModeModelAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'by_cash', 
        'by_card', 
        'by_credit', 
        'sdx_fin', 
        'by_upi'
    ]
