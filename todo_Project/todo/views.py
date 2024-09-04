from rest_framework import generics, permissions
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoCreateView(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ToDoListView(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(owner=user)

    permission_classes = [permissions.IsAuthenticated]

class ToDoDeleteView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_permissions(self):
        if self.request.user.is_staff:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), permissions.IsOwner()]

    permission_classes = [permissions.IsAuthenticated]
