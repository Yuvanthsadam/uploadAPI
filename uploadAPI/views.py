from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uploadAPI.models import profile
from uploadAPI.serializers import ProfileSerializer


class proListView(APIView):
    def get(self, request):
        pro = profile.objects.all()
        pro_serializer = ProfileSerializer(pro, many=True)
        resp1 = {
            "code": 1,
            "message": "GET list success",
            "result": pro_serializer.data
        }

        return Response(data=resp1, status=status.HTTP_200_OK)

    def post(self, request):
        # request.data.update(
        #     {"name": request.data["name"], "picture":  "https://upload-new.herokuapp.com/".join(request.data["picture"])})
        print(request.data["picture"])
        # myData = {
        #     "name": request.data["name"],
        #     "picture": "https://upload-new.herokuapp.com/"+request.data["picture"]
        # }
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp2 = {
                "code": 1,
                "message": "Post success",
                "result": serializer.data
            }
            # print(serializer.data)
            return Response(resp2, status=status.HTTP_201_CREATED)
        else:
            resp3 = {
                "code": 0,
                "message": "Post Unsuccess",
                "result": serializer.errors
            }
            return Response(resp3)


class proDetailView(APIView):

    def get(self, request, pk):
        try:
            pro = profile.objects.get(pk=pk)
        except profile.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        pro_serializer = ProfileSerializer(pro)
        return Response(pro_serializer.data)

    def put(self, request, pk):
        pro = profile.objects.get(pk=pk)
        pro_serializer = ProfileSerializer(pro, data=request.data)
        if pro_serializer.is_valid():
            pro_serializer.save()
            return Response(pro_serializer.data)
        else:
            return Response(pro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pro = profile.objects.get(pk=pk)
        pro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
