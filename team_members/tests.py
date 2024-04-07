from django.test import TestCase

# Create your tests here.
from .models import Member

from django.urls import reverse


def create_member(first_name, last_name, phone_number, email, role):
    return Member.objects.create(first_name=first_name, last_name=last_name,
                                 phone_number=phone_number, email=email, role=role)


class MemberListTests(TestCase):
    def test_no_members(self):
        response = self.client.get(reverse('team_members:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have 0 team members')

    def test_member_exists(self):
        member = create_member(first_name='first', last_name='last',
                               phone_number='1234567890', email='email@email.com',
                               role=Member.Role.REGULAR)

        response = self.client.get(reverse('team_members:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have 1 team members')
        self.assertQuerySetEqual(
            response.context["members_list"], [member])
