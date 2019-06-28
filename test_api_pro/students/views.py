from rest_framework.viewsets import ModelViewSet
from .models import Student,Teacher
from .serializers import StudentModelSerializer, TeacherModelSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin


# Create your views here
class StudentViewSet(CacheResponseMixin, ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer



