from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html",context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }

    return render(request, 'news/news_detail.html', context)

''' def homePageView(request):
    categories = Category.objects.all()
    news_list = News.objects.filter(status=News.Status.Published).order_by('-publish_time')[:4]
    sport = News.objects.filter(status=News.Status.Published, category__name="Sport").order_by('-publish_time')[:1]
    sport_news = News.objects.filter(status=News.Status.Published, category__name="Sport").order_by('-publish_time')[:4]
    context = {
        "news_list": news_list,
        "categories": categories,
        "sport_news": sport_news,
        "sport": sport
    }

    return render(request, 'news/home.html', context) '''


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.filter(status=News.Status.Published).order_by('-publish_time')[:4]
        context['sport_xabarlari'] = News.objects.filter(status=News.Status.Published, category__name="Sport").order_by('-publish_time')[:4]
        context['xorij_xabarlari'] = News.objects.filter(status=News.Status.Published, category__name="Xorij").order_by('-publish_time')[:4]
        context['texno_xabarlar'] = News.objects.filter(status=News.Status.Published, category__name="Texnologiya").order_by('-publish_time')[:4]
        context['mahalliy_xabarlar'] = News.objects.filter(status=News.Status.Published, category__name="Mahalliy").order_by('-publish_time')[:4]
        return context






''' def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> So'rovingiz yuborildi! </h2>")
    context = {
        "form": form
    }
    return render(request, 'news/contact.html', context) '''

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("So'rovingiz yuborildi!")

        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


class LocalNewsPage(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = 'mahalliy_xabarlar'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Mahalliy")
        return news


class WorldNewsPage(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = 'xorij_xabarlari'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Xorij")
        return news

class TechnologyNewsPage(ListView):
    model = News
    template_name = "news/texno.html"
    context_object_name = 'texno_xabarlar'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Texnologiya")
        return news

class SportNewsPage(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = 'sport_xabarlari'

    def get_queryset(self):
        news = self.model.objects.all().filter(category__name="Sport")
        return news



def errorPageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)

def aboutPageView(request):
    context = {

    }
    return render(request, 'news/about.html', context)
