from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from links.forms import CreateLink
from .models import Links


@login_required(login_url='login')
def create(request):
    if request.user.is_authenticated:
        error = ''
        link = Links.objects.all()
        form = CreateLink()

        if request.method == 'POST':
            if list(request.POST.values())[2] in [data[2] for data in list(link.values().values_list())]:
                error = 'Сокращенная ссылка с таким названием уже существует'
            else:
                form = CreateLink(data=request.POST)

                if form.is_valid():
                    post = form.save(commit=False)
                    post.author_id = request.user.id
                    post.save()
                    return redirect('links')
                else:
                    error = 'Неправильно введенные данные'
        data = {
            'form': form,
            'link': link,
            'error': error
        }
        return render(request, 'links/create.html', data)
    else:
        return redirect('login')


def redirect_link(request, url):
    curr_short_link = Links.objects.filter(short_link=url)
    curr_full_link = Links.objects.get(short_link=curr_short_link[0]).full_link

    if len(curr_short_link) == 0:
        return render(request, 'links/page_not_found.html')

    return redirect(curr_full_link)
