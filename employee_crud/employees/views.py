
from django.shortcuts import get_object_or_404

from employees.models import Employee

from rest_framework.views import APIView
from rest_framework.response import Response

from employees.serializers import EmployeeSerializer
from rest_framework import status

#API view for reading all records
class EmployeeList(APIView):
    def get(self,request):
        qs=Employee.objects.all()
            #Reads all employee records from Employee table(query set(qs))

        serializer_instance=EmployeeSerializer(qs,many=True)
            #EmployeeSerializer converts qs into python native types

            #qs contains more than on record so we use many=True

        return Response(data=serializer_instance.data)
            #sends python native data as json using Response class


#APIView for creating new employee record
class EmployeeCreate(APIView):
    def post(self,request):
        #View receives data as request.data(client data--python native type)

        #Calls serializer class for deserialization,here we pass request.data as argument

        #after validation serializer saves data as model object inside db table

        serializer_instance=EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


#APIView for reading a specific record
class EmployeeDetail(APIView):
    def get(self,request,i):

        #Reads employee objects from model
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)

        #converts model object into python native using EmployeeSerializer
        serializer_instance=EmployeeSerializer(e)

        #Sends the response as json
        return Response(data=serializer_instance.data)

#APIView for deleting a specific record
class EmployeeDelete(APIView):
    def delete(self,request,i):
        e = get_object_or_404(Employee, id=i)
        e.delete()
        return Response({'message':'Deleted successfully'})


#APIView for updating an existing record(full updation)
class EmployeeUpdate(APIView):
    def put(self,request,i):

        e = get_object_or_404(Employee, id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()             #calls update() inside serializer class
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class EmployeePartialUpdate(APIView):
    def patch(self,request,i):

        e = get_object_or_404(Employee, id=i)
        serializer_instance=EmployeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()             #calls update() inside serializer class
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

