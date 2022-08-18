from rest_framework import serializers


from api.models import Company, JobPosting, User, Application


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'country', 'city']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'phone']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'jobPosting', 'user']

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
