from django.apps import AppConfig


class MembersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "members"

class VoucherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  
    name="voucher"
