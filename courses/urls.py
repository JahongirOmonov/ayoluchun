from django.urls import path, include
from rest_framework import routers
from .views import InterviewViewSet, upload_video, CourseArchiveView, CourseListView, CourseListRetrieveUpdateDestroy, CourseArchive

router = routers.DefaultRouter()
router.register(r'mediafiles', InterviewViewSet)

urlpatterns = [
    path('interviews/', include(router.urls)),
    path('archieve/', CourseArchiveView.as_view()),
    path('archieve/<int:pk>', CourseArchiveView.as_view()),
    path('list/', CourseListView.as_view()),
    path('list/<int:pk>', CourseListRetrieveUpdateDestroy.as_view())
]

