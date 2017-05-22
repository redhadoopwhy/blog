# coding=utf-8
from django.shortcuts import render,render_to_response
def index(request):
    return render_to_response('index.html')
def jianli(request):
    grqk = "- 姓名：王宏宇\n- 年龄：24\n- 毕业院系：衡水学院数学与计算机科学系\n- 个人邮箱：why@whysdomain.com\n- 联系电话：135 5249 3019/188 3286 9630\n- 求职意向：Linux运维工程师\n- 期望月薪：12k"
    grnl = "1. 硬件服务器方面：了解服务器安装，维护，有阿里云ESC公有云环境使用经验;\n2. 网络方面：了解TCP/IP协议，了解转发和路由;\n3. 操作系统方面：熟悉Redhat/CentOS6操作系统，包括安装，基本命令，服务，例如DNS，sshd，rsync，nfs，iptables，了解内核调优;\n4. WEB服务器方面：熟悉Apache，Nginx，PHP配置和优化项，了解Tomcat;\n5. 高可用和负载均衡方面：熟悉keepalived和heardbeat进行高可用配置，通过HAproxy，Nginx和LVS实现负载均衡和反向代理;\n6. 数据库方面：熟悉MySQL管理，优化和数据恢复，熟悉MongoDB，了解Memcache和redis;\n7. 大数据方面：熟悉hadoop生态圈组件，例如hadoop，hive，熟悉ELK日志分析，了解JVM调优;\n8. 编程方面：熟悉linux shell以及awk，sed，了解Python和Django web框架，了解部分前端技术;\n9. 自动化运维方面：熟悉saltstack进行批量部署，了解SVN和git版本控制;\n10. 监控方面：熟悉nagios和zabbix对包括设备，系统，网络，业务，服务，接口和流量等进行监控;\n11. 虚拟化方面：了解KVM和OpenStack，了解Docker;\n11. 个人能力方面：具备查阅英文官方文档的能力，用于实现需要解决的需求。"
    gzjl = "就职公司：北京红象云腾系统技术有限公司\n就职时间：2016年4月至今\n负责工作：项目运维，项目实施，项目性能测试\n \n 1. 资源卫星中心上百台大数据集群运维\n1.1 通过saltstack进行常规部署，批量执行;\n1.2 监控整个集群性能并保证集群业务正常运行;\n1.3 根据日志和监控对集群进行系统和硬件方面的维护。\n \n 2. 礼物说WEB集群运维 \n2.1 负责高可用LVS负载均衡和HAproxy反向代理的高可用web集群运维; \n2.2 监控集群流量和业务运行情况，在高峰期适当通过docker进行横向扩展; \n2.3 进行新版本业务灰度发布; \n2.4 测试环境的自动化搭建并配合开发总结业务情况。"
    zwpj = "  1. 工作细致，考虑周全，熟悉生产环境，根本没听说过rm和drop等操作；\n  2. 学习能力强，对新技术有探索欲望并能够运用到实际工作中并形成文档；\n 3. 具备查阅英文官方文档的能力；\n 4. 善于与同事和客户沟通，营造良好的氛围。"
    grxm = "- 个人博客:http://www.whysdomain.com/blog"
    return render(request,'jianli.html',{'grqk':grqk,'grnl':grnl,'gzjl':gzjl,'zwpj':zwpj,'grxm':grxm})
def me(request):
    why = "- 姓名：王宏宇\n- 英文简写：why\n- 研究方向：大数据，web服务，python自动化运维\n- 个人规划：成为一个Devops\n"
    work = "- 2016年4月至2017年5月就职于北京红象云腾系统技术有限公司"
    return render(request,'me.html',{'why':why,'work':work})
def page_404(request):
    return render_to_response('404.html')
