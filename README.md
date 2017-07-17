# django-multidomain
App for multi domain in django. Python2.x, Python3.x, Django>=1.4

Add request.host with subdomain value or None

Quick start
-----------

1. Add "multidomain" to your INSTALLED_APPS setting like this:
```
      INSTALLED_APPS = (
          ...
          'multidomain',
      )
```
2. Include the 'multidomain.middleware.GetDomainMiddleware' MIDDLEWARE in your project settings.py like this:
```
      MIDDLEWARE = [
          ...
          'multidomain.middleware.GetDomainMiddleware',
      ]
```
3. Run `python manage.py migrate` to create the multidomain models.


TODO:
1) Localization
2) Many-Level domain
3) Docs
4) ...
