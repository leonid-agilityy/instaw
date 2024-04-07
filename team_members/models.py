from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from django.core.validators import validate_email

import re


class Member(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=320, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)

    class Meta:
        constraints = [
            UniqueConstraint(Lower("email"), name="unique_email"),
            UniqueConstraint(Lower("phone_number"), name="unique_phone_number"),
        ]

    class Role(models.IntegerChoices):
        REGULAR = 0, _("Regular - Can't delete members")
        ADMIN = 1, _("Admin - Can delete members")

    role = models.IntegerField(
        choices=Role,
        default=Role.REGULAR,
    )

    def __str__(self):
        return self.email

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=None)

        phone = re.sub('\D', '', self.phone_number)
        if len(phone) != 10:
            raise ValidationError("Phone number should have 10 digits.")
        else:
            self.phone_number = phone

        try:
            validate_email(self.email)
        except ValidationError as e:
            raise ValidationError("Email is not formatted correctly.")

