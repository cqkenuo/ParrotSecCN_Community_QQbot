import json
import time
import grequests
import requests


class gwhatweb:
    def __init__(self, url):
        self.url = url
        self.time = 0

    def whatweb(self):
        url = 'http://whatweb.bugscaner.com/what/'
        start = time.clock()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Referer': 'http://whatweb.bugscaner.com/look/'}
        cocokies = {'saeut': 'CkMPHlqbqdBQWl9NBG+uAg=='}
        new_url = self.url.strip(
            '/').replace('http://', '').replace('https://', '')
        data = {
            'url': new_url,
            'hash': '0eca8914342fc63f5a2ef5246b7a3b14_7289fd8cf7f420f594ac165e475f1479'}
        content = json.loads(
            requests.post(
                url,
                headers=headers,
                data=data).text)
        end = time.clock()
        self.time = end - start
        if content['cms']:
            return {
                'total': 1424,
                'url': self.url,
                'result': content['cms'],
                'time': '%.3f s' % self.time}
        else:
            return {
                'total': 1424,
                'url': self.url,
                'result': '未知CMS',
                'time': '%.3f s' % self.time}


# whatweb("http://www.dedecms.com").scan() # return {'total': 1424, 'url':
# 'http://www.dedecms.com', 'result': 'DedeCMS(织梦)', 'time': '5.364 s'}


# 端口扫描
class portscan:
    def __init__(self, address, port):
        # port should be [80,81,82,83] or [21,80,3306]
        self.address = address
        self.port = port
        self.result = []

    def scan(self):
        tasks = [
            grequests.post(
                "http://tools.hexlt.org/api/portscan",
                json={
                    "ip": self.address,
                    "port": port}) for port in self.port]
        res = grequests.map(tasks, size=30)
        for i in res:
            result = i.json()
            if result['status']:
                self.result.append(result['port'])
        return self.result


'''

portscan("localhost", [21, 80, 81, 443, 5000, 8000]).scan()  # return [80, 443, 8000]

'''

# 漏洞检测


