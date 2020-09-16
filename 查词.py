import urllib.request
import urllib.parse
import re
import socket
import subprocess
import os
import sys
from ping3 import ping



z = 1
print('使用时请保持联网！！！')

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
        # 下面两行新增的


print(ping_host('www.zdic.net'))

print('***如果第三项为‘false’，表示你可能没有连接互联网。请检查网络后重试。***')
print("")


while z == 1:
    ciyu = input("请输入你要查询的词语（输入'quit'即可退出）：")
    long = len(ciyu)
    if ciyu == 'quit':
        break

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
            else:
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
        dizhi = 'https://www.zdic.net/hans/' + ciyu
        url = dizhi

        data = urllib.parse.urlencode(data).encode('utf-8')
        response = urllib.request.urlopen(url, data)
        html = response.read().decode('utf-8')
        wlsy = html.find('<h3>百度百科</h3><div class="bknr"><h3>')
        wlsy2 = html.find('</li></div>                    <div class="div copyright"> © 汉典 </div>')
        wlsy1 = html[wlsy + 45 + long:wlsy2]
        wlsy1 = wlsy.replacee('</li>',' ')
        wlsy1 = wlsy.replacee('<li>',' ')
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
            print('网络释义：' + wlsy1)
            print('++++++++++===========================================++++++++++')
    continue