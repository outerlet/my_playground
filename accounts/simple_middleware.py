class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Before request')

        response = self.get_response(request)

        print('After response')

        return response