class exploit:
    def __init__(self, url="", keyword=""):
        self.url = url
        self.keyword = keyword
        self.poclist = {}
        self.cmspocdict = ["泛微OA downfile.php 任意文件下载漏洞",
                           "泛微OA 数据库配置泄露",
                           "phpok res_action_control.php 任意文件下载(需要cookies文件)",
                           "phpok api.php SQL注入漏洞",
                           "phpok remote_image getshell漏洞",
                           "jeecg 重置admin密码",
                           "typecho install.php反序列化命令执行",
                           "Dotnetcms(风讯cms)SQL注入漏洞",
                           "韩国autoset建站程序phpmyadmin任意登录漏洞",
                           "phpstudy探针",
                           "phpstudy phpmyadmin默认密码漏洞",
                           "Discuz论坛forum.php参数message SSRF漏洞",
                           "Discuz X3 focus.swf flashxss漏洞",
                           "Discuz! X2.5 物理路径泄露漏洞",
                           "Discuz问卷调查参数orderby注入漏洞",
                           "Hishop系统productlist.aspx SQL注入",
                           "亿邮邮箱弱口令列表泄露",
                           "亿邮Email Defender系统免登陆DBA注入",
                           "亿邮邮件系统重置密码问题暴力破解",
                           "亿邮mail5 user 参数kw SQL注入",
                           "金蝶办公系统任意文件下载",
                           "金蝶协同平台远程信息泄露漏洞",
                           "金蝶AES系统Java web配置文件泄露",
                           "金蝶EAS任意文件读取",
                           "乐语客服系统任意文件下载漏洞",
                           "smartoa 多处任意文件下载漏洞",
                           "urp查询接口曝露",
                           "URP越权查看任意学生课表、成绩(需登录)",
                           "URP综合教务系统任意文件读取",
                           "pkpmbs工程质量监督站信息管理系统SQL注入",
                           "pkpmbs建设工程质量监督系统注入",
                           "pkpmbs建设工程质量监督系统SQL注入",
                           "帝友P2P借贷系统无需登录SQL注入漏洞",
                           "帝友P2P借贷系统任意文件读取漏洞",
                           "iGenus邮件系统一处无需登录的任意代码执行",
                           "iGenus邮箱系统login.php 参数Lang任意文件读取",
                           "iGenus邮箱系统管理中心sys/login.php 参数Lang任意文件读取",
                           "live800客服系统downlog任意文件下载",
                           "live800在线客服系统loginAction SQL注入漏洞",
                           "live800在线客服系统多处SQL注入GETSHELL漏洞",
                           "live800在线客服系统XML实体注入漏洞",
                           "Onethink 参数category SQL注入",
                           "ThinkPHP 代码执行漏洞",
                           "汇思学习管理系统任意文件下载",
                           "Cyberwisdom wizBank学习管理平台SQL注入漏洞",
                           "domino_unauth未授权漏洞",
                           "宏景EHR系统多处SQL注入",
                           "汇能群管理系统SQL注入",
                           "汇文软件图书管理系统ajax_asyn_link.old.php任意文件读取",
                           "汇文软件图书管理系统ajax_asyn_link.php任意文件读取",
                           "汇文软件图书管理系统ajax_get_file.php任意文件读取",
                           "通元建站系统用户名泄露漏洞",
                           "metinfo5.0 getpassword.php两处时间盲注漏洞",
                           "用友ICC struts2远程命令执行",
                           "V2视频会议系统某处SQL注射、XXE漏洞(可getshell)",
                           "政府采购系统eweb编辑器默认口令Getshell漏洞",
                           "RAP接口平台struts远程代码执行",
                           "虹安DLP数据泄露防护平台struts2远程命令执行",
                           "九羽数字图书馆struts远程命令执行",
                           "垚捷电商平台通用struts命令执行",
                           "Digital-Campus数字校园平台LOG文件泄露",
                           "Digital-Campus2.0数字校园平台Sql注射",
                           "jeecms download.jsp 参数fpath任意文件下载",
                           "shopex敏感信息泄露",
                           "动科(dkcms)默认数据库漏洞",
                           "FineCMS免费版文件上传漏洞",
                           "DaMall商城系统sql注入",
                           "大汉版通JCMS数据库配置文件读取漏洞",
                           "大汉downfile.jsp 任意文件下载",
                           "大汉VerfiyCodeServlet越权漏洞",
                           "PHP168 login.php GETSHELL漏洞",
                           "dedecms版本探测",
                           "dedecms search.php SQL注入漏洞",
                           "dedecms trace爆路径漏洞",
                           "dedecms download.php重定向漏洞",
                           "dedecms recommend.php SQL注入",
                           "umail物理路径泄露",
                           "U-Mail邮件系统sessionid访问",
                           "metinfo v5.3sql注入漏洞",
                           "用友致远A6协同系统SQL注射union可shell",
                           "用友致远A6协同系统多处SQL注入",
                           "用友致远A6协同系统敏感信息泄露&SQL注射",
                           "用友致远A6协同系统数据库账号泄露",
                           "用友致远A6 test.jsp SQL注入",
                           "用友CRM系统任意文件读取",
                           "用友EHR 任意文件读取",
                           "用友优普a8 CmxUserSQL时间盲注入",
                           "用友a8 log泄露",
                           "用友a8监控后台默认密码漏洞",
                           "用友致远A8协同系统 blind XML实体注入",
                           "用友GRP-U8 sql注入漏洞",
                           "用友u8 CmxItem.php SQL注入",
                           "用友FE协作办公平台5.5 SQL注入",
                           "用友EHR系统 ResetPwd.jsp SQL注入",
                           "用友nc NCFindWeb 任意文件下载漏洞",
                           "fsmcms p_replydetail.jsp注入漏洞",
                           "FSMCMS网站重装漏洞",
                           "FSMCMS columninfo.jsp文件参数ColumnID SQL注入",
                           "qibocms知道系统SQL注入",
                           "qibo分类系统search.php 代码执行",
                           "qibocms news/js.php文件参数f_idSQL注入",
                           "qibocms s.php文件参数fids SQL注入",
                           "依友POS系统登陆信息泄露",
                           "浪潮行政审批系统十八处注入",
                           "浪潮ECGAP政务审批系统SQL注入漏洞",
                           "五车图书管系统任意下载",
                           "五车图书管系统kindaction任意文件遍历",
                           "Gobetters视频会议系统SQL注入漏洞",
                           "LBCMS多处SQL注入漏洞",
                           "Euse TMS存在多处DBA权限SQL注入",
                           "suntown未授权任意文件上传漏洞",
                           "Dswjcms p2p网贷系统前台4处sql注入",
                           "skytech政务系统越权漏洞",
                           "wordpress AzonPop插件SQL注入",
                           "wordpress 插件shortcode0.2.3 本地文件包含",
                           "wordpress插件跳转",
                           "wordpress 插件WooCommerce PHP代码注入",
                           "wordpress 插件mailpress远程代码执行",
                           "wordpress admin-ajax.php任意文件下载",
                           "wordpress rest api权限失效导致内容注入",
                           "wordpress display-widgets插件后门漏洞",
                           "Mallbuilder商城系统SQL注入",
                           "efuture商业链系统任意文件下载",
                           "kj65n煤矿远程监控系统SQL注入",
                           "票友机票预订系统6处SQL注入",
                           "票友机票预订系统10处SQL注入",
                           "票友机票预订系统6处SQL注入(绕过)",
                           "票友机票预订系统6处SQL注入2(绕过)",
                           "票友票务系统int_order.aspx SQL注入",
                           "票友票务系统通用sql注入",
                           "中农信达监察平台任意文件下载",
                           "连邦行政审批系统越权漏洞",
                           "北斗星政务PostSuggestion.aspx SQL注入",
                           "TCExam重新安装可getshell漏洞",
                           "合众商道php系统通用注入",
                           "最土团购SQL注入",
                           "时光动态网站平台(Cicro 3e WS) 任意文件下载",
                           "华飞科技cms绕过JS GETSHELL",
                           "IWMS系统后台绕过&整站删除",
                           "农友政务系统多处SQL注入",
                           "农友政务系统Item2.aspx SQL注入",
                           "农友政务ShowLand.aspx SQL注入",
                           "农友多处时间盲注",
                           "某政府采购系统任意用户密码获取漏洞",
                           "铭万事业通用建站系统SQL注入",
                           "铭万B2B SupplyList SQL注入漏洞",
                           "铭万门户建站系统ProductList SQL注入",
                           "xplus npmaker 2003系统GETSHELL",
                           "xplus通用注入",
                           "workyi人才系统多处注入漏洞",
                           "菲斯特诺期刊系统多处SQL注入",
                           "东软UniPortal1.2未授权访问&SQL注入",
                           "PageAdmin可“伪造”VIEWSTATE执行任意SQL查询&重置管理员密码",
                           "SiteFactory CMS 5.5.9任意文件下载漏洞",
                           "璐华企业版OA系统多处SQL注入",
                           "璐华OA系统多处SQL注入",
                           "璐华OA系统多处SQL注入3",
                           "GN SQL Injection",
                           "JumboECMS V1.6.1 注入漏洞",
                           "joomla组件com_docman本地文件包含",
                           "joomla 3.7.0 core SQL注入",
                           "北京网达信联电子采购系统多处注入",
                           "Designed by Alkawebs SQL Injection",
                           "一采通电子采购系统多处时间盲注",
                           "启博淘店通标准版任意文件遍历漏洞",
                           "PSTAR-电子服务平台SQL注入漏洞",
                           "PSTAR-电子服务平台isfLclInfo注入漏洞",
                           "PSTAR-电子服务平台SQL注入漏洞",
                           "TRS(拓尔思) wcm pre.as 文件包含",
                           "TRS(拓尔思) 网络信息雷达4.6系统敏感信息泄漏到进后台",
                           "TRS(拓尔思) 学位论文系统papercon处SQL注入",
                           "TRS(拓尔思) infogate插件 blind XML实体注入",
                           "TRS(拓尔思) infogate插件 任意注册漏洞",
                           "TRS(拓尔思) was5配置文件泄露",
                           "TRS(拓尔思) was5 download_templet.jsp任意文件下载",
                           "TRS(拓尔思) wcm系统默认账户漏洞",
                           "TRS(拓尔思) wcm 6.x版本infoview信息泄露",
                           "TRS(拓尔思) was40 passwd.htm页面泄露",
                           "TRS(拓尔思) was40 tree导航树泄露",
                           "TRS(拓尔思) ids身份认证信息泄露",
                           "TRS(拓尔思) wcm webservice文件写入漏洞",
                           "易创思ECScms MoreIndex SQL注入",
                           "金窗教务系统存在多处SQL注射漏洞",
                           "siteserver3.6.4 background_taskLog.aspx注入",
                           "siteserver3.6.4 background_log.aspx注入",
                           "siteserver3.6.4 user.aspx注入",
                           "siteserver3.6.4 background_keywordsFilting.aspx注入",
                           "siteserver3.6.4 background_administrator.aspx注入",
                           "NITC营销系统suggestwordList.php SQL注入",
                           "NITC营销系统index.php SQL注入",
                           "南大之星信息发布系统DBA SQL注入",
                           "蓝凌EIS智慧协同平台menu_left_edit.aspx SQL注入",
                           "天柏在线培训系统Type_List.aspx SQL注入",
                           "天柏在线培训系统TCH_list.aspx SQL注入",
                           "天柏在线培训系统Class_Info.aspx SQL注入",
                           "天柏在线培训系统St_Info.aspx SQL注入",
                           "安财软件GetXMLList任意文件读取",
                           "安财软件GetFile任意文件读取",
                           "安财软件GetFileContent任意文件读取",
                           "天津神州助平台通用型任意下载",
                           "ETMV9数字化校园平台任意下载",
                           "安脉grghjl.aspx 参数stuNo注入",
                           "农友多处时间盲注",
                           "某政府通用任意文件下载",
                           "师友list.aspx keywords SQL注入",
                           "speedcms list文件参数cid SQL注入",
                           "卓繁cms任意文件下载漏洞",
                           "金宇恒内容管理系统通用型任意文件下载漏洞",
                           "任我行crm任意文件下载",
                           "易创思教育建站系统未授权访问可查看所有注册用户",
                           "wecenter SQL注入",
                           "shopnum1 ShoppingCart1 SQL注入",
                           "shopnum1 ProductListCategory SQL注入",
                           "shopnum1 ProductDetail.aspx SQL注入",
                           "shopnum1 GuidBuyList.aspx SQL注入",
                           "好视通视频会议系统(fastmeeting)任意文件遍历",
                           "远古流媒体系统两处SQL注入",
                           "远古 pic_proxy.aspx SQL注入",
                           "远古流媒体系统  GetCaption.ashx注入",
                           "shop7z order_checknoprint.asp SQL注入",
                           "dreamgallery album.php SQL注入",
                           "IPS Community Suite <= 4.1.12.3 PHP远程代码执行",
                           "科信邮件系统login.server.php 时间盲注",
                           "shopNC B2B版 index.php SQL注入",
                           "南京擎天政务系统 geren_list_page.aspx SQL注入",
                           "学子科技诊断测评系统多处未授权访问",
                           "Shadows-IT selector.php 任意文件包含",
                           "皓翰数字化校园平台任意文件下载",
                           "phpcms digg_add.php SQL注入",
                           "phpcms authkey泄露漏洞",
                           "phpcms2008 flash_upload.php SQL注入",
                           "phpcms2008 product.php 代码执行",
                           "phpcms v9.6.0 SQL注入",
                           "phpcms 9.6.1任意文件读取漏洞",
                           "phpcms v9 flash xss漏洞",
                           "seacms search.php 代码执行",
                           "seacms 6.45 search.php order参数前台代码执行",
                           "seacms search.php 参数jq代码执行",
                           "安脉学生管理系统10处SQL注入",
                           "cmseasy header.php 报错注入",
                           "PhpMyAdmin2.8.0.3无需登录任意文件包含导致代码执行",
                           "opensns index.php 参数arearank注入",
                           "opensns index.php 前台getshell",
                           "ecshop uc.php参数code SQL注入",
                           "ecshop3.0 flow.php 参数order_id注入",
                           "SiteEngine 6.0 & 7.1 SQL注入漏洞",
                           "明腾cms cookie欺骗漏洞",
                           "正方教务系统services.asmx SQL注入",
                           "正方教务系统数据库任意操纵",
                           "正方教务系统default3.aspx爆破页面",
                           "V2视频会议系统某处SQL注射、XXE漏洞(可getshell)",
                           "1039驾校通未授权访问漏洞",
                           "thinksns category模块代码执行",
                           "TPshop eval-stdin.php 代码执行漏洞"]
        self.hardwarepocdict = ["Dlink 本地文件包含",
                                "Dlink DIAGNOSTIC.PHP命令执行",
                                "锐捷VPN设备未授权访问漏洞",
                                "上海安达通某网关产品&某VPN产品struts命令执行",
                                "SJW74系列安全网关 和 PN-2G安全网关信息泄露",
                                "迈普vpn安全网关弱口令&&执行命令",
                                "迈普网关webui任意文件下载",
                                "浙江宇视（DVR/NCR）监控设备远程命令执行漏洞",
                                "富士施乐打印机默认口令漏洞",
                                "惠普打印机telnet未授权访问",
                                "东芝topaccess打印机未授权漏洞",
                                "佳能打印机未授权漏洞",
                                "juniper NetScreen防火墙后门(CVE-2015-7755)",
                                "海康威视web弱口令"]
        self.industrialpocdict = ["新力热电无线抄表监控系统绕过后台登录",
                                  "火力发电能耗监测弱口令",
                                  "sgc8000 大型旋转机监控系统报警短信模块泄露",
                                  "sgc8000 监控系统数据连接信息泄露",
                                  "sgc8000监控系统超管账号泄露漏洞",
                                  "zte 无线控制器 SQL注入",
                                  "中兴无线控制器弱口令",
                                  "东方电子SCADA通用系统信息泄露"]
        self.informationpocdict = ["options方法开启",
                                   "git源码泄露",
                                   "java配置文件文件发现",
                                   "robots文件发现",
                                   "svn源码泄露",
                                   "JetBrains IDE workspace.xml文件泄露",
                                   "apache server-status信息泄露",
                                   "crossdomain.xml文件发现"]
        self.systempocdict = ["CouchDB 未授权漏洞",
                              "zookeeper 未授权漏洞",
                              "GoAhead LD_PRELOAD远程代码执行(CVE-2017-17562)",
                              "天融信Topsec change_lan.php本地文件包含",
                              "Tomcat代码执行漏洞(CVE-2017-12616)",
                              "Tomcat 弱口令漏洞",
                              "redis 未授权漏洞",
                              "KingGate防火墙默认配置不当可被远控",
                              "nginx Multi-FastCGI Code Execution",
                              "TurboMail设计缺陷以及默认配置漏洞",
                              "TurboGate邮件网关XXE漏洞",
                              "weblogic 弱口令漏洞",
                              "weblogic SSRF漏洞(CVE-2014-4210)",
                              "weblogic XMLdecoder反序列化漏洞(CVE-2017-10271)",
                              "weblogic 接口泄露",
                              "实易DNS管理系统文件包含至远程代码执行",
                              "hudson源代码泄露漏洞",
                              "N点虚拟主机管理系统V1.9.6版数据库下载漏洞",
                              "宏杰Zkeys虚拟主机默认数据库漏洞",
                              "江南科友堡垒机信息泄露",
                              "Moxa OnCell 未授权访问",
                              "glassfish 任意文件读取",
                              "zabbix jsrpc.php SQL注入",
                              "php fastcgi任意文件读取漏洞",
                              "php expose_php模块开启",
                              "hfs rejetto 远程代码执行",
                              "shellshock漏洞",
                              "dorado默认口令漏洞",
                              "ms15_034 http.sys远程代码执行(CVE-2015-1635)",
                              "IIS 6.0 webdav远程代码执行漏洞(CVE-2017-7269)",
                              "深澜软件srun3000计费系统任意文件下载漏洞",
                              "深澜软件srun3000计费系统rad_online.php命令执行bypass",
                              "深澜软件srun3000计费系统rad_online.php参数username命令执行",
                              "深澜软件srun3000计费系统download.php任意文件下载",
                              "深澜软件srun3000计费系统user_info.php命令执行",
                              "intel AMT web系统绕过登录(CVE-2017-5689)",
                              "smtp starttls明文命令注入(CVE-2011-0411)",
                              "resin viewfile 任意文件读取",
                              "mongodb 未授权漏洞",
                              "深信服 AD4.5版本下命令执行漏洞"]
        self.result = []
        self.searchresult = []

    def keyword2num(self):
        self.poclist["cms"] = [x for x in range(
            len(self.cmspocdict)) if self.keyword.lower() in self.cmspocdict[x].lower()]
        self.poclist["system"] = [x for x in range(len(
            self.systempocdict)) if self.keyword.lower() in self.systempocdict[x].lower()]
        self.poclist["industrial"] = [x for x in range(len(
            self.industrialpocdict)) if self.keyword.lower() in self.industrialpocdict[x].lower()]
        self.poclist["information"] = [x for x in range(len(
            self.informationpocdict)) if self.keyword.lower() in self.informationpocdict[x].lower()]
        self.poclist["hardware"] = [x for x in range(len(
            self.hardwarepocdict)) if self.keyword.lower() in self.hardwarepocdict[x].lower()]
        for type in ['cms', 'system', 'industrial', 'information', 'hardware']:
            if self.poclist[type]:
                for i in self.poclist[type]:
                    eval('self.searchresult.append(self.' +
                         type + 'pocdict[' + str(i) + '])')  # 暴力一下
        return self.searchresult

    def show(self, info):
        if info == "cms":
            self.out = "\n".join(self.cmspocdict)
        elif info == "hardware":
            self.out = "\n".join(self.hardwarepocdict)
        elif info == "industrial":
            self.out = "\n".join(self.industrialpocdict)
        elif info == "system":
            self.out = "\n".join(self.systempocdict)
        elif info == "information":
            self.out = "\n".join(self.informationpocdict)
        else:
            pass
        return self.out

    def information(self):
        self.poclist = {'cms': [],
                        'system': [],
                        'industrial': [],
                        'information': range(len(self.informationpocdict)),
                        'hardware': []}

    def cms(self):
        self.poclist = {'cms': range(len(self.informationpocdict)), 'system': [
        ], 'industrial': [], 'information': [], 'hardware': []}

    def system(self):
        self.poclist = {'cms': [],
                        'system': range(len(self.systempocdict)),
                        'industrial': [],
                        'information': [],
                        'hardware': []}

    def industrial(self):
        self.poclist = {'cms': [], 'system': [], 'industrial': range(
            len(self.industrialpocdict)), 'information': [], 'hardware': []}

    def hardware(self):
        self.poclist = {'cms': [],
                        'system': [],
                        'industrial': [],
                        'information': [],
                        'hardware': range(len(self.hardwarepocdict))}

    def exploitpoc(self):
        for poctype in [
            'cms',
            'system',
            'industrial',
            'information',
                'hardware']:
            tasks = [
                grequests.post(
                    "http://tools.hexlt.org/api/" +
                    poctype,
                    json={
                        "url": self.url,
                        "type": type}) for type in self.poclist[poctype]]
            res = grequests.map(tasks, size=30)
            for i in res:
                result = i.json()
                if result['status']:
                    self.result.append(result['pocresult'])
        return self.result  # exp利用成功以列表形式返回结果,否则返回空列表 []


