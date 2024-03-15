from django import forms
from .models import VariantEn # import the model that maps to the variant table

class VariantEnForm(forms.ModelForm):
    hgvs = forms.TextInput()
    gene = forms.TextInput()
    disease = forms.TextInput()
    frequency = forms.IntegerField()
    def fillDatabase(hgvs, gene, disease,frequency):
        return VariantEn(hgvs, gene, disease,frequency)
    fillDatabase(hgvs, gene, disease,frequency)
    class Meta:
        model = VariantEn
        fields = ['hgvs', 'gene', 'disease', 'frequency']
    
        
