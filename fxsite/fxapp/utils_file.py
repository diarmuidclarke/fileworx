import os
from django.conf import settings

# for files uploaded via web page
def upload_the_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
