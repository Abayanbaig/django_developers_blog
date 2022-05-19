# from django.test import TestCase
# from ..forms import ProjectForm
# from ..models import Project
# from django.contrib.auth.models import User
# # Create your tests here.


# class UnitTestCase(TestCase):

#     def test_home_page(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed('myprojecct/projects.html')

#     def test_project_form(self):
#         form = ProjectForm(data={'name': 'Django Web Application', 'img': 'photos/website.jpg',
#                                  'description': 'Nice Application', 'vote_total': 200, 'vote-ratio': 50})
#         self.assertTrue(form.is_valid())
# # ,'tags':('Ruby on Rails','Django'),

#     def test_project_model(self):
#         proj = Project()
#         proj.name = 'Django Application'
#         proj.img = 'photos/website.jpg'
#         proj.save()
#         proj_obj = Project.objects.get(name='Django Application')
#         self.assertEqual('photos/website.jpg', proj_obj.img)

#     def test_view_project(self):
#         User.objects.create(username='jaya')
#         user = User.objects.get(id=1)
#         proj = Project()
#         proj.owner = user.profile
#         proj.name = 'Django Application'
#         proj.img = 'photos/website.jpg'
#         proj.save()
#         proj_obj = Project.objects.get(name='Django Application')
#         response = self.client.get('/projects/')
#         self.assertContains(response, 'Django')


# class ProjectModelTest(TestCase):
#     def setUp(self):
#         user = User.objects.create(username='priya')
#         project = Project.objects.create(
#             owner=user.profile, name='Django Application', img='/photos/pattern.jpg', vote_ratio=80)

#     def test_name_maxlength(self):
#         projectobj = Project.objects.get(id=1)
#         name_len = projectobj._meta.get_field('name').max_length
#         self.assertEqual(200, name_len)

#     def test_object_name_is_name_and_vote_ratio(self):
#         projobj = Project.objects.get(id=1)
#         expected_val = f'{projobj.name}[{projobj.vote_ratio}]'
#         self.assertEqual(str(projobj), expected_val)
