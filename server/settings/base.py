import os
from pathlib import Path
# import amadeus
# settings from unfold documentation
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-r7ofvp1tmlv_@3lur2p6r^-+61l0*-vm63)'
DEBUG = True



INSTALLED_APPS = [
    "unfold.contrib.import_export",
    "import_export",
    'unfold',
    "unfold.contrib.forms",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # install apps
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
    'amadeus',
    'allauth',
    'allauth.account',
    # Enabled social auth
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    # all apps
    'customuser',
    'rental',
    'travel',
    #cloudinary
    'cloudinary_storage',
    'cloudinary',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dnvrnyqje',
    'API_KEY': '857873161588711',
    'API_SECRET': '6YIgETiUAhj3iKTg1eBPR4iSFow',
}

# amadeus = amadeus.Client(
#     client_id='AMADEUS_API_KEY',
#     client_secret='AMADEUS_API_SECRET'
# )

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = 'server.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'


UNFOLD = {
     "SITE_TITLE": "Travel app",
     "SITE_HEADER": "",
     "SITE_URL": "/",
     # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
     "SITE_ICON": {
         "light": lambda request: static("icon-light.svg"),  # light mode
         "dark": lambda request: static("icon-dark.svg"),  # dark mode
     },
     # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    "SITE_LOGO": {
         "light": lambda request: static("logo-light.svg"),  # light mode
         "dark": lambda request: static("logo-dark.svg"),  # dark mode
     },

    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.svg"),
        },
    ],
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
    
    
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    # "EXTENSIONS": {
    #     "modeltranslation": {
    #         "flags": {
    #             "en": "🇬🇧",
    #             "fr": "🇫🇷",
    #             "nl": "🇧🇪",
    #         },
    #     },
    # },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation travel"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "home",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    },

                    {
                        "title": _("CustomUser"),
                        "icon": "person", # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:customuser_customuser_changelist"),
                        # "permission": "customuser.manage_user",
                        
                    },

                    {
                        "title": _("Travel"),
                        "icon": "flight_takeoff", # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:travel_airline_changelist"),
                        # "permission": "travel.view_travel",
                    
                    }
                    
                    # {
                    #     "title": _("Staff"),
                    #     "icon": "user-tie",
                    #     "link": reverse_lazy("admin:index"),
                    #     "permission": "customuser.manage_staff",
                    #     "badge": "Staff",
                    #     },

                    # {
                    #     "title": _("Flights"),
                    #     "icon": "airplane",
                    #     "link": reverse_lazy("admin:index"),                  
                    #     "permission": "customuser.view_flights_and_airlines",
                    # },
                    # {
                    #     "title": _("Airlines"),
                    #     "icon": "plane-departure",
                    #     "link": reverse_lazy("admin:index"),               
                    #     },
                    # {
                    #     "title": _("Hotel and Lodging"),
                    #     "icon": "hotel",
                    #     "link": reverse_lazy("admin:index"),                 
                    #     "permission": "customuser.view_hotel_and_lodging_prices",
                    # },
                    # {
                    #     "title": _("Transport and Transport Fair"),
                    #     "icon": "bus",
                    #     "link": reverse_lazy("admin:index"),
                    # },
                    # {
                    #     "title": _("Payments"),
                    #     "icon": "credit-card",
                    #     "link": reverse_lazy("admin:index"), 
                    #     "permission": "customuser.view_payments",
                    # },

                    # {
                    #     "title": _("Holiday_Plans"),
                    #     "icon": "calendar-alt",
                    #     "link": reverse_lazy("admin:index"),
                    #     "permission": "customuser.view_holiday_plans",
                    #     "badge": "holiday",
                    #     },
            
                   
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:app_label_model_name_changelist"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}


# def dashboard_callback(request, context):
#     """
#     Callback to prepare custom variables for index template which is used as dashboard
#     template. It can be overridden in application by creating custom admin/index.html.
#     """
#     context.update(
#         {
#             "sample": "example",  # this will be injected into templates/admin/index.html
#         }
#     )
#     return context


# def environment_callback(request):
#     """
#     Callback has to return a list of two values represeting text value and the color
#     type of the label displayed in top right corner.
#     """
#     return ["Production", "danger"] # info, danger, warning, success


# def badge_callback(request):
#     return 3

# def permission_callback(request):
#     return request.user.has_perm("sample_app.change_model")
