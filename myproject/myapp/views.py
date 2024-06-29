import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import MyTableExcel

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            for value in df.iloc[:, 0]:
                MyTableExcel.objects.create(data=value)

            return redirect('myapp:success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def show_data(request):
    data = MyTableExcel.objects.all()
    cvon = {
        'data': data
    }
    return render(request, 'show.html' , context=cvon)