'''
#obj=exploit(url="http://www.dedecms.com")
#obj.information()
#print (obj.exploitpoc())


执行结果：

['[+]存在robots.txt爬虫文件...(敏感信息)\tpayload: http://www.dedecms.com/robots.txt', '[+]存在svn源码泄露漏洞...(高危)\tpayload: http://www.dedecms.com/.svn/entries']

---------------------------------------------------------------------------------------------------------------------

exploit(keyword="dede",url="http://www.dedecms.com").keyword2num()
#return:
{'cms': [71, 72, 73, 74, 75], 'system': [], 'industrial': [], 'information': [], 'hardware': []}

exploit(keyword="php",url="http://www.dedecms.com").keyword2num()
# return:
{'cms': [0, 2, 3, 4, 6, 8, 9, 10, 11, 35, 36, 42, 48, 49, 50, 52, 70, 72, 74, 75, 91, 99, 100, 101, 116, 118, 134, 188, 189, 220, 221, 222, 223, 226, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 239, 240, 241, 242, 243, 244, 253], 'system': [3, 20, 21, 22, 29, 30, 31, 32], 'industrial': [], 'information': [], 'hardware': [1]}

---------------------------------------------------------------------------------------------------------------------

example:
obj=exploit(keyword="dede",url="http://www.dedecms.com")
obj.keyword2num()
obj.exploitpoc()
来进行搜索+利用 功能类似：http://tools.hexlt.org/search


还可以
obj=exploit(url="http://www.dedecms.com")
obj.information() // obj.cms() //obj.system 等等
obj.exploitpoc()
来对一个范围利用 功能类似 http://tools.hexlt.org/cms // http://tools.hexlt.org/hardware 等等
'''