import json
import time
import requests
import random

#cookie
Cookie = input('cookie：')

def score():
    url_ger_score = "https://mobile.campushoy.com/v6/user/myStatistics"
    headers_get_score = {
        "Content-Type": "application/json",
        "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
    }
    re_score = requests.post(url_ger_score,headers=headers_get_score)
    time.sleep(2)
    re_score_text = json.loads(re_score.text).get("data").get("score")
    return re_score_text

a1 = score()
print("开始获取当前今币数量：",a1)

#刷新主页并获取文章id
url_zynr ="https://mobile.campushoy.com/v9/content/fresh/listFirstPageRec?timeValue=1649346094000&action=UP&pageNumber=7&exposure=NO&freshType=ARTICLE%2CSMALL_VIDEO%2CQUESTION%2CSUBJECT%2CGRAPHIC"
headers_zynr = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_zynr = requests.get(url_zynr,headers=headers_zynr)
qq_zynr_list = json.loads(qq_zynr.text).get("data").get("rows")
id1 = qq_zynr_list[0].get("freshId")
print("获取到第一篇文章的id为：",id1)
id2 = qq_zynr_list[1].get("freshId")
print("获取到第二篇文章的id为：",id2)
id3 = qq_zynr_list[2].get("freshId")
print("获取到第三篇文章的id为：",id3)
id4 = qq_zynr_list[3].get("freshId")
print("获取到第四篇文章的id为：",id4)
id5 = qq_zynr_list[4].get("freshId")
print("获取到第五篇文章的id为：",id5)
id6 = qq_zynr_list[5].get("freshId")
print("获取到第六篇文章的id为：",id6)

time.sleep(3)
#点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id1,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第一次点赞",dianzan_back)

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次点赞")

#第二次点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id2,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第二次点赞",dianzan_back)

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次点赞")

#第三次点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id3,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第三次点赞",dianzan_back)

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次点赞")

#第四次点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id4,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第四次点赞",dianzan_back)

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次点赞")

#第五次点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id5,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第五次点赞",dianzan_back)

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次点赞")

#第六次点赞
url_dianzan = "https://mobile.campushoy.com/v3/thumbsUp"
data_dianzan = json.dumps({"id": id6,"toggle": "DO"})
headers_dianzan = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_dianzan = requests.post(url_dianzan,headers=headers_dianzan,data=data_dianzan)
time.sleep(1)
dianzan_back = json.loads(qq_dianzan.text).get("errMsg")
print("进行第六次点赞",dianzan_back)

#分享，无需特定文章
print("开始第一次分享任务")
url_share = "https://mobile.campushoy.com/v3/user/score/operation"
data_share = json.dumps({"opType": "SHARE"})
headers_share = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_share =requests.post(url_share,headers=headers_share,data=data_share)
score_share = json.loads(qq_share.text).get("data").get("score")
if score_share == 2:
    print("第一次分享完成")
elif score_share == 0:
    print("今日分享任务已完成")


#静默三秒
time.sleep(3)
print("静默三秒，进行下一次分享")

print("开始第二次分享任务")
url_share = "https://mobile.campushoy.com/v3/user/score/operation"
data_share = json.dumps({"opType": "SHARE"})
headers_share = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_share =requests.post(url_share,headers=headers_share,data=data_share)
score_share = json.loads(qq_share.text).get("data").get("score")
if score_share == 2:
    print("第二次分享完成")
elif score_share == 0:
    print("今日分享任务已完成")


#静默三秒
time.sleep(3)
print("静默三秒，进行下一次分享")

print("开始第三次分享任务")
url_share = "https://mobile.campushoy.com/v3/user/score/operation"
data_share = json.dumps({"opType": "SHARE"})
headers_share = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_share =requests.post(url_share,headers=headers_share,data=data_share)
score_share = json.loads(qq_share.text).get("data").get("score")
if score_share == 2:
    print("第三次分享完成")
elif score_share == 0:
    print("今日分享任务已完成")


#文章下评论
#生成随机数
number1 = str(random.randint(10, 200000000))
number2 = str(random.randint(10, 200000000))
number3 = str(random.randint(10, 200000000))
message = "我来占个楼"
message1 = message + number1
message2 = message + number2
message3 = message + number3
#文章下评论
url_comment = "https://mobile.campushoy.com/v3/fresh/comment"
data_comment = json.dumps({
    "freshId": id1,
    "content": message1,
    "imgUrls": ""
})
headers_comment = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_comment = requests.post(url_comment,headers=headers_comment,data=data_comment)
qq_comment_errMsg = json.loads(qq_comment.text).get("errMsg")
if qq_comment_errMsg == "success":
    print("第一次评论成功")
else:print("第一次评论失败")

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次评论")

#第二次评论
url_comment = "https://mobile.campushoy.com/v3/fresh/comment"
data_comment = json.dumps({
    "freshId": id2,
    "content": message2,
    "imgUrls": ""
})
headers_comment = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_comment = requests.post(url_comment,headers=headers_comment,data=data_comment)
qq_comment_errMsg = json.loads(qq_comment.text).get("errMsg")
if qq_comment_errMsg == "success":
    print("第二次评论成功")
else:print("第二次评论失败")

