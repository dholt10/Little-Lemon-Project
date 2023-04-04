from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def requests(self, request, pk):
        if request.method == 'GET':
            menu_item = Menu.objects.all()
            menu_serializer = MenuSerializer(menu_item, many=True)
            return Response(menu_serializer.data)
        elif request.method == 'POST':
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'PUT':
            put_serializer = MenuSerializer(menu_item, data=request.data)
            if put_serializer.is_valid():
                put_serializer.save()
                return Response(put_serializer.data)
            return Response(put_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            menu_to_delete = Menu.objects.get(pk=pk)
            menu_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Successful"})
        return JsonResponse({"message": "Error"})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return JsonResponse({"message": "This view is protected"})
