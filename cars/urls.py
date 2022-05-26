from django.urls import path

from cars.views import ModelsView, add_to_wishlist, WishlistModelListView

app_name = 'models'

urlpatterns = [
        path('wishlist/', WishlistModelListView.as_view(), name='wishlist'),
        path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
        path('', ModelsView.as_view(), name='product'),
]
