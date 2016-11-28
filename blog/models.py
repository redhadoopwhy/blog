#coding=utf-8
from django.db import models
from django.contrib import admin

# Create your models here.
class Family(models.Model):
    family_name = models.CharField(max_length=32)
    def __unicode__(self):
        return self.family_name
class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    family = models.ForeignKey(Family)
    def __unicode__(self):
        return self.title
    class Meta:					#时间倒序
        ordering = ('-timestamp',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')	#显示title和timesmapt
admin.site.register(Family)
admin.site.register(BlogPost,BlogPostAdmin)	
