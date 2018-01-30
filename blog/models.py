#coding=utf-8
from django.db import models
from django.contrib import admin

# Create your models here.
class Family(models.Model):
    family_name = models.CharField(max_length=32, verbose_name='分类')
    def __unicode__(self):
        return self.family_name
    class Meta:                 
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'
class BlogPost(models.Model):
    title = models.CharField(max_length = 150, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    timestamp = models.DateTimeField(verbose_name='时间')
    family = models.ForeignKey(Family)
    def __unicode__(self):
        return self.title
    class Meta:					#时间倒序
        verbose_name = '博客'
        verbose_name_plural = '博客'
        ordering = ('-timestamp',)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')	#显示title和timesmapt

admin.site.register(Family)
admin.site.register(BlogPost,BlogPostAdmin)	
