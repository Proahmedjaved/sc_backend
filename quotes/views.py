from django.shortcuts import render
from quotes.models import Quote
from quotes.serializers import QuoteSerializer
from rest_framework import generics
# Create your views here.


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer