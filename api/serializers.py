from rest_framework import serializers

from api.models import Company, JobPosting


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'country', 'city']

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id', 'company', 'position', 'compensation', 'content', 'stack']

class JobPostingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['company', 'position', 'compensation', 'content', 'stack']

class JobPostingRetrieveSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    country = serializers.CharField(source='company.country')
    city = serializers.CharField(source='company.city')

    class Meta:
        model = JobPosting
        fields = ['id', 'company_name', 'country', 'city', 'position', 'compensation', 'stack', 'content']

class JobPostingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['position', 'compensation', 'content', 'stack']

class JobPostingListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    country = serializers.CharField(source='company.country')
    city = serializers.CharField(source='company.city')

    class Meta:
        model = JobPosting
        fields = ['id', 'company_name', 'country', 'city', 'position', 'compensation', 'stack']

class JobPostingAnotherListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    country = serializers.CharField(source='company.country')
    city = serializers.CharField(source='company.city')
    another = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = JobPosting
        fields = ['id', 'company_name', 'country', 'city', 'position', 'compensation', 'stack', 'another']