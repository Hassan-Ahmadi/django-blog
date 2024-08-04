# from django.shortcuts import redirect  
# from django.conf import settings

# class ComingSoonMiddleware:  
#     def __init__(self, get_response):  
#         self.get_response = get_response  

#     def __call__(self, request):  
#         # some conditions for redirections ...
#         if settings.MAINTENANCE_MODE:
#             return redirect('coming_soon')  
        
from django.shortcuts import reverse, redirect
from django.conf import settings


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")

        if settings.MAINTENANCE_MODE and path!= reverse("maintenance"):
            response = redirect(reverse("maintenance"))
            return response

        response = self.get_response(request)

        return response