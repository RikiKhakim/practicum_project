from .models import News

def latest_news(request):
    latest_news = News.objects.all().order_by("-publish_time")[:8]

    context = {
        "latest_news": latest_news
    }

    return context