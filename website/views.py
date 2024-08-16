from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from blog.models import Post
from django.utils import timezone

from .forms import NewsletterForm, ContactForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
# custom 404 view
def custom_404(request, exception):
    return render(request, "website/404-page.html", status=404)


def about_view(request):
    User = get_user_model()
    users = User.objects.filter(is_superuser=False)
    context = {"users": users}

    return render(request, "website/about.html", context)


def newsletter_view(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "ایمیل شما با موفقیت به روزنامه اضافه گردید."
            )
        else:
            messages.add_message(
                request, messages.ERROR, "ثبت ایمیل شما در روزنامه با خطا مواجه شد."
            )

        return redirect(request.META.get("HTTP_REFERER"))


def contact_us_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            form.instance.name = "ناشناس"
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "پیام شما با موفقیت ارسال شد."
            )
        else:
            messages.add_message(request, messages.ERROR, "خطایی در ارسال پیام شما رخ داد")
            

    elif request.method == "GET":
        pass

    context = {
        "phone": "+98 919 1200 824",
        "email": "h20.ahmadi@gmail.com",
        "form": ContactForm(),
    }
    return render(request, "website/contact.html", context)


# def test_view(request):
#     # if request.method == "POST":
#     #     form = NameForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         name = form.cleaned_data["name"]
#     #         email = form.cleaned_data["email"]
#     #         subject = form.cleaned_data["subject"]
#     #         message = form.cleaned_data["message"]
#     #         print(name, email, subject, message)
#     #         return HttpResponse("")
#     # else:
#     #     form = NameForm()
#     messages.add_message(request, messages.SUCCESS, "Your message has been sent successfully")
#     messages.add_message(request, messages.ERROR, "Your message has been sent With Error")
#     return render(request, "website/test.html")


def index_view(request):

    # get last 4 posts with most views
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), is_published=True
    ).order_by("-counted_view")[:4]

    context = {"posts": posts}
    return render(request, "website/index.html", context)


def maintenance(request):
    return render(request, "website/comingsoon.html")
