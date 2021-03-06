'''
    Courses module
'''

import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView

from coaches.models import Coach

from . models import Course, Lesson
from . forms import CourseModelForm, LessonModelForm

LOGGER = logging.getLogger('courses')


class CourseDetailView(DetailView):
    '''
        Detail information about course
    '''

    model = Course

    template_name = 'courses/detail.html'

    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        LOGGER.debug('Courses detail view has been debugged!')
        LOGGER.info('Logger of courses detail view informs you!')
        LOGGER.warning('Logger of courses detail view warns you!')
        LOGGER.error('Courses detail view went wrong!')

        context = super().get_context_data(**kwargs)

        context['lessons_list'] = Lesson.objects.filter(course=self.kwargs['pk'])

        return context


# def detail(request, course_id):
#     course = Course.objects.get(id=course_id)
#     lessons_list = Lesson.objects.filter(course=course)
#     coach = Coach.objects.get(id=course.coach.id)
#     assistant = Coach.objects.get(id=course.assistant.id)

#     context = {
#         'course': course,
#         'lessons_list': lessons_list,
#         'coach': coach,
#         'assistant': assistant,
#     }
#     return render(request, 'courses/detail.html', context)


def add(request):
    '''
        Add new course
    '''

    if request.method == 'POST':
        form = CourseModelForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            form.save()

            message = ('Course {} has been successfully added.'
                       .format(data['name']))

            messages.success(request, message)

            return redirect('/')
    else:
        form = CourseModelForm()

    context = {
        'form': form,
    }

    return render(request, 'courses/add.html', context)


def edit(request, course_id):
    '''
        Edit course information
    '''

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)

        if form.is_valid():
            form.save()

            message = 'The changes have been saved.'

            messages.success(request, message)

            return redirect('/courses/edit/{}'.format(course_id))
    else:
        form = CourseModelForm(instance=course)

    context = {
        'form': form
    }

    return render(request, 'courses/edit.html', context)


def remove(request, course_id):
    '''
        Remove course functionality
    '''

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        message = 'Course {} has been deleted.'.format(course.name)

        course.delete()

        messages.success(request, message)

        return redirect('/')

    context = {
        'course': course
    }

    return render(request, 'courses/remove.html', context)


def add_lesson(request, course_id):
    '''
        Add new lesson functionality
    '''

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = LessonModelForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            form.save()

            message = ('Lesson {} has been successfully added.'
                       .format(data['subject']))

            messages.success(request, message)

            return redirect('/courses/{}'.format(data['course'].id))
    else:
        form = LessonModelForm(initial={'course': course})

    context = {
        'form': form,
    }

    return render(request, 'courses/add_lesson.html', context)
