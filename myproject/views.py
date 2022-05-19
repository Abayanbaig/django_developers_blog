
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ProjectForm, ReviewForm
from .models import Project, Review, Tag
from django.contrib import messages
from .utils import searchProjects
from .utils import paginateProjects


def free(request):

    return render(request, 'projects/free.html')

def freefour(request):

    return render(request, 'projects/freefour.html')


def freethree(request):

    return render(request, 'projects/freethree.html')

def freetwo(request):

    return render(request, 'projects/freetwo.html')




@login_required(login_url='users:login')
def projects(request):
    project_list, search_query = searchProjects(request)

    project_list, custom_range = paginateProjects(
        request, project_list, 3)

    context = {'projects': project_list,
               'search_query': search_query,
               'custom_range': custom_range,

               }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    proj = None
    proj = Project.objects.get(id=pk)
    # all_reviewer = proj.reviewers
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.project = proj
            review.owner = request.user.profile
            review.save()

            proj.getVoteCount

            messages.success(request, 'Comment Added Successfully')
            return redirect('myproject:project', pk=proj.id)
        else:
            messages.error(request, 'Error occurred')

    context = {'proj': proj, 'review_form': review_form, }

    return render(request, 'projects/single-project.html', context)


def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project created Successfully')
            return redirect('users:account')
        else:
            messages.error(request, 'Some error occurred')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)






def deleteProject(request, pk):
    #profile = request.user.profile
    p = Project.objects.filter(id=pk)

    if request.method == 'POST':
        p.delete()
        messages.success(request, 'Project deleted Successfully')
        return redirect('users:account')

    context = {'object': p,

               }
    return render(request, 'projects/delete-form.html', context)


def updateProject(request, pk):
    profile = Project.objects.get(id=pk)
    p = profile
    form = ProjectForm(instance=p)
    msg = ''

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
            return redirect('users:account')
        else:
            messages.error(request, 'Some error occurred')

    context = {'form': form,
               'msg': msg, }

    return render(request, 'projects/project-form.html', context)

