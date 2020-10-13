from django.db import models
from django.urls import reverse
# Create your models here.
class LocationPhotos(models.Model):
    """Model representing a Photo genre."""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos',blank=True)
    depiction = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Photo."""
        return reverse('Photo-detail', args=[str(self.id)])