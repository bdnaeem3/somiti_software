# from django.db.models.signals import post_save
# from .models import Savings
# from django.dispatch import receiver
# from reference.models import Reference


# @receiver(post_save, sender=Savings)
# def create_reference(sender, instance, created, **kwargs):
#     if created:
#         Reference.objects.create(savings=instance)


# @receiver(post_save, sender=Savings)
# def save_reference(sender, instance, **kwargs):
#     instance.reference.save()