#静默三秒
time.sleep(3)
print("静默三秒，进行下一次评论")

#第三次评论
url_comment = "https://mobile.campushoy.com/v3/fresh/comment"
data_comment = json.dumps({
    "freshId": id3,
    "content": message3,
    "imgUrls": ""
})
headers_comment = {
    "Content-Type": "application/json",
    "Cookie": Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_comment = requests.post(url_comment,headers=headers_comment,data=data_comment)
qq_comment_errMsg = json.loads(qq_comment.text).get("errMsg")
if qq_comment_errMsg == "success":
    print("第三次评论成功")
else:print("第三次评论失败")

#动态
url_dongtai = "https://mobile.campushoy.com/v8/content/fresh/publish"
data_dongtai = json.dumps({
    "imgUrls": "",
    "content": message1,
    "taskId": "0ebaccb92fa1bea8eddc4360e2b16335",
    "rewardCoin": 0
})
headers_dongtai = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
print('发布成功，开始获取文章id')
qq_dongtai = requests.post(url_dongtai,data=data_dongtai,headers=headers_dongtai)
id_message = json.loads(qq_dongtai.text).get("data").get("id")
score_message = json.loads(qq_dongtai.text).get("data").get("score")
print("获取到的文章id为：",id_message,"获得积分：",score_message)

print("发布成功，5秒后删除")
time.sleep(5)

#删除发布的文章
url_dongtai_del = "https://mobile.campushoy.com/v3/fresh/delete"
headers_dongtai_del = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
data_dongtai_del = json.dumps({
    "freshId": id_message
})
qq_dongtai_del = requests.post(url_dongtai_del,data=data_dongtai_del,headers=headers_dongtai_del)
message_del = json.loads(qq_dongtai_del.text).get("errMsg")
print("尝试删除文章",message_del)
print("静默三秒进行下一次动态的发布")
time.sleep(3)

url_dongtai = "https://mobile.campushoy.com/v8/content/fresh/publish"
data_dongtai = json.dumps({
    "imgUrls": "",
    "content": message2,
    "taskId": "0ebaccb92fa1bea8eddc4360e2b16335",
    "rewardCoin": 0
})
headers_dongtai = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
print('发布成功，开始获取文章id')
qq_dongtai = requests.post(url_dongtai,data=data_dongtai,headers=headers_dongtai)
id_message = json.loads(qq_dongtai.text).get("data").get("id")
score_message = json.loads(qq_dongtai.text).get("data").get("score")
print("获取到的文章id为：",id_message,"获得积分：",score_message)

print("发布成功，5秒后删除")
time.sleep(5)

#删除发布的文章
url_dongtai_del = "https://mobile.campushoy.com/v3/fresh/delete"
headers_dongtai_del = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
data_dongtai_del = json.dumps({
    "freshId": id_message
})
qq_dongtai_del = requests.post(url_dongtai_del,data=data_dongtai_del,headers=headers_dongtai_del)
message_del = json.loads(qq_dongtai_del.text).get("errMsg")
print("尝试删除文章",message_del)
print("静默三秒进行下一次动态的发布")
time.sleep(3)

url_dongtai = "https://mobile.campushoy.com/v8/content/fresh/publish"
data_dongtai = json.dumps({
    "imgUrls": "",
    "content": message1,
    "taskId": "0ebaccb92fa1bea8eddc4360e2b16335",
    "rewardCoin": 0
})
headers_dongtai = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
print('发布成功，开始获取文章id')
qq_dongtai = requests.post(url_dongtai,data=data_dongtai,headers=headers_dongtai)
id_message = json.loads(qq_dongtai.text).get("data").get("id")
score_message = json.loads(qq_dongtai.text).get("data").get("score")
print("获取到的文章id为：",id_message,"获得积分：",score_message)

print("发布成功，5秒后删除")
time.sleep(5)

#删除发布的文章
url_dongtai_del = "https://mobile.campushoy.com/v3/fresh/delete"
headers_dongtai_del = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
data_dongtai_del = json.dumps({
    "freshId": id_message
})
qq_dongtai_del = requests.post(url_dongtai_del,data=data_dongtai_del,headers=headers_dongtai_del)
message_del = json.loads(qq_dongtai_del.text).get("errMsg")
print("尝试删除文章",message_del)

#签到
print("开始进行每日签到任务")
url_sign = "https://mobile.campushoy.com/v3/active/punch"
headers_sign = {
    "Content-Type": "application/json",
    "Cookie" : Cookie,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15.5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 cpdaily/9.0.20 wisedu/9.0.20"
}
qq_sign = requests.post(url_sign,headers=headers_sign)
sign_or = json.loads(qq_sign.text).get("errCode")
if sign_or == 0:
    print("签到成功，已连续签到天数:",json.loads(qq_sign.text).get("data").get("continuousTime"),"签到时间为：",json.loads(qq_sign.text).get("data").get("punchTime"))
elif sign_or == -1:
    print("今日已签到")

a2 = score()
print("所有任务已完成")
print("开始获取当前今币数量：",a2,"本次运行获得了",a2-a1,"个今币")

print("三十秒后结束任务窗口，谢谢使用")
time.sleep(30)