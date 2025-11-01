from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    AboutView, HomeView, ContactView, PlantListView, HelpView,
    PlantDetailView, SearchView, CompoundDetailView, AdvancedSearchView,
    TargetDetailView, PlantCompoundDetailView, download_sdf
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", HomeView.as_view(), name="home"),
    path("",include('user.urls')),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("plant/", PlantListView.as_view(), name="plant"),
    path("help/", HelpView.as_view(), name="help"),
    path("plant/plantdetail/<str:name>/", PlantDetailView.as_view(), name="plantdetail"),
    path("search/", SearchView.as_view(), name="search"),
    path("detail/<str:name>/", CompoundDetailView.as_view(), name="detail"),
    path("detail/compound/<str:name>/", PlantCompoundDetailView.as_view(), name="compounddetail"),
    path("advancedsearch/", AdvancedSearchView.as_view(), name="advanced_search"),
    path("detail/target/<str:name>/", TargetDetailView.as_view(), name="target"),
    path('detail2/<str:name>/<str:id>/', download_sdf, name='download_sdf'),
]


handler404 = 'myProject.views.custom_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
