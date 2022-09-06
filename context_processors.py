from django.apps import apps

def theme_config(request):
    return {'isu22': apps.get_app_config('iastate22theme')}