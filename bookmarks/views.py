from django.shortcuts import render
from .models import Bookmark, PersonalBookmark
from .forms import BookmarkForm

# Create your views here.
def index(request):
    # import pdb; pdb.set_trace()

    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            # TODO check for reques.user to allow for personal bookmarks
            form.save()
        else:
            # TODO error
            pass
    
    context = {}

    pbid = PersonalBookmark.objects.values_list('id')
    
    context['bookmarks'] = Bookmark.objects.exclude(id__in=pbid)

    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)
    
    context['form'] = BookmarkForm

    return render(request, 'bookmarks/index.html', context)
  