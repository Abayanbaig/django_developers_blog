from django.test import TestCase
from myproject.forms import ProjectForm


class ProjectFormTest(TestCase):

    def test_project_form(self):
        form = ProjectForm(data={'name': 'Django Web Application', 'img': 'photos/website.jpg',
                                 'description': 'Nice Application', 'vote_total': 200, 'vote-ratio': 50})
        self.assertTrue(form.is_valid())
