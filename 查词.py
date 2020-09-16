import urllib.request
import urllib.parse
import re
import socket
import subprocess
import os
import sys
from ping3 import ping

#用户提示

z = 1
print('使用时请保持联网！！！')
print('若想使用最新版本软件，请前往网址：https://github.com/Cheng07-python/cha-ci.git'+'，并且点击“Code“按钮下载ZIP压缩包。')


host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: %s" % host_name)
print("IP address: %s" % ip_address)




def ping_host(ip):
    """
    获取节点的延迟的作用
    :param node:
    :return:
    """
    ip_address = ip
    response = ping(ip_address)
    print(response)
    if response is not None:
        delay = int(response * 1000)
        print("延迟:",delay)



print(ping_host('www.zdic.net'))

print('***如果第三项为‘false’，表示你可能没有连接互联网。请检查网络后重试。***')
print("")

#正式开始
while z == 1:
    wlsy1=wlsy=wlsy2=''
    ciyu = input("请输入你要查询的词语或字（输入'quit'即可退出）：")
    long = len(ciyu)
    if ciyu == 'quit':
        break

    #字
    if long == 1:

        ci = ciyu
        if ciyu == 'quit':
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
            sy = html1.find(
                '<span class="ptr"><a class="audio_play_button i_volume-up ptr" data-src-mp3="//img.zdic.net/audio/zd/py/')
            syI = html1[sy + 104:]
            sy1 = syI.find("</span></p><ol> <li>")
            syII = syI[sy1 + 20:]
            syjs = syII.find('其它字义')
            syII = syII[:syjs]
            syjs = syII.find('其它字义')
            bihua = html.find('<p><span class="z_ts3">总笔画</span> ')
            bihuashu = html[bihua + 34:bihua + 36]
            syII = syII.replace('（<span class="dicpy">','')
            syII = syII.replace('</span>）','')
            syII = syII.replace('</span>', '')
            syII = syII.replace('<li>', '')
            syII = syII.replace('</li>', '')
            syII = syII.replace('</li> <li>',' ')
            syII = syII.replace('<','')
            syII = syII.replace('>','')
            syII = syII.replace('/', '')
            syII = syII.replace('"','')
            syII = syII.replace('=','')
            zm=['a','b','c','d','e','f','g','h','i','j','k','m','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
            sz=['1','2','3','4','5','6','7','8','9','0']
            for j in range(10):
                syII = syII.replace(sz[j],'')
            for i in range(26):
                syII = syII.replace(zm[i], '')

            sy0 = syII[:syjs]
            if where == -1:
                print('未找到 ' + ci + ' 请重新输入。')
            else:

                print('字音：', zy)
                print('笔画数：', bihuashu.replace("<", " "))
                print('释义：',sy0)

    # 词语

    if 2 <= long < 4:
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
            e = html.find(
                '</span> <span class="z_d song"><span class="ptr"><a class="audio_play_button i_volume-up ptr cd_au" title="' + ci + '">')
            wlsy = html.find('<h3>百度百科</h3><div class="bknr"><h3>')
            wlsy2 = html.find('</li></div> <div class="div copyright"> © 汉典 </div>')

            wlsy1 = html[wlsy + 45 + long:wlsy2]

            if where == -1:
                print('未找到 ' + ci + ' 请重新输入。')
            else:#筛选
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
                wlsy1 = wlsy1.replace('（<span class="dicpy">', '')
                wlsy1 = wlsy1.replace('</span>）', '')
                wlsy1 = wlsy1.replace('</span>', '')
                wlsy1 = wlsy1.replace('<li>', '')
                wlsy1 = wlsy1.replace('</li>', '')
                wlsy1 = wlsy1.replace('</li> <li>', ' ')
                wlsy1 = wlsy1.replace('<', '')
                wlsy1 = wlsy1.replace('>', '')
                wlsy1 = wlsy1.replace('/', '')
                wlsy1 = wlsy1.replace('"', '')
                wlsy1 = wlsy1.replace('=', '')
                zm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
                sz = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                for j in range(10):
                    wlsy1 = wlsy1.replace(sz[j], '')
                for i in range(26):
                    wlsy1 = wlsy1.replace(zm[i], '')

                end = html2.find('</p></div><div class="h_line1">-----------------</div>')
                zkh1 = html2.find('[')
                zkh2 = html2.find(']')
                html2 = html2[zkh2 + 1:end]
                zjks = html2.find('</p><p><span class="')
                # print(zaoju,zjjs)
                html2 = html2[:zjks]
                if wlsy1 == -1:
                    wlsy1 = '无'
                # fanyi = html2[zkh1+1:zkh2]
                # html23 = html[html22+1:]
                print('拼音：   ' + html1)
                print('释义：  ' + html2)
                print("网络释义：" + wlsy1)
                print('++++++++++===========================================++++++++++')
                # print('翻译：'+fanyi)
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
        wlsy = html.find('<h3>百度百科</h3><div class="bknr"><h3>')
        wlsyI=str(html[wlsy+35:])
        wlsy2 = wlsyI.find('</li></div> <div class="div copyright"> © 汉典')
        wlsyII = wlsyI[:wlsy2]
        wlsyII = wlsyII.replace('</h3>','')
        wlsyII = wlsyII.replace('<li>','')
        wlsyII = wlsyII.replace('</li>','')

        zifu = '<h3>' + ci + '</h3><p>【解释】'
        where = html.find(zifu)
        d = html.find('</p><p>【')
        a = where + 12 + long
        if wlsy1 == -1:
            wlsy1 = '无'
        if where == -1:
            print('未找到 ' + ci + ' 请重新输入。')
        else:

            html1 = html[a:d]
            print(html1)
            print('网络释义：' + wlsyII)
            print('++++++++++===========================================++++++++++')
    continue