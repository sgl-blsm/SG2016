from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    create_time = indexes. DateTimeField(model_attr='create_time')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status='p')
