from django.shortcuts import render
from django.views import generic
from rest_framework import generics, viewsets

from api.models import Company, JobPosting
from api.serializers import CompanySerializer, JobPostingSerializer, JobPostingListSerializer, \
    JobPostingUpdateSerializer, JobPostingDetailSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobPostingCV(generics.CreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobPostingUV(generics.UpdateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingUpdateSerializer

class JobPostingLV(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingListSerializer

class JobPostingDV(generics.RetrieveAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingDetailSerializer

# class JobPostingViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         pass
#
#     def create(self, request):
#         pass
#
#     def retrieve(self, request, pk=None):
#         pass
#
#     def update(self, request, pk=None):
#         pass
#
#     def partial_update(self, request, pk=None):
#         pass
#
#     def destroy(self, request, pk=None):
#         pass