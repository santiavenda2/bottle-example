# -*- coding: utf-8 -*-
import webtest
import unittest
import main
import collections

app = webtest.TestApp(main.app)


class BottleTestCase(unittest.TestCase):

    def test_home_page(self):
        response = app.get('/')
        self.assertEquals(response.status_int, 200)

    def test_hello_static_url(self):
        response = app.get('/hello')
        self.assertEquals(response.status_int, 200)

    def test_hello_static_url_with_slash(self):
        response = app.get('/hello/')
        self.assertEquals(response.status_int, 200)

    def test_hello_static_url_with_parameter(self):
        response = app.get('/hello/santiago')
        self.assertEquals(response.status_int, 200)
        self.assertEquals(response.body, "Hello santiago, how are you?")

    def test_hello_static_url_with_wrong_parameter(self):
        response = app.get('/hello/Santiago', expect_errors=True)
        self.assertEquals(response.status_int, 404)

    def test_login(self):
        params = collections.OrderedDict([
            ('username', 'santiago'),
            ('password', 'santiago')
        ])
        response = app.post('/login',  params=params)
        self.assertEquals(response.status_int, 200)


if __name__ == '__main__':
    unittest.main()
