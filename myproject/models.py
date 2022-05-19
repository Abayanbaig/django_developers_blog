
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
from users.models import Profile

# Create your models here.


class Project(models.Model):

    owner = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name='project')
    name = models.CharField(max_length=200)
    write_code = models.TextField(null=True, blank=True)
    
    about_project = models.CharField(max_length=5000 , null=True, blank=True)
    # Form doesn't require a value and database also doesn't require a value
    # OR default = timezone.now

    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    created = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag', blank=True)
    # photos dir will be created under media folder specified in MEDIA_ROOT variable in settings.py
    img = models.ImageField(upload_to='photos/%Y/%m/%d/',
                            default='photos/comment.png')

    published_at = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name + "["+str(self.vote_ratio)+"]"

    def status(self):
        print('Project -- Review Count Statistics')
        projects = Project.objects.all()
        data = []

        for proj in projects:
            proj_list = []
            review_count = proj.review_set.all().count()
            proj_list.append(proj)
            proj_list.append(review_count)
            data.append(proj_list)

        from tabulate import tabulate
        print(tabulate(data, headers=['Project Name', 'Review Count']))

    def getProfilesWhoseProjectNotUpdated(self):
        from datetime import datetime
        expected_date = datetime.today() - timedelta(days=15)
        projects = Project.objects.filter(created__lte=expected_date)
        idlist = []
        for p in projects:
            idlist.append(p.id)

        profiles = Profile.objects.filter(project__id__in=idlist)
        return profiles

    @property
    def reviewers(self):
        return self.review_set.all().values_list('owner__id', flat=True)

    @property
    def getVoteCount(self):

        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up')
        upCount = upVotes.count()
        totalCount = reviews.count()
        self.vote_total = totalCount
        self.vote_ratio = (upCount/totalCount)*100
        self.save()

        class Meta:
            ordering = ['created']


class Review(models.Model):
    VOTE_TYPE = [
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    ]

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['project', 'owner']]


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # projects = models.ManyToManyField(Project,blank=True)

    def __str__(self):
        return self.name
