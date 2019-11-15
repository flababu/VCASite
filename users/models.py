from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator
import datetime


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 100, blank=True, null = True)
    first_name = models.CharField(max_length = 100, default = '')
    last_name = models.CharField(max_length = 100, default = '')
    middle_name = models.CharField(max_length = 100, null = True)
    birth_date = models.DateField(null = True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    last_login = models.DateTimeField('last_login', auto_now_add=True,  null=True)
    is_teacher = models.BooleanField('teacher', default=False)
    is_parent = models.BooleanField('parent', default=False)
    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('admin status', default=False)
    is_active = models.BooleanField('active status', default=True)

    def __str__(self):
        if self.first_name == '' and self.last_name == '':
            return '{}'.format(self.username)
        else:
            return '{}, {} - {}'.format(self.last_name, self.first_name, self.username)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, limit_choices_to={'is_parent':True},)
    date_added = models.DateField('date added', auto_now_add=True)
    id_code = models.AutoField(primary_key = True, validators=[MinLengthValidator(4), MaxLengthValidator(4)])


    def save(self):
        super().save()

        # img = Image.open(self.image.path)
        #
        # if img.height > 600 or img.width > 600:
        #     output_size = (600,600)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    # @property
    # def create_id(self):
    #     now = datetime.datetime.now()
    #     id_code = self.id_code
    #     return str("2")+str(now.year)+str(now.month)+str(now.day)+str(id_code)[:14]


    #    def get_serial_number(self):
        #    "Get formatted value of serial number"
    #        return "%.2d-%.3d" % (self.code, self.product)

    #    def increment_id():
    #        top = Parent.objects.order_by('-parent_number')[0]
#
    #        if date.today() > self.top.date_added
    #            id = id+1
    #        else

    #def save(self):
     # "Get last value of Code and Number from database, and increment before save"
     # top = Parent.objects.order_by('-parent_number')[0]
     # self.parent_number = top.parent_number + 1
     # super(Parent, self).save()


    # parent_number = models.CharField(default=create_id, editable=False, max_length = 13, validators=[MinLengthValidator(13), MaxLengthValidator(13)])

    def __str__(self):
        return '{}'.format(self.user)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, limit_choices_to={'is_teacher':True},)
    date_added = models.DateField('date added', auto_now_add=True)
    id_code = models.AutoField(primary_key = True, validators=[MinLengthValidator(4), MaxLengthValidator(4)])

    def save(self):
        super().save()


    def __str__(self):
        return '{}'.format(self.user)


class AuditEntry(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    username = models.CharField(max_length=256, null=True)
    time = models.DateTimeField('time', auto_now_add=True,  null=True)

    class Meta:
        verbose_name_plural = "Audit Entries"
        app_label = 'admin'
        db_table = 'users_auditentry'

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)
