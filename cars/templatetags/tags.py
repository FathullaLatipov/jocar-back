from django import template

register = template.Library()


@register.filter()
def in_wishlist(wishlist, request):
    return wishlist.pk in request.session.get('wishlist', [])
