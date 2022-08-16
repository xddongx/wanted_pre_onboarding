from django.urls import path, include
from rest_framework import routers

from api import views
from api.views import CompanyViewSet, JobPostingCV, JobPostingDV, JobPostingLV  # , JobPostingViewSet

router = routers.DefaultRouter()
router.register(f'company', CompanyViewSet)
# router.register(r'job_posting', JobPostingCV, basename='create')
# router.register(r'job_posting-detail', JobPostingDV, basename='detail')
# router.register(r'job_posting-list', JobPostingLV)
# router.register(r'job_posting', JobPostingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('job_posting/', views.JobPostingCV.as_view(), name='create'),
    path('job_posting/<int:pk>/', views.JobPostingDV.as_view(), name='detail'),
    path('job_posting/list/', views.JobPostingLV.as_view(), name='list'),
    path('job_posting/update/<int:pk>/', views.JobPostingUV.as_view(), name='update'),

]
