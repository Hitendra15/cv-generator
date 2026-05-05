from django.urls import path
from . import views
urlpatterns = [
    path('create_resume',views.create_resume,name="create_resume"),
    path('preview_resume/<slug:slug>',views.preview_resume,name="preview_resume"),
    path('',views.dashboard,name="dashboard")
]
