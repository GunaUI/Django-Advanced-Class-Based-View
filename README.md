# Django Advanced Class Based View
## Basic
### Url.py
* Extract CBView class as view
```
    path('',views.CBView.as_view())
```
### Views.py
```
class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
```