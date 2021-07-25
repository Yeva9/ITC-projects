from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="ANUN")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='STEGHTSVEL E')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='POPOKHVEL E')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='HRATARAKVEL E')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def my_func(self):
        return "Hello from model."

    class Meta:
        ''' Meta description '''
        verbose_name = "Norutyun"  # entavernagira tsarayum(or` add news-y darav add Norutyun...)
        verbose_name_plural = "Norutyunner"  # sa el hognakii depqum(inchin -s er avelacnum` sa kdarna)
        # or` delet selected Norutyunner
        ordering = ['-created_at']  # ev adminki ev modeli sort. hertakanutyuny kpokhvi


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='CATEGORYI ANUN')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categoryner"
        ordering = ['title']
