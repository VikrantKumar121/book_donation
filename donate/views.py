from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Details, Details2
from .forms import Donate_Book
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from . import forms
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

def admin_view(request):
    user_log = get_current_users().count()
    context = {
    'user_log': user_log,
    "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,'unclassed'],
    }
    return render(request, 'donate/index.html', context)

def index(request):
    total_books = Details2.objects.all().count()
    total_users = User.objects.all().count()
    user_log = get_current_users()
    print(user_log.count())
    context = {
        "user_log": user_log.count(),
        "total_books": total_books,
        "total_users": total_users,
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,'unclassed'],

    }

    return render(request, 'donate/index.html', context)


def books_list(request):
    queryset = Details2.objects.all().order_by("-id")
    context = {
        "object_list": queryset,  # this context is the dictionary for impoting the objects of databaset
    }
    return render(request, 'donate/books_list.html', context)


@login_required(login_url='/login/')
def book_detail(request, id):
    instance = get_object_or_404(Details2, id=id)
    context = {
        "instance": instance,
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"],

    }
    return render(request, 'donate/book_detail.html', context)


@login_required(login_url='/login/')

def profile(request):
    # print(request.user.id)
    queryset_list = Details2.objects.filter(user = request.user.id)#.order_by("-id")
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    print(queryset_list)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "queryset_list": queryset,
        "page_request_var": page_request_var
    }
    return render(request, 'donate/profile.html', context)


def contributer_board(request):
    return render(request, 'donate/contributer_board.html')


@login_required(login_url='/login/')
def search_list(request):
    query1 = request.GET.get('q1')
    query2 = request.GET.get('q2')
    # query3 = request.GET.get('q3')
    # query4 = request.GET.get('q4')
    only_open = Details2.objects.filter(Status="Open")
    if query1 and query2:
        queryset_list = only_open.filter(
            Q(Name__iexact=query1) &
            Q(Class=query2)
            # Q(Your_District__iexact=query3) &
        ).distinct()
        paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
        page_request_var = "page"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)
        context = {
            "queryset_list": queryset,
            "page_request_var": page_request_var
        }
        return render(request, 'donate/search_list.html', context)
    else:
        return render(request, 'donate/404.html')


@login_required(login_url='/login/')  # LOGIN_URL = '/login/'
def donate_book(request):
    form = Donate_Book(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message response
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'unclassed'],
        "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth" ],
    }

    return render(request, 'donate/donate_book.html', context)


def donate_book_update(request, id=None):
    instance = get_object_or_404(Details2, id=id)
    form = Donate_Book(request.POST or None, instance=instance)
    if request.user.is_authenticated() and instance.user.id == request.user.id:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # message_response
            return HttpResponseRedirect(instance.get_absolute_url())

        context = {
            "instance": instance,
            "form": form,
            "class_count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "edition_count": ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"],

        }
        return render(request, 'donate/donate_book.html', context)
    else:
        response = HttpResponse("You donot have permission to do this")
        return response


def test(request):
    queryset = Details2.objects.filter(Name__iexact="Q")
    total_users = User.objects.all().count()
    context = {
        "object_list": queryset,  # this context is the dictionary for impoting the objects of databaset
        "total_users": total_users,
    }
    return render(request, 'donate/test.html', context)

#
# def delete(request, id=None):
#     instance = get_object_or_404(Details2, id=id)
#     if request.user.is_authenticated() and instance.user.id == request.user.id:
#         instance.delete()
#         return redirect("books_list")
#     else:
#         response = HttpResponse("You dont have permission to do this")
#         return response

def contact_us(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ashwindhakal97@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "donate/contact_us.html", {'form': form})

def success(request):
    return render(request, 'donate/success.html')
