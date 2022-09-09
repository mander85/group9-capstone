from django.contrib import admin
#from .models import Leader_Post
from .models import Generator_Exercises, Leader_Post_bytime
# Register your models here.

#### Defunct model kept in case of future use 
#admin.site.register(Leader_Post)

admin.site.register(Leader_Post_bytime)
admin.site.register(Generator_Exercises)