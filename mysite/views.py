# coding=utf-8
from django.shortcuts import render,render_to_response
def index(request):
    return render_to_response('index.html')
def jianli(request):
    grqk = "- 姓名：王宏宇\n- 年龄：24\n- 毕业院系：衡水学院数学与计算机科学系\n- 个人邮箱：93216193@qq.com\n- 联系电话：13552493019/18832869630\n- 求职意向：Linux运维工程师\n- 期望月薪：12k"
    grnl = "1. 了解服务器安装，维护，熟悉Redhat6操作系统;\n2. 熟悉linux系统安装与服务，例如rsync，NFS，iptables;\n3. 熟悉LAMP/LNMP架构，LVS和keepalive高可用负载均衡及常用Apache，Nginx，反向代理和PHP优化项;\n4. 熟悉MySQL管理，优化和数据恢复，了解Memcache和redis;\n4. 熟悉hadoop生态圈组件，例如hadoop，hive;\n5. 熟悉linux shell以及awk，sed。熟悉Python,了解Django web框架，了解部分前端;\n6. 熟悉saltstack，nagios，了解zebbix。"
    gzjl = "就职公司：北京红象云腾系统技术有限公司\n就职时间：2016年4月至今\n负责工作：项目运维，项目实施，项目性能测试\n \n 1. 资源卫星中心上百台大数据集群运维\n1.1 通过saltstack进行常规部署，批量执行;\n1.2 监控整个集群性能并保证集群业务正常运行;\n1.3 根据日志和监控对集群进行系统和硬件方面的维护。\n \n 2. 资源卫星中心网站集群运维 \n2.1 构建高可用LVS负载均衡和nginx反向代理; \n2.2  \n2.3  \n"
    zwpj = "  1. 工作细致，考虑周全，熟悉生产环境，根本没听说过rm和drop等操作；\n  2. 学习能力强，对新技术有探索欲望并能够运用到实际工作中并形成文档；\n 3. 具备查阅英文官方文档的能力；\n 4. 善于与同事和客户沟通，营造良好的氛围；\n  5. 可以接受中短期的出差。\n"
    grxm = "- 个人博客:http://www.whysdomain.com/blog"
    return render(request,'jianli.html',{'grqk':grqk,'grnl':grnl,'gzjl':gzjl,'zwpj':zwpj,'grxm':grxm})
def me(request):
    why = "- 姓名：王宏宇\n- 英文简写：why\n- 研究方向：大数据，web服务，python自动化运维\n- 个人规划：成为一个Devops\n- 工作履历：2016年4月至今就职于北京红象云腾系统技术有限公司\n"
    return render(request,'me.html',{'why':why})
def page_404(request):
    return render_to_response('404.html')
