from django.test import TestCase

from .models import Person


class DemoTest(TestCase):
    def test_index(self):
        Person.objects.create(name='John', date_of_birth='1957-06-01')
        Person.objects.create(name='Sarah', date_of_birth='1975-01-06')
        rsp = self.client.get('/')
        self.assertContains(rsp, 'Found records for 2 people')
        self.assertContains(rsp, 'John')
        self.assertContains(rsp, 'Sarah')

    def test_index_with_no_people(self):
        rsp = self.client.get('/')
        self.assertContains(rsp, 'Found no records')
