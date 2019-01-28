from django.test import TestCase
from workouts.models import Individual
import datetime

class IndividualTestCase(TestCase):
    def setUp(self):
        Individual.objects.create(user_name = "testuser", rec_ins_ts = datetime.datetime.now())

    def test_indiv_created(self):
        indiv = Individual.objects.get(user_name="testuser")
        user_name = indiv.user_name
        self.assertEqual(user_name, "testuser")


# Create your tests here.
