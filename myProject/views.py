from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from myapp.models import Plant, Phytochemical, Target
from myapp.forms import ContactForm
from django.http import HttpResponse
import requests
from tempfile import NamedTemporaryFile
import os

class AboutView(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, request):
        return render(request, "my_app/about.html")

class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, "my_app/home.html")

class ContactView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        form = ContactForm()
        return render(request, 'my_app/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'my_app/contact.html', {'form': form})

class PlantListView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        plants = Plant.objects.all().order_by("name")
        return render(request, "my_app/plant.html", {"dicts": plants})

class HelpView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, "my_app/help.html")

class PlantDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, name):
        plant = get_object_or_404(Plant, name=name)
        phytochemicals = plant.phytochemical_value.all()
        return render(request, "my_app/plantdetail.html", {'dicts': plant, "dict2": phytochemicals})

class SearchView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        var = request.GET.get("main_search", "").strip()
        if not var:
            messages.error(request, 'Please enter a valid search term.')
            return render(request, "my_app/search.html")

        phytochemicals = Phytochemical.objects.filter(
            Q(synonymous_names__icontains=var) & Q(synonymous_names__istartswith=var)
        ).order_by("name")

        if not phytochemicals.exists():
            messages.info(request, 'No results found.')

        paginator = Paginator(phytochemicals, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "my_app/search.html", {"dicts": page_obj})

class CompoundDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, name):
        phytochemical = get_object_or_404(Phytochemical, name=name)
        return render(request, "my_app/compound_detail.html", {"dicts": phytochemical})

class PlantCompoundDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, name):
        phytochemical = get_object_or_404(Phytochemical, name=name)
        return render(request, "my_app/compound_detail.html", {"dicts": phytochemical})

class AdvancedSearchView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, "my_app/acknowledgement.html")

class TargetDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, name):
        target = get_object_or_404(Target, name=name)
        return render(request, "my_app/target.html", {"dicts": target})

# Download sdf function remains as function based per your request
def download_sdf(request, name, id):
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/{id}/record/SDF/"
    response = requests.get(pubchem_url)
    if response.status_code == 200:
        sdf_content = response.content
        with NamedTemporaryFile(delete=False, suffix='.sdf') as tmp_file:
            tmp_file.write(sdf_content)
            tmp_file_path = tmp_file.name

        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{name}.sdf"'

        with open(tmp_file_path, 'rb') as file:
            response.write(file.read())

        os.remove(tmp_file_path)
        return response

    return HttpResponse(f"Error fetching SDF content for compound name {name} from PubChem")


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)