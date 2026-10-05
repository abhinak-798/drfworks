from django.shortcuts import get_object_or_404
from django.template.context_processors import request

from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, generics
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

# class MovieListCreate(APIView):
#     def get(self,request):
#         #qs
#         qs =Movie.objects.all()
#
#         #serializer instance
#         serializer_instance = MovieSerializer(qs, many=True)
#
#         #Responses
#         return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
#
#     def post(self, request):
#         form_data = request.data
#         serializer_instance = MovieSerializer(data=form_data)
#         if serializer_instance.is_valid():
#             # cleaned_data=serializer_instance.validated_data
#             # title=cleaned_data['title']
#
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors)
#
# #APIView for reading a specific record
# #APIView for updating a specific record
# #APIView for deleting a specific record
# class MovieRetrieveUpdateDelete(APIView):
#     def get(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(m)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def put(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(m,request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self,request,id):
#         e = get_object_or_404(Movie, id=id)
#         serializer_instance = MovieSerializer(e, request.data, partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         m.delete()
#         return Response({'message':'Deleted'})


#MIXIN CLASS
# from rest_framework import mixins,generics
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     def get(self, request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self, request,pk):
#         return self.update(request,pk)
#
#     def patch(self, request,pk):
#         return self.partial_update(request,pk)
#
#     def delete(self, request,pk):
#         return self.destroy(request,pk)


#GENERICS CLASS
# from rest_framework import generics
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer


#VIEWSETS
# from rest_framework import viewsets
# class MovieView(viewsets.ModelViewSet):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer



#SEARCH APIView
from django.db.models import Q
# class SearchAPIView(APIView):
    # def get(self,request):
    #
    #     #fetches data coming from request url
    #     data=self.request.query_params.get('serach')
    #
    #     #filters movie record having title matching with data
    #     m=Movie.objects.filter(Q(title__icontains=data) |
    #                            Q(director__icontains=data) |
    #                            Q(language__icontains=data))
    #
    #     if not m.exists():
    #         return Response({'message':'no record found'},status=status.HTTP_200_OK)
    #
    #     #converts the qs into native using Serializer class
    #     serializer_instance=MovieSerializer(m,many=True)
    #
    #     #return response as json using Response class
    #     return Response(serializer_instance.data,status=status.HTTP_200_OK)


from rest_framework.filters import SearchFilter
class SearchAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    filter_backends = [SearchFilter]

    search_fields=['title','director','language']

class RegisterAPIView(APIView):
    def post(self,request):

        form_data=request.data

        serializer_instance=UserSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)