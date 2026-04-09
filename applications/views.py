from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer

class IsApplicantOrCompany(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.applicant == request.user or obj.job.company == request.user

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'company':
            return Application.objects.filter(job__company=user)
        return Application.objects.filter(applicant=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)