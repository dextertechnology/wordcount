from django.shortcuts import render

from .text_analyze import general

def home(request):
    return render(request, 'index.html', {
        'apple': 'Diwakar Pandey'
})

def count(request):
    fulltext = general(request.GET['fulltext'])

    context = {
        'no_of_char': fulltext.count_letters(),
        'no_of_words': fulltext.count_words(),
        'tag_list': fulltext.words_with_numbers()
    }

    return render(request, 'count.html', context)