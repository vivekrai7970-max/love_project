from django.shortcuts import render

def birthday_wish(request):
    return render(request, 'birthday.html')

def proposal_page(request):
    return render(request, 'proposal.html')

def congratulations_page(request):
    return render(request, 'congratulations.html')

def memories_page(request):
    return render(request, 'memories.html')
