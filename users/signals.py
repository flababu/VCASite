from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
#from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, CustomUser, AuditEntry, Parent, Teacher

@receiver(post_save, sender = CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    time = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_in', ip=ip, username=user.username, time=time)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    time = request.META.get('REMOTE_ADDR')
    AuditEntry.objects.create(action='user_logged_out', ip=ip, username=user.username, time=time)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    AuditEntry.objects.create(action='user_login_failed', username=credentials.get('username', None))

@receiver(post_save, sender = CustomUser)
def create_parent(sender, instance, created, **kwargs):
    if created:
        parent = Parent(user=instance)
        parent.save()

# @receiver(post_save, sender=CustomUser)
# def save_parent(sender, instance, **kwargs):
#     instance.parent.save()

@receiver(post_save, sender = CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created:
        teacher = Teacher(user=instance)
        teacher.save()

# @receiver(post_save, sender=CustomUser)
# def save_teacher(sender, instance, **kwargs):
#     instance.teacher.save()
