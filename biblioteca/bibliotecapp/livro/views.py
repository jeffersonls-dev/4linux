import os
from django.shortcuts import render
from .forms import LivroCreate
from .models import Livro
from django.http import HttpResponse, Http404
from bibliotecapp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT


def index(request):
    shelf = livro.objects.all()
    return render(request, 'livro/libraru.html', {'shelf': shelf})

def upload(request):
    upload = LivroCreate()
    if request.method == 'POST':
        upload = LivroCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpReponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'livro/upload_form.html',{'upload_form':upload})

def update_livro(request, livro_id):
    livro_id = int(livro_id)
    try:
        livro_sel = Livro.objects.get(id = livro_id)
    except  Livro.DoesNotExist:
        livro_form = LivroCreate(request.POST or None, instance = livro_sel)
    if livro_form.is_valid():
        livro_form.save()
        return redirect('index')
    return render(request, 'livro/upload_form.html', {'upload_form' : livro_form})

def delete_livro(request, livro_id):
    livro_id = int(livro_id)
    try:
        livro_sel = livro.objects.get(id = livro_id)
    except Livro.DoesNotExist:
        return redirect('index')
    livro_sel.delete()
    return redirect('index')

def download(request, livro_id):
    livro_id = int(livro_id)
    try:
        livro_sel = Livro.objects.get(id=livro_id)
    except Livro.DoesNotExist:
        return redirect('index')

    file_path = os.path.join(MEDIA_ROOT, livro_sel.document.url)
    file_path = os.getcwd() + file_path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def error_404(request, exception):
    data = {}
    return render(request,'error_404.html',data)
