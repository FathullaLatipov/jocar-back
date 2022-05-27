from django import template

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)


@register.filter()
def in_wishlist(wishlist, request):
    return wishlist.pk in request.session.get('wishlist', [])
