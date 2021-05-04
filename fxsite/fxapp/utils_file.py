"""
Utility methods for file operations
"""

import os
from django.conf import settings

# for files uploaded via web page
def upload_the_file(f):
    with open(os.path.join(settings.MEDIA_ROOT, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



# get a list of files (filenames only)
#   matching a list of supported extensions
#
def get_files(path_of_files,list_supported_extensions):
    list_files = []
    for search_path, search_subfolders, search_files in os.walk(path_of_files):
        for name in search_files:
            fn = os.path.join(search_path, name)
            full_filename = os.path.basename(fn)
            name, ext = os.path.splitext(full_filename)
            if ext.lower() in list_supported_extensions:
                list_files.append(full_filename)
    
    return list_files