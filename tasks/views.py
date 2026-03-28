from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrOwner

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()   # ✅ ADD THIS LINE
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Task.objects.all()
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)