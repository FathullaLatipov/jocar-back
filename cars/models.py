from django.db import models


class CarModel(models.Model):
    model = models.CharField(max_length=99, null=True)
    image = models.FileField(upload_to='cars_image', null=True)
    obyom = models.CharField(max_length=99, null=True)
    moshnost = models.CharField(max_length=99, null=True)
    korobka = models.CharField(max_length=99, null=True)
    dvigatel = models.CharField(max_length=99, null=True)
    toplivo = models.CharField(max_length=99, null=True)
    privod = models.CharField(max_length=99, null=True)
    razgon = models.CharField(max_length=99, null=True)
    rasxod = models.CharField(max_length=99, null=True)
    max_skorost = models.CharField(max_length=99, null=True)
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
