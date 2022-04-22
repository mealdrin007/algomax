from django.shortcuts import render,redirect
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def movies():
    with open("C:/Users/hp/Desktop/programing/Djangoprojects/algomaxtest14/movielist/static/movies.json", encoding="utf8") as m:
        data = json.load(m)
        sort = [movie for movie in data if movie["year"] > 2015 & movie["year"] < 2018]
        return sort


class MoviesView(APIView):
    def get(self, request, *args, **kwargs):
        sort=movies()
        return Response({"sort": sort},status=status.HTTP_200_OK)

class MovieDetails(APIView):
    def get(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            datas=movies()
            sort=datas[int(id)-1]
            print(sort)
            return Response({"sort": sort},status=status.HTTP_200_OK)
        except:
            return Response({"msg":"invalid requesst"})


class Search(APIView):
    def get(self,request,*args,**kwargs):
        year=request.query_params.get("year")
        sort=movies()
        qs=[movie for movie in sort if(movie["year"]==int(year))]
        return Response({"sort":qs},status=status.HTTP_200_OK)