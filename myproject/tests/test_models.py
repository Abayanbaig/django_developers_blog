from django.test import TestCase
from myproject.models import Project
from django.contrib.auth.models import User


class ProjectModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='priya')
        project = Project.objects.create(
            owner=user.profile, name='Django Application', img='/photos/pattern.jpg', vote_ratio=80)

    def test_name_maxlength(self):
        projectobj = Project.objects.get(id=1)
        name_len = projectobj._meta.get_field('name').max_length
        self.assertEqual(200, name_len)

    def test_object_name_is_name_and_vote_ratio(self):
        projobj = Project.objects.get(id=1)
        expected_val = f'{projobj.name}[{projobj.vote_ratio}]'
        self.assertEqual(str(projobj), expected_val)
