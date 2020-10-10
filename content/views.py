from django.shortcuts import render
from .models import New, Recent
from django.views.generic import ListView, DetailView

# Вывод всех статей
class ShowNewsAllView(ListView):
    model = New
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 6


    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsAllView, self).get_context_data(**kwargs)
        ctx['title'] = 'Все статьи'
        return ctx

# Вывод статей на главной странице
class ShowNewsView(ListView):
    model = New
    template_name = 'content/New.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 6



    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'
        return ctx
# Развертывание статей
class NewsDetailView(DetailView):
    model = New


    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = New.objects.filter(pk=self.kwargs['pk']).first()
        return ctx
# Контакты
def contact(request):
    return render(request, 'content/contact.html')

# История создания
def history_creat(request):
    return render(request, 'content/history_creat.html')

# Последнии события
def recent_events(request):
    form = Recent.objects.all()
    return render(request, 'content/recent_events.html', {'form':form})
