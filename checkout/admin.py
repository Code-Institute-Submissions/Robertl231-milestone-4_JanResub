from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'sub_total', 'original_bag', 'stripe_pid')

    field = ('order_number', 'user_profile', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2', 'country', 'delivery_cost', 'order_total', 'sub_total', 'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost', 'sub_total', )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
