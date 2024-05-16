from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from .idreader import reader_id
from .models import Client
from .serializers import ClientSerializer
from uuid import uuid4
import django


class ClientIDCardViewSet(views.APIView):
    def post(self, request):
        try:
            img = request.data['photo']
        except KeyError:
            return Response({'error': 'Photo field is missing'}, status=status.HTTP_400_BAD_REQUEST)

        name = f'uploads/{uuid4()}.png'

        with open(name, 'wb') as f:
            f.write(img.read())

        try:
            data = reader_id(name)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            f.close()

        try:
            client = Client.objects.create(
                name=data['name'],
                surname=data['surname'],
                personal_number=data['personal_number'],
                nationality=data['nationality'],
                card_number=data['card_number'],
                date_of_birth=data['birth_date'],
                gender=data['gender'],
                expiration_date=data['expiration_date'],
            )
        except django.db.utils.IntegrityError:
            return Response({'error': 'Photo already exists'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(ClientSerializer(client).data, status=status.HTTP_201_CREATED)
