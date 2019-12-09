from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView, View, ListView, DetailView, CreateView)
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Photos, Like
from .forms import PhotoForm


class PhotosView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Photos.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'created':
            queryset = queryset.order_by('-created')
        elif order == 'quant_like':
            queryset = queryset.order_by('-quant_like')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        return context


class PhotosNotView(ListView):
    template_name = 'autorizar_fotos.html'

    def get_queryset(self):
        queryset = Photos.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'created':
            queryset = queryset.order_by('-created')
        if order == 'quant_like':
            queryset = queryset.order_by('-quant_like')
        return queryset


class ViewFormPhotos(CreateView):
    model = Photos
    template_name = 'enviar_foto.html'
    form_class = PhotoForm
    success_url = reverse_lazy('photos:send_photo')


class PhotoAutorized(View):
    aproved = True

    def get(self, request, pk):
        photo = get_object_or_404(Photos, pk=pk)
        photo.aproved = self.aproved
        photo.save()
        message = 'Foto autorizada com sucesso'
        messages.success(request, message)
        success_url = reverse_lazy('photos:not_view')
        return redirect(success_url)


class PhotoRemove(View):
    def get(self, request, pk):
        photo = get_object_or_404(Photos, pk=pk)
        photo.delete()
        message = 'Foto deletada com sucesso'
        messages.success(request, message)
        success_url = reverse_lazy('photos:not_view')
        return redirect(success_url)


class AddLike(View):

    def get(self, request, pk):
        user = request.user.id
        photo = get_object_or_404(Photos, pk=pk)
        if Like.objects.filter(id_photo=pk, author=user).count() == 0:
            like = Like(id_photo=pk, author=user)
            like.save()
            photo.quant_like = photo.quant_like + 1
            photo.save()
        elif Like.objects.filter(id_photo=pk, author=user).count() == 1:
            like = Like.objects.filter(id_photo=pk, author=user)
            like.delete()
            photo.quant_like = photo.quant_like - 1
            photo.save()
        success_url = reverse_lazy('photos:feed')
        return redirect(success_url)


feed = PhotosView.as_view()
not_view = PhotosNotView.as_view()
approve_photo = PhotoAutorized.as_view()
send_photo = ViewFormPhotos.as_view()
remove_photo = PhotoRemove.as_view()
add_like = AddLike.as_view()
