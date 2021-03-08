import urllib.request
import urllib.parse
import re
import socket
import subprocess
import os
import sys
from ping3 import ping

# 用户提示
# 程序里面变量比较多，一定要仔细看
z = 1# 死循环，不然程序运行一遍就会退出


host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

def fjx(n):
    if n == 1:
        print('===========================我是分界线===============================')
        print("")
    elif n == 2:
        print('++++++++++===============================================++++++++++')
        print("")
    elif n == 3:

            print("")
    elif n == 4:
        print("-------------------------------------------------------------------")
        print("")

print('使用时请保持联网！！！')

print('输入‘quit’或‘exit’以退出，输入‘help’以获取帮助')
fjx(3)

def ping_host(ip):# 这个可加可不加，反正对查词没有什么帮助。
    """
    获取节点的延迟的作用
    :param node:
    :return:
    """
    ip_address = ip
    response = ping(ip_address)

    if response is not None:
        delay = ("延迟:"+str(int(response * 1000)))
        print('    '+delay)



print('请输入你要查询的词语或字：')

#正式开始
while z == 1:
    wlsy1=wlsy=wlsy2=''
    ciyu = input(">>")
    long = len(ciyu)
    fjx(4)
    if ciyu == 'quit' or 'exit':
        break

    if ciyu == 'help':
        print('帮助：')
        print('  网络环境：')
        print("    Host name: %s" % host_name)
        print("    IP address: %s" % ip_address)
        print('    '+str(ping_host('www.zdic.net')))
        print('***如果第三项为‘false’，表示你可能没有连接互联网。请检查网络后重试。***')
        print("")
        print("  使用说明：")
        print("    使用时应当输入正经词汇，若查询网络用语或人名可能会查找不到。")
        print("    若’释义‘栏或’网络释义‘一栏中没有内容，则代表未查找到相关资料。")
        print("    程序中可能有Bug，可以反映在Github上的评论区里。")
        print('    若想使用最新版本软件，请前往网址：https://github.com/Cheng07-python/cha-ci.git' + '，并且点击“Code“按钮下载ZIP压缩包。')
        fjx(1)
    #字
    if long == 1:

        ci = ciyu
        if ciyu == 'quit' or 'exit':
            break
        else:
            data = {}
            ciyu = urllib.parse.quote(ciyu)
            dizhi = 'https://www.zdic.net/hans/' + ciyu
            url = dizhi

            data = urllib.parse.urlencode(data).encode('utf-8')
            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')

            zifu = '<p><span class="z_ts2">拼音</span> <span class="z_d song">'
            where = html.find(zifu)
            d = html.find('<div class="enbox"><p><span class="z_ts2">')
            a = where + 56
            html1 = html[a:d]

            zyzfc = '<span class="ptr"><a class="audio_p'
            zyjs = html1.find(zyzfc)
            zy = html1[:zyjs]
            syks = html1.find("<p><strong>基本字义</strong></p>")
            syzfc = '"</span>）</strong></p><p><span class="dicpy">"'
            # 找到相应数据
            sy = html1.find('<span class="ptr"><a class="audio_play_button i_volume-up ptr" data-src-mp3="//img.zdic.net/audio/zd/py/')
            syI = html1[sy + 102:]
            sy1 = syI.find("</span></p><ol> <li>")
            syII = syI[sy1 + 20:]

            syjs = syII.find('其它字义')
            syII = syII[:syjs]
            syjs = syII.find('其它字义')
            bihua = html.find('<p><span class="z_ts3">总笔画</span> ')
            bihuashu = html[bihua + 34:bihua + 37]
            # 查找替换
            syII = syII.replace('（<span class="dicpy">','')
            syII = syII.replace('</span>）','')
            syII = syII.replace('</span>', '')
            syII = syII.replace('<li>', '')
            syII = syII.replace('</li>', '')
            syII = syII.replace('</li> <li>', ' ')
            syII = syII.replace('<', '')
            syII = syII.replace('>', '')
            syII = syII.replace('/', '')
            syII = syII.replace('"', '')
            syII = syII.replace('=', '')
            zm=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            sz=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            for j in range(10):
                syII = syII.replace(sz[j], '')
            for i in range(26):
                syII = syII.replace(zm[i], '')

            sy0 = syII[:syjs]
            if where == -1:
                print('未找到 ' + ci + ' 请重新输入。')
                fjx(3)
            else:

                print('字音：', zy)
                print('笔画数：', bihuashu.replace("<", " "))
                print('释义：', sy0)
                fjx(2)

    # 词语

    elif 2 <= long < 4:
        ci = ciyu
        if ciyu != 'quit':
            data = {}
            ci = ciyu
            ciyu = urllib.parse.quote(ciyu)
            dizhi = 'https://www.zdic.net/hans/' + ciyu
            url = dizhi

            # 利用urlencode把它编码成url的形式
            data = urllib.parse.urlencode(data).encode('utf-8')
            response = urllib.request.urlopen(url, data)
            html = response.read().decode('utf-8')
            pinyin = '<p><span class="z_ts2">拼音</span> <span class="dicpy">'
            zifu = '<span class="z_ts2">解释</span><div class="jnr"><p>◎ <strong>' + ci + '</strong> <span class="dicpy">'
            where = html.find(zifu)
            py = html.find(pinyin)
            d = html.find('<div class="div copyright"> © 汉典 </div>')
            a = where + 89 + long

            e = html.find('</span> <span class="z_d song"><span class="ptr"><a class="audio_play_button i_volume-up ptr cd_au" title="' + ci + '">')

            e = html.find('</span>  <span class="z_d song"><span class="ptr"><a class="audio_play_button i_volume-up ptr cd_au" title="' + ci + '">')

            wlsy = html.find('<h3>百度百科</h3><div class="bknr"><h3>'+ci)
            wlsy2 = html.find('</li></div>                    <div class="div copyright"> © 汉典 </div>')

            wlsy1 = html[wlsy + 45 + long:wlsy2]

            if where == -1:
                print('未找到 ' + ci + ' 请重新输入。')
                fjx(3)
            else:   # 筛选
                html1 = html[py + 53:e]
                html2 = html[a:d]

                html2 = html2.replace('i</span></p><p><span class="cino">', '')
                html2 = html2.replace('</span> <span class="encs">', '')
                html22 = html2.find(';</span></p><p><span class="encs">')
                html2 = html2[html22 + 34:]
                html2 = html2.replace("</span>", ' ')
                '''
                zaoju = html2.find('</p><p><span class="diczx1">')
                zjjs = html2.find('</span></p><p><span class="diczx1">')
    '''
                ss = ['（<span class="dicpy">','</span>）','</span>','<li>','</li>','</li> <li>','<','>','/','"','=','&','%','_','-','.',';','∶','.','(',')','[',']','      ','国语辞典',',','拼音为']

                for g in range(len(ss)):
                    wlsy1 = wlsy1.replace(ss[g],'')
                    html2 = html2.replace(ss[g],'')
                #作者最终还是没有逃过真香定律。。。


                zm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                sz = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                piny = ['ā','á','ǎ','à','ō','ó','ǒ','ò','ē','ē','é','ě','è','ī','í','ǐ','ì','ū','ú','ǔ','ù','ǖ','ǘ','ǚ','ǜ']
                for j in range(10):
                    wlsy1 = wlsy1.replace(sz[j], '')
                    html2 = html2.replace(sz[j],'')
                for i in range(52):
                    wlsy1 = wlsy1.replace(zm[i], '')
                    html2 = html2.replace(zm[i],'')
                for h in range(24):
                    wlsy1 = wlsy1.replace(piny[h],'')
                    html2 = html2.replace(piny[h], '')
                end = html2.find('<div class="div copyright"> © 汉典 </div>')
                zkh1 = html2.find('[')
                zkh2 = html2.find(']')
                html2 = html2[zkh2 + 1:end]
                zjks = html2.find('</p><p><span class="')

                html2 = html2.replace('英语','')
                # print(zaoju,zjjs)
                html2 = html2[:zjks]
                wlsy1 = wlsy1.replace("，读音为",'')
                if wlsy1 == -1:
                    wlsy1 = '无'
                # fanyi = html2[zkh1+1:zkh2]
                # html23 = html[html22+1:]
                print('拼音：   ' + html1)
                print('释义：' + html2)
                print("网络释义：" + wlsy1)
                fjx(2)
                # print('翻译：'+fanyi)
                #print(html)
            # 成语
    elif long == 4:
        data = {}
        ci = ciyu
        ciyu = urllib.parse.quote(ciyu)
        dizhi = 'https://www.zdic.net/hans/' + ciyu#爬虫
        url = dizhi
        #筛选
        data = urllib.parse.urlencode(data).encode('utf-8')
        response = urllib.request.urlopen(url, data)
        html = response.read().decode('utf-8')
        wlsy = html.find('<h3>百度百科</h3><div class="bknr"><h3>'+ci)
        wlsyI=str(html[wlsy+35:])
        wlsy2 = wlsyI.find(' © 汉典')
        wlsyII = wlsyI[:wlsy2-45]
        wlsyII = wlsyII.replace('</h3>','')
        wlsyII = wlsyII.replace('<li>','')
        wlsyII = wlsyII.replace('</li>','')
        zhuyin1 = html.find('<p><span class="z_ts2">拼音</span> <span class="dicpy">')
        zhuyin2 = html.find('</span>  <span class="z_d song"><span class="ptr"><a class="audio_play_button i_volume-up ptr cd_au" title="')
        zhuyinI = html[zhuyin1+53:zhuyin2]
        zifu ='</h3><p>【解释】'

        d = html.find('                  <div class="div copyright"> © 汉典 </div>')
        html4 = html[d+55:]
        d = html4.find('                  <div class="div copyright"> © 汉典 </div>')
        where = html4.find(zifu)
        sx = ['</p>', '<p>']
        for i in range(len(sx)):
            html4 = html4.replace(sx[i], ' ')

        a = where + 6
        if wlsy1 == -1:
            wlsy1 = '无'
        if where == -1:
            print('未找到 ' + ci + ' 请重新输入。')
            fjx(3)
        else:

            html4 = html4[a:d]
            print('注音：', zhuyinI)
            print(html4)
            wlsyII = wlsyII.replace('</div>','')
            wlsyII = wlsyII.replace('</p>', '')
            wlsyII = wlsyII.replace('，读音为','')
            print('网络释义：' + wlsyII)
            #print(a,d) <=用于调试
            #print(html)
            fjx(2)
    continue#我也不知道这个continue有啥用反正运行不会出错
    #程序又短了几行呢。。。