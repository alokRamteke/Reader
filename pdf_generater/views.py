# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
import os
import uuid
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        html = document_to_html(uploaded_file_url)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'html1':html
        })
    return render(request, 'upload.html')


def document_to_html(file_path):
    tmp = "/tmp"
    # file_path1 = os.path.join(settings.BASE_DIR, file_path)
    file_path1 = '/home/rails/Projects/Alok/pdf_reader/pdf_reader'+file_path
    guid = str(uuid.uuid1())
    # convert the file, using a temporary file w/ a random name
    command = "abiword -t %(tmp)s/%(guid)s.html %(file_path1)s; cat %(tmp)s/%(guid)s.html" % locals()
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=os.path.join(settings.BASE_DIR, "templates"))
    
    error = p.stderr.readlines()
    import pdb;pdb.set_trace()
    if error:
        raise Exception("".join(error))
    html = p.stdout.readlines()
    return "".join(html)