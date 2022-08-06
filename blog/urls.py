from django.urls import path,include
from . import views
urlpatterns=[
    path('', views.home, name="home"),
    path('post/<str:pk>/', views.post_details, name="post_detail"),
    # path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/', views.category, name="category"),
    path('blog/', views.blog, name="blog"),
    # path('category/<str:category>/', views.category, name="category"),
    path('tinymce/', include('tinymce.urls')),
    
]


