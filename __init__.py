from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.sites.models import Site

@receiver(pre_save, sender=Site)
def site_save_handler(sender, **kwargs):
    print "Sites are being saved"