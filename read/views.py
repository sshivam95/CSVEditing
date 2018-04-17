from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pandas import DataFrame
import pandas as pd
from bs4 import BeautifulSoup

from .models import Document
from .forms import DocumentForm
from .CSVEditing import process_file

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)# Getting the post method from upload Button
        if form.is_valid():
            document = form.save()
            # call to the new method
            csv = process_file(document.document) # Calling process_file function from CSVEditing to add Predicted_Category column
            csv.to_csv("read/media/result.csv", index=False) # saving the file, later this file will be edited and downloaded
            csv_file = pd.read_csv("read/media/result.csv", usecols=['Predicted_Category', 'complaint_title']) # displaying only 2 columns
            # df_title = pd.read_csv("read/media/result.csv", usecols=['complaint_title'])
            data = DataFrame(csv_file)
            data_html = data.to_html(index=False) # displaying the data in table form
            soup = BeautifulSoup(data_html, "html.parser")
            soup.find('table')['align'] = 'center'
            soup.find('table')['id'] = 'outerTable'
            # table = soup.findAll('table')[0]
            # rows = table.findAll('tr')
            # predicted = []
            # for row in rows[1:]:
            #     predicted.append(row.findAll('td')[1])

            # print(data_html) # this will be passed in the html
            # form = DocumentForm()
            # print(str(predicted))
            # print(str(soup))
            pre = [ 'Category 1', 'Category 2', 'Category 3']
            context = {'loaded_data': str(soup),
                       'predicte_data': pre,
                       'form' : form,
                       'url': './media/result.csv',
                       }
            # selected_cat = form.cleaned_data('value')
            # response = HttpResponse(csv, content_type='text/csv')
            # response['Content-Disposition'] = 'attachment; filename = result.csv'
            # return response
            form.save()
            return render(request, 'index.html', context)
    else:
        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form,
        'url' : './media/result.csv',
    })
