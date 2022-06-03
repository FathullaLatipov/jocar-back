from django.db import models


class CarModel(models.Model):
    model = models.CharField(max_length=99, null=True)
    image = models.FileField(upload_to='cars_image', null=True)
    volume = models.CharField(max_length=99, null=True)
    power = models.CharField(max_length=99, null=True)
    transmission = models.CharField(max_length=99, null=True)
    engine = models.CharField(max_length=99, null=True)
    fuel = models.CharField(max_length=99, null=True)
    drive_unit = models.CharField(max_length=99, null=True)
    overclocking = models.CharField(max_length=99, null=True)
    consumption = models.CharField(max_length=99, null=True)
    max_speed = models.CharField(max_length=99, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_from_wishlist(request):
        wishlist = request.session.get('wishlist', [])
        return CarModel.objects.filter(pk__in=wishlist)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'car_spetification'
        verbose_name_plural = 'cars_spetifications'
