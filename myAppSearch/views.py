from django.shortcuts import render
from rest_framework.response import Response
from .models import Students
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StudentsSerializers
from django.http import Http404, HttpRequest
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your views here.
class StudentsAPI(APIView):
    def get(self, request):
        st = Students.objects.all()
        ss = StudentsSerializers(st, many=True)
        return Response(ss.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        ss = StudentsSerializers(data=request.data)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_201_CREATED)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentAPI(APIView):
    def get_by_id(self, id):
        try:
            st = Students.objects.get(id=id)
            return st
        except Students.DoesNotExist:
            raise Http404
    
    def get(self, request, id):
        sr = self.get_by_id(id)
        ss = StudentsSerializers(sr)
        return Response(ss.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        sr = self.get_by_id(id)
        ss = StudentsSerializers(sr, data=request.data)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_202_ACCEPTED)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        sr = self.get_by_id(id)
        ss = StudentsSerializers(sr, data=request.data, partial=True)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_202_ACCEPTED)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        sr = self.get_by_id(id)
        sr.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentsSearch(APIView):
    def post(self, request):
        # data = request.data
        # print(data)

        # search = data.get('search')
        search = request.body.decode('utf-8')

        print(request.COOKIES)
        
        print(request.get_host())

        print(search)

        search = str(search)
        xx = Students.objects.filter(Q(name__icontains=search) | Q(age__icontains=search) | Q(city__icontains=search) | Q(standards__icontains=search))
        if xx:
            ss = StudentsSerializers(xx, many=True)
            return Response(ss.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_204_NO_CONTENT)


# class StudentBySlugAPI(APIView):
#     def get_by_slug(self, slug):
#         try:
#             student = Students.objects.get(slug=slug)
#             return student
#         except Students.DoesNotExist:
#             raise Http404

#     def get(self, request, slug):
#         student = self.get_by_slug(slug)
#         serializer = StudentsSerializers(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class StudentsSearchN(APIView):
#     def get(self, request):
#         search_query = request.GET.get("search")
#         if search_query:
#             # Perform the search query using filter and Q objects
#             results = Students.objects.filter(
#                 Q(name__icontains=search_query) |
#                 Q(age__icontains=search_query) |
#                 Q(city__icontains=search_query) |
#                 Q(standards__icontains=search_query)
#             )
#             # Serialize the results
#             serializer = StudentsSerializers(results, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response([], status=status.HTTP_204_NO_CONTENT)


# def sam(request):
#     pass


# def search_models(request):
#     query = request.GET.get('query', '')  # Get the query parameter from the URL

#     if query:
#         # Search for models with names similar to the query
#         results = Students.objects.filter(Q(name__icontains=query))

#     else:
#         results = []

#     context = {
#         'query': query,
#         'results': results,
#     }

#     return render(request, 'search.html', context)
