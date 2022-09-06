Django app for the [IASTATE theme](https://www.theme.iastate.edu/)

# Set up

In apps.py of your project, create a subclass of Iastate22ThemeConfig and override any settings you want

```python
from iastate22theme.apps import Iastate22ThemeConfig

class TurtlebaseThemeConfig(Iastate22ThemeConfig):
    site_name = 'Turtlebase'
```

In settings.py of your project, add that class to your installed apps

```python
INSTALLED_APPS = [
    # ...
    'turtlebase.apps.TurtlebaseThemeConfig',
]
```

Then, also in settings.py, add this to your TEMPLATE settings:

```python
TEMPLATES = [
    {
        # ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                # ...
                'iastate22theme.context_processors.theme_config',
            ],
        },
    },
]
```

# Usage

A basic page template would look like this:

```django
{% extends "iastate22theme/base.html" %}

{% block content %}
<div class="outer-pad">
    <div class="text-content">
    Hello world
    </div>
</div>
{% endblock %}
```

You can override templates in your project by copying a template file from templates/iastate22theme to yourproject/templates/iastate22theme and modifying it.