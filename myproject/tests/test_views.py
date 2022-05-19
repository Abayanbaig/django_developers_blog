from django.test import TestCase
from django.contrib.auth.models import User
from myproject.models import Project


class ProjectViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='jaya', password='jaya@123')
        user.save()  # Profile will be created automatically

        proj = Project()
        proj.owner = user.profile
        proj.name = 'Django Application'
        proj.img = 'photos/website.jpg'
        proj.save()

    def test_view_project(self):
        user = User.objects.get(id=1)
        proj_obj = Project.objects.get(name='Django Application')
        response = self.client.get('/projects/')
        self.assertContains(response, proj_obj.name)
