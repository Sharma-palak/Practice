from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class  Otp_Generate(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    otp = models.PositiveIntegerField(default=0)
    def __str__(self):
         return ("%s" %(self.otp))




class Category(MPTTModel):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(null=True ,blank=True)
    parent = TreeForeignKey('self',on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name


class Filters(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    def __str__(self):
         return self.name+" "+self.category.name

# class Filter_Features(models.Model):
#     name = models.CharField(max_length=200)
#     filter = models.ForeignKey(Filters,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name +" "+ self.filter.name
#




    # class Meta:
    #     unique_together=('slug','parent')
    #     verbose_name_plural = "categories"
    #
    # def __str__(self):
    #     full_path = [self.name]
    #     k = self.parent
    #
    #     while k is not None:
    #         full_path.append(k.name)
    #         k = k.parent
    #
    #     return ' -> '.join(full_path[::-1])



class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    slug =  models.SlugField(unique=True,null=True,blank=True)
    rating = models.DecimalField(max_digits=10,decimal_places=1,default=0)
    cost = models.DecimalField(max_digits=20,decimal_places=4,default=0)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,blank=True)

    image = models.ImageField(upload_to='profile_pic',default='')

    def __str__(self):
        return self.name


# def slug_generator(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug ='SLUG'
#
#
# pre_save.connect(slug_generator,sender=Product)
class Product_Detail(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=True)
    def __str__(self):
        return self.name.name
