
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import LoginView, LogoutView
# from users.views import register




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('face.urls')),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login')
    path('accounts/', include('django.contrib.auth.urls'))
]
