from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from NoteAPI.models import Note
from NoteAPI.serializers import NoteSerializer
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class NoteViewSet(ModelViewSet):
    queryset  = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class HomePage(TemplateView):
    template_name = 'note/base.html'
