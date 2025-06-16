from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeModelViewSet, basename='employee')

urlpatterns = [
  path('students', views.studentsView),
  path('students/<int:pk>', views.studentDetailView),
  # path('employees', views.Employees.as_view()),
  # path('employees/<int:pk>', views.EmployeeDetail.as_view()),
  path('', include(router.urls)),
  path('blogs/', views.BlogListView.as_view(), name='blog-list'),
  path('comments/', views.CommentListView.as_view(), name='comment-list'),
  path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
  path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),

]