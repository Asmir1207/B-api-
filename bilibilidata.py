# coding=utf-8
###注：我们的存放数据的文件是已经有人爬取过了的很多aid文件（它某个时间的播放量，评论数，收藏量），
#                我们再去爬取这些aid文件其它的信息，比如它的上传时间等等其它信息，丰富它的数据。
import os
import re
import requests
import csv

header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def getaid():  #获取文件aid620.mat中数字620
    all_id = []
    path = "E:/xzfcwl/bilibili_csv_447500/csv_1_10000/part3"
    dirs = os.listdir(path)
    dirs.sort()
    # 输出所有文件的数字字符
    for file in dirs:

      re1 = '.*?'
      re2 = '(\\d+)'
      rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)
      m = rg.search(file)
      if m:
         int1 = m.group(1)
         all_id.append(int1)
    return all_id
def list_str(list):
    str = " ".join(list)
    return str
def parse(text,id2): #匹配文本数据
        # "code":-404,
        aid = re.findall('"stat".*?"aid":(\d+),', text, re.S)
        if aid == []:
            list2 = [id2]
            with open('null1.csv', 'a+', newline="", encoding='UTF-8')as f:
             csv_write = csv.writer(f)
             csv_write.writerow(list2)
        else:

            # 匹配data所有数据
            aid = re.findall('"stat".*?"aid":(\d+),', text, re.S)            # aid视频id
            videos = re.findall('"videos":(\d+),', text, re.S)              # videos视频数
            tid = re.findall('"tid":(\d+),', text, re.S)                    # tid 分类号？
            tname = re.findall('"tname":"(.*?)",', text, re.S)              # tname 分类名
            copyright = re.findall('"copyright":(\d+),', text, re.S)        # copyright ？？？
            title = re.findall('"title":"(.*?)","pubdate"', text, re.S)              # title 标题
            pubdate = re.findall('"pubdate":(\d+),', text, re.S)            # pubdata上传时间
            ctime = re.findall('"ctime":(\d+),', text, re.S)                # ctime 估计是第一条弹幕时间
            desc = re.findall('"desc":"(.*?)","state"', text, re.S)                # desc描述
            state = re.findall('"state":(\d+),', text, re.S)                # state 啥玩意儿？
            attribute = re.findall('"attribute":(\d+),', text, re.S)        # attribute 属性
            duration = re.findall('"duration":(\d+),', text, re.S)          # duration ？？？
            # 匹配rights所有数据                                             不知道啥玩意儿*11
            bp = re.findall('"bp":(\d+),', text, re.S)
            elec = re.findall('"elec":(\d+),', text, re.S)
            download = re.findall('"download":(\d+),', text, re.S)
            movie = re.findall('"movie":(\d+),', text, re.S)
            pay = re.findall('"pay":(\d+),', text, re.S)
            hd5 = re.findall('"hd5":(\d+),', text, re.S)
            no_reprint = re.findall('"no_reprint":(\d+),', text, re.S)
            autoplay = re.findall('"autoplay":(\d+),', text, re.S)
            ugc_pay = re.findall('"ugc_pay":(\d+),', text, re.S)
            is_cooperation = re.findall('"is_cooperation":(\d+),', text, re.S)
            ugc_pay_preview = re.findall('"ugc_pay_preview":(\d+)}', text, re.S)

            # 匹配owner所有数据
            mid = re.findall('"mid":(\d+),', text, re.S)  # up主id
            name = re.findall('"name":"(.*?)",', text, re.S)  # up主名字

            # 匹配stat所有数据
            view = re.findall('"view":(\d+),', text, re.S)                # view观看数
            danmaku = re.findall('"danmaku":(\d+),', text, re.S)          # danmaku弹幕数
            reply = re.findall('"reply":(\d+),', text, re.S)              # reply评论
            favorite = re.findall('"favorite":(\d+),', text, re.S)        # favorite收藏
            coin = re.findall('"coin":(\d+),', text, re.S)                # coin硬币
            share = re.findall('"share":(\d+),', text, re.S)              # share分享
            now_rank = re.findall('"now_rank":(\d+),', text, re.S)        # now_rank？？？
            his_rank = re.findall('"his_rank":(\d+),', text, re.S)        # his_rank？？？
            like = re.findall('"like":(\d+),', text, re.S)                # like点赞数
            dislike = re.findall('"dislike":(\d+)}', text, re.S)          # dislike不喜欢
            dynamic = re.findall('"dynamic":"(.*?)",', text, re.S)        # part？？？
            cid = re.findall('"pages".*?"cid":(\d+),', text, re.S)                  # cid弹幕编码
            width = re.findall('"pages".*?"width":(\d+),', text, re.S)              # width长
            height = re.findall('"pages".*?"height":(\d+),', text, re.S)            # height高
            rotate = re.findall('"pages".*?"rotate":(\d+)}', text, re.S)            # rotate？？？
            no_cache = re.findall('"no_cache":(.*?),', text, re.S)        # no_cache？？？
            page = re.findall('"page":(\d+),', text, re.S)                # page 页数
            From = re.findall('"from":"(.*?)",', text, re.S)              # From首字大写区分关键字 来自
            part = re.findall('"part":"(.*?)",', text, re.S)              # part？？？
            duration = re.findall('"pages".*?"duration":(\d+),', text, re.S)        # duration ???

            #aid,videos,tid,tname,copyright,title,pubdate,ctime,desc,state,attribute,duration,bp,elec,download,movie,pay,hd5,no_reprint,autoplay,ugc_pay,is_cooperation,ugc_pay_preview,mid,name,view,danmaku,reply,favorite,coin,share,now_rank,his_rank,like,dislike,dynamic,cid,width,height,rotate,no_cache,page,From,part
            aid_str = list_str(aid)
            videos_str = list_str(videos)
            tid_str = list_str(tid)
            tname_str = list_str(tname)
            copyright_str =list_str(copyright)
            title_str = list_str(title)
            pubdate_str = list_str(pubdate)
            ctime_str = list_str(ctime)
            desc_str = list_str(desc)
            state_str = list_str(state)
            attribute_str = list_str(attribute)
            duration_str = list_str(duration)

            bp_str = list_str(bp)
            elec_str = list_str(elec)
            download_str = list_str(download)
            movie_str = list_str(movie)
            pay_str = list_str(pay)
            hd5_str = list_str(hd5)
            no_reprint_str = list_str(no_reprint)
            autoplay_str =list_str(autoplay)
            ugc_pay_str =list_str(ugc_pay)
            is_cooperation_str = list_str(is_cooperation)
            ugc_pay_preview_str = list_str(ugc_pay_preview)


            mid_str = list_str(mid)
            name_str = list_str(name)


            view_str = list_str(view)
            danmaku_str = list_str(danmaku)
            reply_str = list_str(reply)
            favorite_str = list_str(favorite)
            coin_str = list_str(coin)
            share_str = list_str(share)
            now_rank_str = list_str(now_rank)
            his_rank_str = list_str(his_rank)
            like_str = list_str(like)
            dislike_str = list_str(dislike)
            dynamic_str = list_str(dynamic)
            cid_str = list_str(cid)
            width_str = list_str(width)
            height_str = list_str(height)
            rotate_str = list_str(rotate)
            no_cache_str = list_str(no_cache)

            page_str = list_str(page)
            From_str = list_str(From)
            part_str = list_str(part)

            list = [aid_str,videos_str,tid_str,tname_str,copyright_str,title_str,pubdate_str,ctime_str,desc_str,state_str,attribute_str,duration_str,bp_str,elec_str,download_str,movie_str,pay_str,hd5_str,no_reprint_str,autoplay_str,ugc_pay_str,is_cooperation_str,ugc_pay_preview_str,mid_str,name_str,view_str,danmaku_str,reply_str,favorite_str,coin_str,share_str,now_rank_str,his_rank_str,like_str,dislike_str,dynamic_str,cid_str,width_str,height_str,rotate_str,no_cache_str,page_str,From_str,part_str]
            with open('new1.csv', 'a+', newline="",encoding='UTF-8-sig')as f:
                csv_write = csv.writer(f)
                csv_write.writerow(list)

def geturl(url,id):

   try:
      ip = '91.233.228.102:80' #代理id可以做个代理池存放
      proxies = {'http': ip}
      response = requests.get(url,proxies=proxies)
      if response.status_code == 200:
          # savehtml = 'aid' + id + '.html'
          # with open(savehtml, 'wb')as f:
          #     f.write(response.content)

        return response.text
   except requests.RequestException:
      return None

def main():
    (all_id) = getaid()
    for id in all_id:
        url='https://api.bilibili.com/x/web-interface/view?aid='+str(id)
        html = geturl(url,id)
        parse(html,id)

if __name__ == '__main__':
            main()