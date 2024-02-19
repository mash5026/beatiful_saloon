from typing import Any
from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http.request import HttpRequest
from .models import Client, Service, Order, ClientType, Follow
from admin_reports import Report, register

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


class FollowInline(admin.TabularInline):
    model = Follow
    extra = 0


@admin.register(ClientType)
class ClientTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    list_filter = ('type_name',)
    search_fields = ('type_name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','family','natinlacode', 'province', 'city', 'mobile', 'gender', 'job' ,'image', 'client_type', 'created_at_persian', 'created_at_miladi', 'updated_at_miladi', 'instagram_id')
    list_filter = ('province', 'city', 'gender', 'client_type')
    search_fields = ('family','natinlacode', 'mobile')
    inlines = (OrderInline, FollowInline)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name','amount')
    list_filter = ('service_name',)
    search_fields = ('service_name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.service_name=='service_name':
            kwargs['queryset'] = Service.objects.all()
            kwargs['widget'] = forms.Select(attrs={"onChange": "getAmount(this.value)"})
        elif db_field.name == 'amount':
            kwargs['queryset'] = Service.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'order_date_persian')
    list_filter = ('client', 'service')
    search_fields = ('client__natinlacode', 'service__service_name', 'client__name', 'client__family')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'follow_date_persian')
    list_filter = ('client', 'service')
    search_fields = ('client__natinlacode', 'service__service_name', 'client__name', 'client__family')


@register()
class MyReport(Report):
    def aggregate(self, **kwargs):
        return Client.objects.filter(client_type='Treated').values('name','family','natinlacode', 'province', 'city', 'mobile', 'gender', 'image', 'client_type', 'created_at_persian', 'created_at_miladi', 'updated_at_miladi', 'instagram_id')