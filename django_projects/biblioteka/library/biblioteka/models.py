from django.db import models
from django.urls import reverse 
import uuid

# Create your models here.

class Genre(models.Model):
    name = models.CharField('pavadinimas', max_length=200, help_text='iveskite knygos zanra(pvz. veiksmo)')
    
    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField('vardas', max_length=100)
    last_name = models.CharField('pavarde', max_length=100)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
    class Meta:
        ordering = ['first_name' ,'last_name']
        verbose_name = 'autorius'
        verbose_name_plural = 'autoriai'

class Book(models.Model):
    """Modelsi reprezentuoja knyga (bet ne specifine knygos kopija"""
    title = models.CharField("pavadinimas", max_length=200) # Charfield atitinka varchar , apie 250 yra riba dazniausiai
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='biblioteka', verbose_name='autorius', null=True)
    summary = models.TextField('aprasymas', max_length=1000, help_text='trumpas knygos aprasymas')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    genre = models.ManyToManyField(Genre, help_text='isrinkite zanra(us) siai knygai')
    
    def __str__(self):
        return f'{str(self.author)} - {self.title}'
    
    # def get_absolute_url(self):
    #     return reverse("book-detail", args=[str(self.id)])



class BookInstance(models.Model):
    """Modelis, aprašantis konkrečios knygos kopijos būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='book_instances', verbose_name='knyga') 
    due_back = models.DateField('Bus prieinama/grazinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['due_back']
        verbose_name = 'knygos kopija'
        verbose_name_plural = 'knygos kopijos'

    def __str__(self):
        return f'{self.id} ({self.book.title})'