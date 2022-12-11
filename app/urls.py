from django.conf import settings
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from . import api



urlpatterns = [
    
    path('', views.home, name="home"), 
    path('dologin/', views.login, name='dologin'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('product\\-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart), 
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('show_category', views.show_category, name='show-category'),  

    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),   
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('registration/', views.CustomerRegistrationFormView.as_view(), name='customerregistration'),

    path('payment/', views.payment_mode_insert, name='payment-mode'), 

    # for admin
    path('admin-home/', views.admin_home, name="admin-home"),
    path('dashboard', views.dashboard, name="dashboard"),

    path('products', views.all_products, name="list-products"),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='update_data'),

    path('carts', views.all_carts, name="list-carts"),
    path('deletes/<int:id>/', views.cart_delete, name="deletesdata"),  

    path('customers', views.all_customer, name="list-customers"),
    path('cudelete/<int:id>/', views.customer_delete, name="customer-delete"), 
    path('update/<int:id>/', views.update_cust, name= "customer-update"), 

    path('order-placed', views.all_orderplaced, name="list-order_placed"),
    path('opdelete/<int:id>/', views.op_delete, name="op-delete"), 
    path('opupdate/<int:id>/', views.op_update, name='op-update'), 

    path('users', views.all_users, name="list-users"),
    path('udelete/<int:id>/', views.u_delete, name="u-delete"),
    path('user_update/<int:id>/', views.update_cust, name="user-update"),  

    path('coupons', views.all_coupon, name="list-coupons"),
    path('coupondelete/<int:id>/', views.c_delete, name="coupon-delete"), 
    path('updatecoup/<int:id>/', views.update_coupon, name="coupon-update"),

    path('taxes', views.all_tax, name="list-tax"),
    path('taxdelete/<int:id>', views.tax_delete, name="tax-delete"),
    path('updatetax/<int:id>/', views.update_tax, name="update-tax"),    

    path('colors', views.all_color, name="list-color"), 
    path('colordelete/<int:id>/', views.color_delete, name="color-delete"), 

    path('sizes', views.all_size, name="list-size"),
    path('sizedalate/<int:id>/', views.size_delete, name="size-delete"),

    path('itemgroup', views.all_group, name="list-group"), 
    path('groupdelete/<int:id>/', views.group_delete, name="group-delete"), 
    path('updategroup/<int:id>/', views.update_group, name="update-group"), 

    path('category', views.all_category, name="list-category"), 
    path('categorydelete/<int:id>/', views.category_delete, name='category-delete'), 
    path('updatecategory/<int:id>/', views.update_category, name="update-category"), 

    path('purchase', views.all_purchase, name="list-purchase"), 
    path('purchasedelete/<int:id>/', views.purchase_delete, name='purchase-delete'), 
    path('updatepurchase/<int:id>/', views.update_purchase, name="update-purchase"),

    path('purchase_product', views.all_purchase_product, name='list-purchase-product'),  

    path('supplier', views.all_supplier, name="list-supplier"),
    path('supplierdelete/<int:id>/', views.supplier_delete, name="supplier-delete"), 
    path('supplierupdate/<int:id>/', views.supplier_update, name='supplier-update'), 

    
    path('success_bill', views.all_success_bills, name='all-success-bill'), 
    path('holded_bill', views.all_hold_bills, name="all-hold-boll"), 
    path('bills', views.bill_page, name="list-bills"), 
    path('purchase_bill', views.purchase_bill, name='bill-purchase'), 
    path('add-product', views.productinsert, name="P-insert"),
    path('add-customer', views.customerinsert, name="Cu-insert"),
    path('add-cart', views.cartinsert, name="Ca-insert"),
    path('add-users', views.user_insert, name="U-insert"),
    path('add-coupon', views.coupon_insert, name="co-insert"),
    path('add-tax', views.tax_insert, name="tax-insert"),
    path('add-color', views.color_insert, name="color-insert"),
    path('add-supplier', views.supplier_insert, name="supplier-insert"),
    path('add-size', views.size_insert, name="size-insert"), 
    path('add-group', views.group_insert, name="g-insert"),
    path('add-category', views.category_insert, name='cat-insert'),  
    path('add-purchase', views.purchase_insert, name='purchase-insert'),
    path('add-purchase_product', views.purchase_product_insert, name='pur_pro_ins'), 
    

    # for staff
    path('staff-home/', views.staff_home, name= "staff-home"),
    path('staff_dashboard', views.staff_dashboard, name="staff_dashboard"),
    path('prod', views.product_all, name='all-prod-list'),
    path('categories', views.category_all, name="category_all"),
    path('color_s', views.color_all, name="all-color-list"),
    path('size', views.size_all, name="size-all"),  
    path('groups', views.group_all, name="all-group-list"),
    path('tax', views.tax_all, name="all-tax-list"), 
    path('coupon_s', views.coupon_all, name="all-coupon-list"),
    path('customer', views.customer_all, name="all-customer-list"), 
    path('purchases', views.purchase_all, name="all-purchase-list"),
    path('suppliers', views.supplier_all, name="all-suppliar-list"), 

# Staff Insert
    path('prod_insert', views.prod_insert, name='insert-prod'), 
    path('category_insert', views.insert_category, name="insert-category"), 
    path('color_insert', views.insert_color, name="insert-color"), 
    path('size_insert', views.insert_size, name="insert-size"), 
    path('group_insert', views.insert_group, name="insert-group"),
    path('tax_insert', views.insert_taxes, name="taxes-insert"),
    path('coupon_insert', views.add_coupon_insert, name="coupon-insert"),
    path('customer_insert', views.insert_customer, name="insert-customer"), 
    path('insert_purchase', views.add_purchase_insert, name="add-purchase-insert"),  
    path('supplier_insert', views.insert_supplier, name="insert-supplier"),  


    path('bills', views.bill_page, name="list-bills"),


    # for Accountant
    path('tax', views.taxes, name='tax-list'), 
    path('coupon', views.coupon, name='coupon-list'), 
    path('purchases', views.purchase, name='purchgase-list'), 
    path('succ_bill', views.success_bills, name='success_bill'), 
    path('hold_bill', views.hold_bills, name="hold_bill"), 

    path('tax-add', views.insert_tax, name="insert-tax"),
    path('coupon-add', views.insert_coupon, name="insert-coupon"),
    path('purchase-add', views.insert_purchase, name='insert-purchase'), 




    # for cashier
    path('cashier-home/', views.cashier_home, name="cashier-home"),
    path('productss', views.all_productss, name="list-productss"),
    path('bills', views.bill_page, name="list-bills"),

    path('exit', views.exit_bill, name='exit_bill'),
    
    path('demo', views.bill_print, name="demo"),  


    # path('api/', include(router.urls)),
    path('api/product', api.filter_product),
    path('api/customer', api.filter_customer),
    path('api/bill', api.save_bill),
    path('api/taxes', api.taxes),
    path('api/check_coupon', api.check_coupon),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
