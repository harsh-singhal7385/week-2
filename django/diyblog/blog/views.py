from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Blog


value = ""

def index(request):
    return render(request, "blog/index.html")

def blogList(request ):
    data = Blog.objects.all().order_by('datetime').reverse()
    context = {"data" : data}
    return render(request, "blog/blogList.html", context)

def authorList(request):
    data = Blog.objects.all().order_by('author_name')
    context = {"data" : data}
    return render(request, "blog/authorList.html",context)

def createBlog(request):
    if request.method == 'POST':
        print(" post request received")
        author_id = request.POST['author-id']
        blog_id = request.POST['blog-id']
        blog_title = request.POST['blog-title']
        blog_description = request.POST['blog-description']
        author_name = request.POST['author-name']
        blog = Blog(blog_id = blog_id, blog_title = blog_title, blog_description = blog_description, author_id = author_id, author_name = author_name)
        blog.save()
        return redirect( "/blog/blogs/")
    
    else:
        print("GET request received")
        return render(request, "blog/create.html")

def updateBlog(request):  
    if request.method == 'POST':
        author_id = request.POST['getauthorid']
        author_name = request.POST['getauthorname']
        data = Blog.objects.filter(author_id = author_id , author_name = author_name).first() 
        if data.author_id == author_id and data.author_name == author_name:
            value = author_id 
            print(value)
            return redirect( f"/blog/update/{value}/")
        else:
            print(" Invalid data found / no access granted ")
            render(request, "blog/update.html")
    
    return render(request, "blog/update.html")


def updateBlogData(request,slug):
    if request.method == 'POST':
        print(" post request received")
        author_id = request.POST['author-id']
        blog_id = request.POST['blog-id']
        blog_title = request.POST['blog-title']
        blog_description = request.POST['blog-description']
        author_name = request.POST['author-name']
        data = Blog.objects.filter(author_id = author_id , author_name = author_name).first()
        data.blog_title = blog_title
        data.blog_description = blog_description
        data.save()
        return redirect( "/blog/blogs/")
    data = Blog.objects.filter(author_id = slug).first()
    context = {"data" : data}
    return render(request, "blog/updateId.html", context)


def deleteBlog(request):  
    if request.method == 'POST':
        author_id = request.POST['getauthoriddel']
        author_name = request.POST['getauthornamedel']
        data = Blog.objects.filter(author_id = author_id , author_name = author_name).first() 
        if data.author_id == author_id and data.author_name == author_name:
            value = author_id 
            print(value)
            return redirect( f"/blog/delete/{value}/")
        else:
            print(" Invalid data found / no access granted ")
            return render(request, "blog/delete.html")

    return render(request, "blog/delete.html")


def deleteBlogData(request,slug):
    if request.method == 'POST':
        print(" post request received")
        # author_id = request.POST['author-id']
        blog_id = request.POST['blog-id']
        # author_name = request.POST['author-name']
        data = get_object_or_404(Blog, blog_id = blog_id )
        data.delete()
        return redirect( "/blog/blogs/")
    data = Blog.objects.filter(author_id = slug).first()
    context = {"data" : data}
    return render(request, "blog/deleteId.html", context)

    

def searchBlog(request):
    return render(request, "blog/search.html")

def getBlogId(request):
    if request.method == 'POST':
        blog_id = request.POST['getblog']
        value = blog_id 
        print(value)
        return redirect( f"/blog/{value}/")
    return render(request, "blog/getBlogId.html")

def getBlogById(request,slug):
    data = Blog.objects.filter(blog_id = slug) 
    print(data)
    context = {"data" : data }
    return render(request, "blog/getBlogById.html" , context)

def getAuthorById(request,slug):
    
    data = Blog.objects.filter(author_id = slug) 
    print(data)
    context = {"data" : data }
    return render(request, "blog/getAuthorById.html" , context)

def getAuthorId(request):
    
    if request.method == 'POST':
        author_id = request.POST['getblogauthor']
        value = author_id 
        print(value)
        return redirect( f"/blog/blogger/{value}/")
    return render(request, "blog/getAuthorId.html")
