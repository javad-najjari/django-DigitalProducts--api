from django.db import models
from utils.validators import validate_sku



# مدل ایجاد اشتراک ها
class Package(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    sku = models.CharField(verbose_name='stock keeping unit', max_length=20, validators=[validate_sku])
    description = models.TextField(verbose_name='description', blank=True)
    avatar = models.ImageField(verbose_name='avater', blank=True, upload_to='packages/')
    is_enable = models.BooleanField(verbose_name='is enable', default=True)
    price = models.PositiveIntegerField(verbose_name='price')
    duration = models.DurationField(verbose_name='duration', blank=True, null=True)
    gateways = models.ManyToManyField('payments.Gateway')
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='updated time', auto_now=True)

    class Meta:
        db_table = 'packages'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
    
    def __str__(self):
        return self.title
    


class Subscription(models.Model):
    user = models.ForeignKey('users.User', related_name='%(class)s', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='%(class)s', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    expire_time = models.DateTimeField(verbose_name='expire time', blank=True, null=True)

    class Meta:
        db_table = 'subscriptions'
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


