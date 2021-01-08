from django.contrib import admin
from home.models import EnggCollege, MmgCollege, MedicalCollege, LawCollege, Contact

# Register your models here.
myModels = [EnggCollege, MedicalCollege, MmgCollege, LawCollege, Contact]
admin.site.register(myModels)


