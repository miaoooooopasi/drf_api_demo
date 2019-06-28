from django.urls.conf import path

from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [

]  # 路由列表
router = DefaultRouter()  # 可以处理视图的路由器
router.register('students', views.StudentViewSet)  # 向路由器中注册视图集
router.register('teachers', views.TeacherViewSet)  # 向路由器中注册视图集
urlpatterns += router.urls  # 将路由器中的所有路由信息追加到Django的路由列表中
