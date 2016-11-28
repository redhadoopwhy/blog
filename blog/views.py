#coding=utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect

# Create your views here.
from blog.models import BlogPost
from blog.models import Family
from datetime import datetime

def blog_index(request):					      #主页显示
    blog_list = BlogPost.objects.all()
    dic_blog_list = {'blog_list': blog_list}
    return render(request, 'blog.html', dic_blog_list)
def blog_bond(request,blog_id=''):				      #内容显示
    blog_list_two = BlogPost.objects.get(id=blog_id)
    return render(request,'blog_every.html',{'blog_list_two':blog_list_two})
def blog_tag(request):						      #标签显示
    blog_list_tag = Family.objects.all() 
    return render(request, 'blog_tag.html',{'blog_list_tag':blog_list_tag} )
def blog_bond_tag(request,blog_tag=''):				      #按着标签显示
    blog_list_tag_two = BlogPost.objects.filter(family_id=blog_tag)     #一定要用filter，这是一对多的关系，另外数据库中没有family_name，存储的是Family中对应的family_id.
    return render(request,'blog_every_tag.html',{'blog_list_tag_two':blog_list_tag_two})
def blog_post(request):						      #添加blog
    blog_list_tag = Family.objects.all()
    return render(request,'blog_post.html',{'blog_list_tag':blog_list_tag})
def blog_post_add(request):
    body = request.POST.get('body')                                     #在前端通过POST发送body数据给后台
    title = request.POST.get('title')                                   #在前端通过POST发送title数据给后台
    family_id = request.POST.get('family_id')                           #在前端通过POST发送family数据给后台         
    timestamp = datetime.now()
#    family_name_all = Family.objects.all()                              #原先就有的tags
#    for tag in family_name_all:                                         #循环判断输入的标签是否存在，如果不存在就新建一个标签
#        if family==tag.family_name:
#            break
#        else:   
#            Family.objects.create(family_name=family)                                           
    blog=BlogPost.objects.create(title=title,                           #新建博客写入数据库中
                        body=body,
                        family_id=family_id,
                        timestamp=timestamp,                                                    
                        )
    id= BlogPost.objects.order_by('-timestamp')[0].id                   #查找最新文章的id                      
    return HttpResponseRedirect('/blog/%s' %id)                         #数据输入到数据库这是后台做的事，前端显示该博客的单篇博客详细内容比较合适
def blog_search(request):                                             #按内容搜索
    search_word = request.POST['searchword']
    blog_list_three = BlogPost.objects.all()
    search_result = []
    for i in blog_list_three:
        if search_word in i.title:
            search_result.append(i)                                      #append追加到list末尾
        elif search_word in i.body:
            search_result.append(i)                                      #append追加到list末尾
    search_status = "error" if len(search_result) == 0 else "success"
    result_length = len(search_result)
    return render(request,'search.html',{'search_word':search_word,'search_result':search_result,'search_status':search_status,'result_length':result_length})
