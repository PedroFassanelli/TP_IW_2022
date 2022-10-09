from haystack import indexes
from sitio.models import Publicacion

class PublicacionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    texto = indexes.CharField(model_attr='text')
    publicationdate = indexes.DateField(model_attr='publicationdate')
    user = indexes.CharField(model_attr='user')
    location = indexes.CharField(model_attr='location')

    def get_model(self):
        return Publicacion

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(state='Publicado')
