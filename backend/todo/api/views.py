from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import Item
from api.serializers import ItemSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def item_list(request):
    if request.method == 'GET':

        items = Item.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            items = items.filter(title__icontains=title)
        
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        print('item post')
        item_data = JSONParser().parse(request)
        print(item_data)
        item_data['id'] = -1
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse(item_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Item.objects.all().delete()
        return JsonResponse({'message': '{} Items were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try: 
        item = Item.objects.get(pk=pk) 
    except Item.DoesNotExist: 
        return JsonResponse({'message': 'The item does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        item_serializer = ItemSerializer(item) 
        return JsonResponse(item_serializer.data) 
 
    elif request.method == 'PUT': 
        item_data = JSONParser().parse(request) 
        item_serializer = ItemSerializer(item, data=item_data) 
        if item_serializer.is_valid(): 
            item_serializer.save() 
            return JsonResponse(item_serializer.data) 
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        item.delete() 
        return JsonResponse({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
