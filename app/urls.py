from django.urls import path
from . import views

urlpatterns = [
        path("",views.index,name="index"),
        path("login/",views.loginView,name="login"),
        path("logout/",views.logoutView,name="logout"),
        path("register/",views.registerView,name="register"),
        path("user<int:user_id>/",views.userProfile,name="userprofile"),
        path("userMemster<user_id>/",views.userMemster,name="usermemster"),
        path("<int:task_id>/",views.noteView,name="noteView"),
        path("deleteTask<int:task_id>/",views.deleteTask,name="deleteTask"),
        path("editTask<int:task_id>/",views.editTaskView,name="editTask"),
]