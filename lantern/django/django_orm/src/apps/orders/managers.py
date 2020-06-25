from django.db import models


class OrderQuerySet(models.QuerySet):
    def expected(self):
        return self.filter(status='expected')

    def verified(self):
        return self.filter(status='verified')

    def paid_out(self):
        return self.filter(status='paid_out')
