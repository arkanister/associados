#!/usr/bin/env python
# encoding: utf-8
from django.test import TestCase
from app.members.forms import MemberForm
from app.members.models import Organization, City, User, Member


class MemberFormTest(TestCase):

    def setUp(self):
        self.data = {
        'full_name': 'Valder Gallo Jr',
        'organization': 'Home',
        'cpf': '94463643104',
        'email': 'valdergallo@gmail.com',
        'phone': '1199492911',
        'city': 'Sao Paulo',
        'state': 'SP',
        'category': '1',
        'relationship': 'think',
        'mailling': 1,
        'contact': 1,
        }
        self.form = MemberForm(self.data)
        self.form.is_valid()

    def test_clean_full_name_firstname(self):
        self.assertEqual(self.form.cleaned_data.get('first_name'), 'Valder')

    def test_clean_full_name_lastname(self):
        self.assertEqual(self.form.cleaned_data.get('last_name'), 'Gallo Jr')

    def test_clean_organization(self):
        self.assertIsInstance(self.form.cleaned_data.get('organization'), Organization)

    def test_clean_city(self):
        self.assertIsInstance(self.form.cleaned_data.get('city'), City)

    def test_save(self):
        new_user = self.form.save()
        self.assertIsInstance(new_user, User)
        self.assertTrue(new_user.member)

    def test_created_object_city(self):
        self.form.save()
        city = City.objects.get()
        self.assertEqual(city.name, self.data.get('city'))

    def test_created_object_organization(self):
        self.form.save()
        organization = Organization.objects.get()
        self.assertEqual(organization.name, self.data.get('organization'))

    def test_should_create_an_user(self):
        self.form.save()
        user = User.objects.get(email=self.data.get('email'))
        self.assertEqual(user.get_full_name(), self.data.get('full_name'))
