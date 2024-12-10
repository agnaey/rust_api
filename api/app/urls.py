from django.urls import path
from . import views

urlpatterns = [
    path('fun1',views.fun1),
    path('fun2',views.fun2),
    path('fun3',views.fun3),
    path('fun4/<d>',views.fun4),
    path('fun5',views.fun5),
    path('fun6/<d>',views.fun6),
    path('fun7',views.fun7.as_view()),
    path('fun8/<d>',views.fun8.as_view()),
    path('fun9',views.genericapiview.as_view()),
    path('fun10/<id>',views.update.as_view()),
]