import logging
from django.http import HttpResponse


logger = logging.getLogger('request_logger')


class MyMiddleware:
    def __init__(self, get_response):
        # print("This is init function inside __init__")
        self.get_response = get_response
        # x = self.get_response
        # print(x)
    
    def __call__(self, request):
        # print("This is call function inside __call__")
        response = self.get_response(request)
        # print(response)
        response['X-Custom-Header']='Hello from custom middleware'

        return response


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """capture the request information...!!!"""
        method = request.method
        path = request.path
        params = request.GET if method == 'GET' else request.POST
        headers = request.META

        """Log the request information...!!!"""
        logger.info(f"Request : {method} {path}")
        logger.info(f"Parameters : {params}")
        logger.info(f"Headers : {headers}")

        response = self.get_response(request)
        # print(f"response from middleware : {response}")
        return response


class SamMid:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Implement your authentication logic here
        if not request.user.is_authenticated:
            return HttpResponse("Unauthorized", status=401)
        
        response = self.get_response(request)
        return response


class Xmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(f"__init__ of Xmiddleware {self.get_response}")

    def __call__(self, request):
        response = self.get_response(request)
        print(f"__call__ of every request \n request : {request.method} \n response : {response.status_code}\n response : {response.charset}")
        print("__call__ of every request")
        
        # Request Object Attributes/Methods
        print(f"Request Method: {request.method}")
        print(f"Request Path: {request.path}")
        print(f"Request Headers (META): {request.META}")
        print(f"GET Parameters: {request.GET}")
        print(f"POST Data: {request.POST}")
        print(f"Cookies: {request.COOKIES}")
        print(f"User (if authenticated): {request.user}")
        print(f"Session Data: {request.session}")
        print(f"Uploaded Files: {request.FILES}")
        print(f"Is Secure (HTTPS): {request.is_secure()}")
        
        # Check for AJAX Request using HTTP_X_REQUESTED_WITH header
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        print(f"Is AJAX Request: {is_ajax}")

        # Response Object Attributes/Methods
        print(f"Response Status Code: {response.status_code}")
        # print(f"Response Content Type: {response.content_type}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Charset: {response.charset}")
        print(f"Response Content: {response.content}")
        print(f"Response Cookies: {response.cookies}")

        # Additional Response Methods
        response.set_cookie('samir', '8050', max_age=3600)  # Replace 'my_cookie' and 'cookie_value' with actual values

        print(f"cookies : {response.cookies}")
        
        print(f"Set Cookie Method: {response.set_cookie('samir', '8050')}")
        print(f"Delete Cookie Method: {response.delete_cookie('samir')}")
        # print(f"Redirect Method: {response.redirect()}")

         # Setting a Cookie

        # Deleting a Cookie (Commented out for reference)
        # response.delete_cookie('my_cookie')  # Replace 'my_cookie' with the actual cookie name

        # Redirecting
        # response = redirect('/new_url/')  # Replace '/new_url/' with the desired URL
        
        return response


class NitinKhatode:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
