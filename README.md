# Django CRUD Operation
## Create View
### views.py (create form here)
* import CreateView from django.views.generic 
    ```
        class SchoolCreateView(CreateView):
        fields = ("name","principal","location")
        model = models.School

    ```
### make create template default name of the CreateView file is modelname_form.html (eg :school_form.html)
```
    {% extends "basic_app/basic_app_base.html" %} 

    {% block body_block %}
    <h1>
        {% if not form.instance.pk %}
            Create School 
        {% else %} 
            Update School 
        {% endif %}
    </h1>
    <form method="POST">
        {% csrf_token %} {{ form.as_p }}
        <input type="submit" class='btn btn-primary' value="Submit">

    </form>


    {% endblock %}
```
### Make sure update url.py about create form path
    ```
        path('create/',views.SchoolCreateView.as_view(),name='create')
    ```
### Retrun to detail page after save(must include this)
* add get_absolute_url definition in school model to inform dhango go back in reverse to detail page with newly created primary key (refer models.py)
```
from django.urls import reverse

def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})
    
```

## Update View
### views.py (update form here)
* import UpdateView from django.views.generic 
    ```
    class SchoolUpdateView(UpdateView):
        fields = ("name","principal")
        model = models.School

    ```
### Make sure update url.py about update form path with primary key
    ```
        path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update')
    ```
### Add update button
    ```
        <p><a class='btn btn-warning' href="{% url 'basic_app:update' pk=school_details.pk %}">Update</a></p>
    ```

## Delete View
### views.py (delete def hrer)
* Import reverse_lazy to wait until get sucess reponse from db then redirect to list
```
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
```
### Make sure update url.py about delete form path with primary key
    ```
        path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete')
    ```
### Create a default delete confirmation template(this will get trigger if we tried to delete manually from Db)

    ```
        {% extends "basic_app/basic_app_base.html" %}

        {% block body_block %}
        <h1>Delete {{school.name }}?</h1>

        <form method="post">
        {% csrf_token %}
        <input type="submit" class="btn btn-danger" value="Delete">
        <a href="{% url 'basic_app:detail' pk=school.pk%} ">Cancel</a>

        </form>

        {% endblock %}

    ```
