from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageForm


def image_create(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            form.save()
            messages.success(request,
                             'Изображение успешно добавлено')
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {
                   'section': 'images',
                   'form': form
                   }
                  )
