from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


class TechReviewsApiView(APIView):
    serializer_class = ReviewSerializer
    permission_classes = []

    def get(self, request, pk):
        food = get_object_or_404(Tech, pk=pk)
        comments_data = self.serializer_class(
            food.reviews, many=True, context={"request": request}
        ).data

        return Response(data=comments_data)





class AddReviewView(CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    authentication_classes = [
        JWTAuthentication,
    ]

    def post(self, request, pk):
        tech = Tech.objects.get(pk=pk)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(tech=tech)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

