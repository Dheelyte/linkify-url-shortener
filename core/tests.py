from django.test import TestCase
from .models import Link
from .serializers import LinkSerializer

# Create your tests here.

class LinkTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        data = {
            "link": "https://delight.com",
            "short_link_id": "link1"
        }
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        

    def test_get_link(self):
        link_obj = Link.objects.get(short_link_id="link1")
        self.assertEqual(link_obj.link, "https://delight.com")

    def test_get_short_link(self):
        link_obj = Link.objects.get(short_link_id="link1")
        self.assertEqual(link_obj.short_link_id, "link1")

    def test_get_absolute_url(self):
        link_obj = Link.objects.get(short_link_id="link1")
        self.assertEqual(link_obj.get_absolute_url(), "/link1/")

