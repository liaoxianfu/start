from django.shortcuts import render


def get_form(request):
    return render(request, 'form.html')
