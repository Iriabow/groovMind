from django.shortcuts import render
from redirections.models import Address
from django.http import HttpResponse
# Create your views here.
def redirect(request):
    address = Address.objects.first()
    print(address.ip)

    html = '<html><body><a href="http://'+address.ip+'">'+address.ip+'</a> <meta http-equiv="refresh" content="0; url=http://'+address.ip +'" /></body></html>'
    return HttpResponse(html)


def saveIp(request):
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    """
    address = Address.objects.first()

    ip = request.GET['ipRedirection']
    if address:
        address.ip= ip
        address.save()
    else:
        address=Address(ip=ip)
        address.save()
    html = "<html><body>Guardado</body></html>"
    return HttpResponse(html)
