from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
from .utils import path_client,LIST_STATUS,OFFICIAL, validat_image, CHOICES_LIST, LIST_ANSWER, ON_GOING
import jdatetime


class ClientType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.service_name

class Client(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    natinlacode = models.CharField(max_length=10)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12)
    gender = models.CharField(max_length=5, choices=CHOICES_LIST)
    job = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to =path_client, validators=[validat_image])
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    created_at_persian = jmodels.jDateTimeField(auto_now_add=True, null=True, blank=True )
    updated_at_persian = jmodels.jDateTimeField(auto_now=True, null=True, blank=True )
    created_at_miladi = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    updated_at_miladi = models.DateTimeField(auto_now=True, null=True, blank=True )
    instagram_id = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    order_date_persian = jmodels.jDateTimeField(default=jdatetime.datetime.now)
    is_treatment_complete = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.client.name} - {self.client.family} - {self.service.service_name} - {self.order_date_persian}'
    
    def save(self, *args, **kwargs):
        if not self.client.order_set.exists():
            type_client = ClientType.objects.filter(type_name='Treated')[0]
            self.client.client_type = type_client
            self.client.save()        
        if self.order_date_persian:
            self.order_date = jdatetime.datetime.togregorian(self.order_date_persian)
        super().save(*args, **kwargs)


class Follow(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    follow_date = models.DateTimeField(default=timezone.now)
    follow_date_persian = jmodels.jDateTimeField(default=jdatetime.datetime.now)
    status = models.CharField(max_length=10,choices=LIST_ANSWER, default=ON_GOING)

    def __str__(self):
        return f'{self.client.name} - {self.client.family} - {self.service.service_name} - {self.follow_date_persian}'