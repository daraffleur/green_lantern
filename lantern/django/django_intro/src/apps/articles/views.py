from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, FormView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ArticlesForm, ArticleImageForm
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.


def main_page(request, *args, **kwargs):
    return render(request, 'pages/main_page.html')


@login_required
def main_page_logged_in(request, some_id=None, *args, **kwargs):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
            # 'search_form': form
        }
        return render(request, 'pages/search.html', context=context_data)

    def post(self, request):
        return HttpResponse('{}', status=201)


class ShowTitsViews(TemplateView):
    template_name = 'tits_list.html'

    def get_context_data(self, **kwargs):
        return {
            'tits': 2
        }


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tits'] = 42
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleUpdateImageView(FormView):
    form_class = ArticleImageForm
    template_name = 'article_image-update.html'

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'id': self.kwargs['id']})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['id'] = self.kwargs['id']
        return ctx


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Article, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Article.objects.get(id=id)

    return render(request, "detail_view.html", context)


# update view for details
def update_view(request, id):
    # dictionary for initial data with field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Article, id=id)

    # pass the object as instance in form
    form = ArticlesForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


class ArticleCreate(CreateView):
    # specify the model for create view
    model = Article

    # specify the fields to be displayed

    fields = ['title', 'body']


class ArticleDeleteView(DeleteView):
    # specify the model you want to use
    model = Article
    success_url = "/"


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(article_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)
