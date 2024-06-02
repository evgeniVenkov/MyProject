from django.shortcuts import render

def main(request):
    return render(request, 'app/main.html')

def product(request):
    return render(request, 'app/product.html')