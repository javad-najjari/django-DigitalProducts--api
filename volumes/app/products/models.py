from django.db import models



class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(verbose_name='description', blank=True)
    avatar = models.ImageField(verbose_name='avatar', blank=True, upload_to='categories')
    is_enable = models.BooleanField(verbose_name='is enable', default=True)
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='updated time', auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name='title', max_length=50)
    description = models.TextField(verbose_name='description', blank=True)
    avatar = models.ImageField(verbose_name='avatar', blank=True, upload_to='products/')
    is_enable = models.BooleanField(verbose_name='is enable', default=True)
    categories = models.ManyToManyField('Category', verbose_name='categories', blank=True)
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPE = (
        (FILE_AUDIO, 'audio'),
        (FILE_VIDEO, 'video'),
        (FILE_PDF, 'pdf'),
    )
    product = models.ForeignKey('Product', verbose_name='product', related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=50)
    file_type = models.PositiveSmallIntegerField(verbose_name='file type', choices=FILE_TYPE)
    file = models.FileField(verbose_name='file', upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(verbose_name='is enable', default=True)
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='updated time', auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'
    
    def __str__(self):
        return self.title

