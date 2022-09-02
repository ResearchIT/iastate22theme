from django.apps import apps

def theme_config(request):
    return {'iastate22theme_config': apps.get_app_config('iastate22theme')}