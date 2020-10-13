from django.shortcuts import render

from .models import LocationPhotos

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_photo = LocationPhotos.objects.all().count()
    print(num_photo)
    
    context = {
        'num_photo': num_photo,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class LocationPhotosListView(generic.ListView):
    model = LocationPhotos
class LocationPhotosDetailView(generic.DetailView):
    model = LocationPhotos
    def Photo_detail_view(request,pk):
        try:
            Photo_id=LocationPhotos.objects.get(pk=pk)
        except LocationPhotos.DoesNotExist:
            raise Http404("Photo does not exist")

        #Photo_id=get_object_or_404(LocationPhotos, pk=pk)
        
        return render(
            request,
            'catalog/locationphotos_detail.html',
            context={'Photo':Photo_id,}
        )
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import LocationPhotos

class PhotoCreate(CreateView):
    model = LocationPhotos
    fields = ['title','image','depiction']


class PhotoUpdate(UpdateView):
    model = LocationPhotos
    fields = ['title','image','depiction']

class PhotoDelete(DeleteView):
    model = LocationPhotos
    success_url = reverse_lazy('Photos')