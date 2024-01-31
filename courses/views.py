from rest_framework import viewsets
from .models import Interviews, CourseArchive, CourseList
from .serializers import InterviewSerializer, CourseArchiveSerializer, CourseListSerializer
from .form import InterviewForm
from django.shortcuts import render, redirect
from rest_framework import generics

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interviews.objects.all()
    serializer_class = InterviewSerializer


def upload_video(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
        else:
            form = InterviewForm()
        return render(request, 'upload.html', {'form':form})


class CourseArchiveView(generics.ListCreateAPIView):
    queryset = CourseArchive
    serializer_class = CourseArchiveSerializer

class CourseArchiveRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseArchive
    serializer_class = CourseArchiveSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = CourseList
    serializer_class = CourseListSerializer

class CourseListRetrieveUpdateDestroy(generics.ListCreateAPIView):
    queryset = CourseList
    serializer_class = CourseListSerializer



