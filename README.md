# Django Advanced Class Based View
## Basic
### Views.py
```
class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
```

### Url.py
* Extract CBView class as view
```
    path('',views.CBView.as_view())
```

## Template View with CBV
### Views.py
* Import TemplateView
* Just set this Class Object Attribute to the template page.
* function to get context data
```
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context
```
### Url.py
* Extract IndexView class as view
```
    path('',views.IndexView.as_view())
```
### Index.html
* View context data in template

```
    <h2>Here is your injected content: {{ injectme }}</h2>
```
#### Next Branch : detail-and-list-view
