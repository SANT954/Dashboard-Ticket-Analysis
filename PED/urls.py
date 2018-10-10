from django.conf.urls import url
from PED import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        url(r'^$', views.PED_summary.as_view()),
		url(r'^sprint_summary/$', views.Fetch_Sprint),
        url(r'^sprint_summary_post_form/$', views.POSTForm),
		url(r'^media/$', views.Ajax_Test),
		
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
