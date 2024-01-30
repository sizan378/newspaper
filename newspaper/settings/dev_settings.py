from .settings import *


INSTALLED_APPS += [
    'debug_toolbar',
    'drf_yasg',
]


MIDDLEWARE += [
   'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [                                              
    '127.0.0.1',                                              
]                                                             

def show_toolbar(request):                                    
    return True                                                

DEBUG_TOOLBAR_CONFIG = {                                      
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,                   
}                                                             

if DEBUG:                                                     
    import mimetypes                                                    
    mimetypes.add_type("application/javascript", ".js", True) 