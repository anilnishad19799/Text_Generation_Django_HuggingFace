from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .class_app import Text_generation
# Create your views here.

class_obj = Text_generation()

@csrf_exempt
def index(request):
    return HttpResponse("Its work")

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        max_length = 50
        num_return_sequences = 1
        starting_text = request.POST['start_string']
        final_output = class_obj.process(starting_text, max_length, num_return_sequences)
        return HttpResponse(f'{final_output}')

