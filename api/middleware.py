import jwt
from django.conf import settings
from django.http import JsonResponse

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.token_free_paths = [
            '/api/usuario-create',
            '/api/usuario-validar-contra',
            '/admin',
            '/static',
            '/favicon'
        ]
        self.links_permitidos_voluntario=[
            "/api/adopcion-update",
            "/api/adopcion-list",
            "/api/animal-list",
            "/api/adoptantes-list"
        ]

        self.links_permitidos_adoptante=[
            "/api/animal-list",
            "/api/adopcion-creacion-edicion-animal"
        ]

    def __call__(self, request):

        if any(request.path.startswith(path) for path in self.token_free_paths):
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            try:

                prefix, token = auth_header.split(' ')
                if prefix != 'Bearer':
                    raise ValueError("Invalid token prefix")


                diccionario=jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

                rol=diccionario["rol"]

                #print(rol)

                if(rol=="voluntario" and (not any(request.path.startswith(path) for path in self.links_permitidos_voluntario))): return JsonResponse({'detail': "No permitida call con ese rol"}, status=401)
                if(rol=="adoptante" and (not any(request.path.startswith(path) for path in self.links_permitidos_adoptante))): return JsonResponse({'detail': "No permitida call con ese rol"}, status=401)
     
                resp=self.get_response(request)

                return resp

            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ValueError) as e:
                return JsonResponse({'detail': str(e)}, status=401)

        return JsonResponse({'detail': "No estás presentando el token"}, status=401)
