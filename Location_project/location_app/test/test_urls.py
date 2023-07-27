from django.test import SimpleTestCase
from django.urls import reverse, resolve
from location_app.views import (
    sign_up_view,
    sign_out_view,
    add_location_data,
    delete_data,
    search_data,
    index_view,
    sign_in_view,
)


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse("sign_in")
        print(resolve(url))
        self.assertEquals(resolve(url).func, sign_in_view)
