import random
import logging

from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, Template, Context
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Team, Character, TeamInfo
from .forms import TeamForm
# Create your views here.

logger = logging.getLogger("django")

# TODO: make new login interface later


@login_required(login_url='accounts/login/')
def index(request):
    logger.info("Logging: This is index")
    return render(request, 'GIRng/index.html')

# display a form for user to add team


def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            char_list = form.cleaned_data['char_list']

            # get resonance from list of character
            # resonance = resonance(char_list)

            team = Team(name=name)
            team.save()
            for char in char_list:
                tmp = TeamInfo(character=char, team=team)
                tmp.save()

            return redirect('GIRng:team-list')
    else:
        form = TeamForm()
        return render(request, 'GIRng/team.html', {'form': form})


@staticmethod
def randomize():
    all_char = list(Character.objects.all())

    # use random.sample to create new Team
    # how to bind char to member?
    # cai nay nen tra lai mot list chua cac Character
    char_list = random.sample(all_char, 4)

    return char_list


def create_random_team(request):
    # why do i need object team? to store team ? to add team attribute later
    # team generated from char list, 4 char added to member field
    # -> generate when init team ?
    # change __init__ then in generate(request) create a new team like so:
    # on second though, just create a generate function to generate the chars
    # in team

    try:
        char_list = randomize()
    #    raise ValueError("Character not found")
    except ValueError as err:
        raise Http404(f"{str(err)}")

    # how do i pass team info to template ?
    # -> what info do i want to put on template?
    # for now i want to pass 'name' to template,
    # but there can be more in the future
    # -> add info to context like so:

    context = {
        'members': char_list,
        'number': len(char_list),
    }

    # after context is added, render either through shortcut or through loader
    # i do not  use generic views for now

    template = loader.get_template('GIRng/randomize.html')

    return HttpResponse(template.render(context, request))

    # short cut
    # return render(request, 'GIRng/team.html', context)


def team_list(request):
    # team list
    try:
        t = Team.objects.all()
    except Exception as err:
        raise Http404(f"{str(err)}")

    return render(request, 'GIRng/team_list.html', {'teamlist': t, })


def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    context = {
        "team_name": team.name,
    }
    return render(request, 'GIRng/team_detail.html', context)


class CharacterListView(ListView):
    model = Character
    context_object_name = 'character_list'


class CharacterDetailView(DetailView, LoginRequiredMixin):
    model = Character


class SignupView(View):
    pass
