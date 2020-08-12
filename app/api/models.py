from django.db import models
from django.utils.translation import gettext_lazy as _


class Data(models.Model):
    url = models.CharField(verbose_name=_("Url"), max_length=180, blank=False, null=False)
    processed = models.BooleanField(verbose_name=_("Processed"), default=False, db_index=True)
    error = models.CharField(verbose_name=_("Error"), max_length=180, default='')
    keys = models.JSONField(verbose_name=_("Keys"), default=list)

    def update_keys(self, keys=None, error=''):
        if not keys:
            keys = list()
        if not self.processed:
            self.processed = True
            self.keys = keys
            self.error = error
            self.save()

    def __str__(self):
        return f'{self.pk} - {self.processed}'

    class Meta:
        verbose_name = _("Data")
        verbose_name_plural = _("Data")
