#!/usr/local/bin/python
# -*- coding: latin-1 -*-
from links.models import Owner, Link
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from links.forms import NewLinkForm


def new(request, name):
    owner = Owner.objects.get(name = name)
    if request.method == 'POST':
        form = NewLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit = False)
            link.owner = owner
            link.save()
        else:
            return HttpResponse("Niepoprawnie wypelniony formularz.")
    else:
        form = NewLinkForm({'owner': owner, 'author': owner,})
        return render_to_response('links/new.html',  
                              {'form': form},)

    return HttpResponseRedirect(reverse('links.views.links', args = (owner.name, )))


def links(request, name = 'tofikowy'):
    return render_to_response('links/list.html', {'view_name': name, })
