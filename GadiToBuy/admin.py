from django.contrib import admin
from .models import Vehicle
from .models import Inquiry
from .models import Favorite
from .models import VehicleImage

admin.site.register(VehicleImage)
admin.site.register(Inquiry)
admin.site.register(Vehicle)
admin.site.register(Favorite)