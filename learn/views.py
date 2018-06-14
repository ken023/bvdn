from django.shortcuts import render

# Create your views here.
def learnHome(request):
    # 实例一: 显示一个基本的字符串在网页上
    #view_string = u"我从view打印string 到template"
    #return render(request, 'learn/learnHome.html', {'template_string': view_string})

    #实例二: 讲解了基本的 for 循环 和 List内容的显示
    # View_List = ["HTML", "CSS", "jQuery", "Python", "Django"]
    #return  render(request,'learn/learnHome.html',{'template_list': View_List})

    # 实例三，显示字典中内容：
    # view_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    # return  render(request, 'learn/learnHome.html', {'template_list': View_List, 'template_dict':view_dict})

    # 实例四，在模板进行条件判断和 for 循环的详细操作：
    view_list = map(str, range(100))  #一个长度为100的list
    return render(request, 'learn/learnHome.html', {'template_list':view_list})


