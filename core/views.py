from rest_framework.views import APIView
import random, string
from django.shortcuts import redirect, render
from .serializers import LinkSerializer
from .models import Link
from rest_framework.response import Response


class ShortenLink(APIView):
    """
    Create a short url for a given url
    """
    def shorten(self):
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=7))

    def get(self, request, *args):
        return render(request, 'index.html')

    def post(self, request):
        if not request.data["link"]:
            return Response({"error": "Add a link to shorten"}, status=409)
        short_link = request.data["short_link_id"] if request.data["short_link_id"] else None
        if short_link:
            accepted_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
            if any((char not in accepted_chars) for char in short_link):
                return Response({"error": "Invalid character found in new url"}, status=409)
            try:
                Link.objects.get(short_link_id=short_link)
                return Response("Short link already exists", status=409)
            except Link.DoesNotExist:
                serializer = LinkSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
        else:
            serializer = LinkSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(short_link_id=self.shorten())
                print(serializer.validated_data)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
    

class RedirectLink(APIView):
    """
    Redirect a short link to original link
    """
    def get(self, request, id):
        link = Link.objects.get(short_link_id=id)
        return redirect(link.link)
