from django.contrib import admin

# Register your models here.
from .models import Bookmark, PersonalBookmark

admin.site.register((Bookmark, PersonalBookmark))
 