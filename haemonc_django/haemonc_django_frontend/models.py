# models.py
from django.db import models
class VariantEn(models.Model):
    # A field for storing the HGVS nomenclature of the variant
    hgvs = models.CharField(max_length=255, null=False, blank=False, unique=True)
    # A field for storing the gene name of the variant
    gene = models.CharField(max_length=255, null=False, blank=False)
    # A field for storing the disease name associated with the variant
    disease = models.CharField(max_length=255, null=False, blank=False)
    # A field for storing the frequency of the variant in the population
    frequency = models.FloatField(null=False, blank=False)
    def __str__(self):
        return self.hgvs
