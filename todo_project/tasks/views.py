
# Create your views here.
from rest_framework import generics, response
from .models import Task
from .serializers import TaskSerializer
from datetime import date

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status', None)
        if status:
            today = date.today()
            if status.lower() == "incoming":
                queryset = queryset.filter(due_date__gt=today)
            elif status.lower() == "today":
                queryset = queryset.filter(due_date=today)
            elif status.lower() == "overdue":
                queryset = queryset.filter(due_date__lt=today)
        return queryset

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
