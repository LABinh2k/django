import random

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Team, Character, TeamInfo
# Create your views here.


    
def index(request):
    
    return render(request, 'GIRng/index.html')

@staticmethod
def randomize():
        all_char = list(Character.objects.all())
        
        # use random.sample to create new Team
        
        # how to bind char to member?
        
        char_list = random.sample(all_char, 4) # cai nay nen tra lai mot list chua cac Character
        
        return char_list
    
# this will map to girng/team/
def generate(request):
    # why do i need object team? to store team ? to add team attribute later (maybe)
    
    # team generated from char list, 4 char added to member field 
    
    # -> generate when init team ?
    
    # change __init__ then in generate(request) create a new team like so:    
    
    # on second though, just create a generate function to generate the chars in team
    
    try:
       char_list = randomize()
    except ValueError as err:
        return HttpResponse(f"{str(err)}")
    
    # how do i pass team info to template ?
    # -> what info do i want to put on template? for now i want to pass 'name' to template, but there can be more in the future
    # -> add info to context like so:
    
    context = {
        'members': char_list,
        'number': len(char_list),
    }
    
    # after context is added, render either through shortcut or through loader
    # i do not  use generic views for now
    
    template = loader.get_template('GIRng/team.html')
    
    return HttpResponse(template.render(context, request))
    
    # short cut
    # return render(request, 'GIRng/team.html', context)