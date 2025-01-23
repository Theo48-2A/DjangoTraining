from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Modèle Band
class Band(models.Model):
    class Genre(models.TextChoices):  # Choix de genres musicaux
        HIP_HOP = 'HH', 'Hip-Hop'
        SYNTH_POP = 'SP', 'Synth Pop'
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'

    name = models.fields.CharField(
        max_length=100,
        default="Unknown Band"  # Nom par défaut
    )
    genre = models.fields.CharField(
        max_length=50,
        choices=Genre.choices,
        default=Genre.HIP_HOP  # Genre par défaut
    )
    biography = models.fields.CharField(
        max_length=1000,
        default="No biography available."  # Biographie par défaut
    )
    year_formed = models.fields.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2021)
        ],
        default=2000  # Année de formation par défaut
    )
    active = models.fields.BooleanField(
        default=True  # Groupe actif par défaut
    )
    official_homepage = models.fields.URLField(
        null=True,
        blank=True,
        default=""  # Page officielle vide par défaut
    )

class Listing(models.Model):
    class ListingType(models.TextChoices):  # Choix des types d'annonces
        RECORDS = 'R', 'Records'
        CLOTHING = 'C', 'Clothing'
        POSTERS = 'P', 'Posters'
        MISC = 'M', 'Miscellaneous'

    title = models.fields.CharField(
        max_length=100,
        default="Untitled Listing"  # Titre par défaut
    )
    description = models.fields.CharField(
        max_length=1000,
        default="No description available."  # Description par défaut
    )
    sold = models.fields.BooleanField(
        default=False  # Par défaut, l'article n'est pas vendu
    )
    year = models.fields.IntegerField(
        null=True,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2021)
        ],
        default=2000  # Année par défaut si inconnue
    )
    band = models.ForeignKey(
        Band,
        null=True,
        on_delete=models.SET_NULL  # Si le groupe est supprimé, cette valeur devient NULL
    )
    type = models.fields.CharField(
        max_length=5,
        choices=ListingType.choices,
        default=ListingType.MISC  # Type par défaut : Miscellaneous
    )
