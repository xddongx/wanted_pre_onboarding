from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import filters
from rest_framework.status import HTTP_200_OK

from api.models import Company, JobPosting
from api import serializers

import io

# from api.serializers import JobPostingAnotherListSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer

class JobPostingViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = JobPosting.objects.all()
        serializer = serializers.JobPostingListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = serializers.JobPostingCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = JobPosting.objects.all()
        jobPosting = get_object_or_404(queryset, pk=pk)
        serializer = serializers.JobPostingRetrieveSerializer(jobPosting)

        print("serializer data 1 >>> ", serializer.data)

        companyId = jobPosting.company.pk
        anotherList = JobPosting.objects.filter(company=companyId).values_list('pk', flat=True)

        json = JSONRenderer().render(serializer.data)

        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)

        data["anotherPosts"] = anotherList

        print("data >>> ", data)

        return Response(data)

    def update(self, request, pk=None):
        queryset = JobPosting.objects.all()
        jobPosting = get_object_or_404(queryset, pk=pk)

        serializer = serializers.JobPostingUpdateSerializer(jobPosting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = JobPosting.objects.all()
        jopPosting = get_object_or_404(queryset, pk=pk)
        jopPosting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobPostingSearchView(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = serializers.JobPostingListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['company__name', 'stack']


