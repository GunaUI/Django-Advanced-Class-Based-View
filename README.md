# Django Advanced Class Based View
## Detailed view and List view
### models.py (Create models here)
```
    class School(models.Model):
        name = models.CharField(max_length=256)
        principal = models.CharField(max_length=256)
        location = models.CharField(max_length=256)

        def __str__(self):
            return self.name
            
    class Student(models.Model):
        name = models.CharField(max_length=256)
        age = models.PositiveIntegerField()
        school = models.ForeignKey(School,related_name='students')

        def __str__(self):
            return self.name

```

### admin.py
* Inform admin about newly created model
```
from django.contrib import admin
from basic_app.models import School,Student

admin.site.register(School)
admin.site.register(Student)  
```
### Do migrations 3 steps (refer django)
### Create a “superuser (refer django)
### Run server

### Create Views (views.py)

```
    class SchoolListView(ListView):
        # If you don't pass in this attribute,
        # Django will auto create a context name
        # for you with object_list!
        # Default would be 'school_list'

        # Example of making your own:
        # context_object_name = 'schools'
        
        model = models.School

    class SchoolDetailView(DetailView):
        model = models.School
        template_name = 'basic_app/school_detail.html'
```

### Add navigations templates in base.html
### Extend block code in school_list.html
    ```
        {% extends "basic_app/basic_app_base.html" %} 
        {% block body_block %}
        <div class="jumbotron">

            <h1>Welcome to the List of Schools Page!</h1>
            #school_list name created by ListView in views.py
            #if you need userdefined name you could add context_object_name (refer views.py)
            <ol>
                {% for school in school_list %}
                <h2>
                    <li><a href="{{school.id}}/">{{school.name}} </a></li>
                </h2>
                {% endfor %}
            </ol>

        </div>


        {% endblock %}
    ```
### Extend template in school_details.html
    ```
        {% extends "basic_app/basic_app_base.html" %}
        {% block body_block %}
        <div class="jumbotron">
            <h1>Welcome to the School Detail Page</h1>
            <h2>School Details:</h2>
            <p>Id_num: {{school_details.id}}</p>
            <p>Name: {{school_details.name}}</p>
            <p>Principal: {{school_details.principal}}</p>
            <p>Location: {{school_details.location}}</p>
            <h3>Students:</h3>
            # here students.all taken from related name of sudent detail models (refer models.py)
            {% for student in school_details.students.all %}
                <p>{{student.name}} who is {{student.age}} years old.</p>
            {% endfor %}

        </div>
        <div class="container">
            <p><a class='btn btn-warning' href="{% url 'basic_app:update' pk=school_details.pk %}">Update</a></p>

        </div>

        {% endblock %}
    ```
### intimate urlpatterns about new screens in apps url.py
    ```
        from django.urls import path
        from basic_app import views

        app_name = 'basic_app'

        urlpatterns = [
            path('',views.SchoolListView.as_view(),name='list'),
            path('school/<int:pk>/',views.SchoolDetailView.as_view(),name='detail')
        ]
    ```
#### Next Branch : django-crud
