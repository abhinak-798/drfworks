from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
# class MovieList(APIView):
#     def get(self,request):
#         #qs
#         qs =Movie.objects.all()
#
#         #serializer instance
#         serializer_instance = MovieSerializer(qs, many=True)
#
#         #Responses
#         return Response(data=serializer_instance.data)
#
# class MovieCreate(APIView):
#     def post(self,request):
#         form_data=request.data
#         serializer_instance=MovieSerializer(data=form_data)
#         if serializer_instance.is_valid():
#             # cleaned_data=serializer_instance.validated_data
#             # title=cleaned_data['title']
#
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)

class MovieListCreate(APIView):
    def get(self,request):
        #qs
        qs =Movie.objects.all()

        #serializer instance
        serializer_instance = MovieSerializer(qs, many=True)

        #Responses
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)

    def post(self, request):
        form_data = request.data
        serializer_instance = MovieSerializer(data=form_data)
        if serializer_instance.is_valid():
            # cleaned_data=serializer_instance.validated_data
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)

#APIView for reading a specific record
#APIView for updating a specific record
#APIView for deleting a specific record
class MovieRetrieveUpdateDelete(APIView):
    def get(self,request,id):
        m=get_object_or_404(Movie,id=id)
        serializer_instance=MovieSerializer(m)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        m=get_object_or_404(Movie,id=id)
        serializer_instance=MovieSerializer(m,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        e = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializer(e, request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        m=get_object_or_404(Movie,id=id)
        m.delete()
        return Response({'message':'Deleted'})