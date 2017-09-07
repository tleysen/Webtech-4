from django.contrib import admin

from .models import Quote
from .models import Author

admin.site.register(Quote)
admin.site.register(Author)
