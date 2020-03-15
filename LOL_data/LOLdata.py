import requests,json  #导入解析网页和json数据的模块
import openpyxl #导入Excel模块

#设置Excel
wb = openpyxl.Workbook() #创建工作簿
ws = wb.active #创建工作表
ws.title = 'LOL数据' #表名为LOL数据
ws.append(['胜负','击杀','死亡','助攻','买眼数','放置守卫数','击杀守卫数','挣金币数','击杀小兵数','摧毁水晶数'])

#获取gameId
url1 = 'https://lol.sw.game.qq.com/lol/api/?c=Battle&a=matchList&areaId=30&accountId=4007807286&queueId=70,72,73,75,76,78,96,98,100,300,310,313,317,318,325,400,420,430,450,460,600,610,940,950,960,980,990,420,440,470,83,800,810,820,830,840,850&r1=matchList'#网址
headers = {'Cookie': 'pgv_pvi=8636771328; pgv_pvid=454362090; eas_sid=A175H8A2o7T9Q7o9R2K306C805; RK=HWawDcwC+8; ptcz=241fe16d79e98480d78418fdd47931a86cc2fc0d28830ad3934fd566664b5547; ied_qq=o2294776060; uin_cookie=o2294776060; LOLWebSet_AreaBindInfo_2294776060=%257B%2522areaid%2522%253A%252230%2522%252C%2522areaname%2522%253A%2522%25E7%2594%25B7%25E7%2588%25B5%25E9%25A2%2586%25E5%259F%259F%2520%25E5%2585%25A8%25E7%25BD%2591%25E7%25BB%259C%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25222294776060%2522%252C%2522rolename%2522%253A%2522%25E6%2588%2591%25E4%25B8%25BA%25E5%25B0%258F%25E5%25A5%2588%25E4%25B8%258A%25E9%259D%2592%25E9%2593%259C%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C2294776060%257C30%257C2294776060*%257C%257C%257C%257C%2525E6%252588%252591%2525E4%2525B8%2525BA%2525E5%2525B0%25258F%2525E5%2525A5%252588%2525E4%2525B8%25258A%2525E9%25259D%252592%2525E9%252593%25259C*%257C%257C%257C1582919823%2522%252C%2522md5str%2522%253A%25226CA0A15915A8974E6683C6F4702DD9F1%2522%252C%2522roleareaid%2522%253A%252230%2522%252C%2522sPartition%2522%253A%252230%2522%257D; ptui_loginuin=2294776060; tvfe_boss_uuid=550a429e130b2663; o_cookie=2294776060; Qs_lvt_323937=1583745853; Qs_pv_323937=2711233408968657000; pgv_info=ssid=s2973764524; pgv_si=s8986649600; _qpsvr_localtk=0.8156297785618216; uin=o2294776060; skey=@PZsPWhqz5; p_uin=o2294776060; pt4_token=yrDkLg219IyzpY4EYO6kswYgCoZtkhNOvmrnkUS3IRI_; p_skey=IzbehE3gaZhmGLUlwQizCqv-ugNrnNxlxJdFCBLIpfI_; IED_LOG_INFO2=userUin%3D2294776060%26nickName%3D%2525E3%252581%2525BC%2525E3%252581%2525BC%2525E3%252581%252597%2525E3%252582%252593%2525E3%252582%25258A%2525E3%252581%25258F%2525E3%252581%252582%26userLoginTime%3D1583884301; lolqqcomrouteLine=index-tool_main_main_space_space_space_space','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}#cookie里有你账号信息,不带cookie查不到你的游戏数据,User-Agent防止反爬虫
res = requests.get(url1,headers = headers)
# print(res.status_code)  #状态码为200正常
# print(res.text[:1000]) #因数据很多,这里只显示1000字
json1 = json.loads(res.text[16:])#将文本前面16个不是json格式的字符去掉
games = json1['msg']['games']  #获得所有game的列表
gameIds = [] #创建一个存放gameId的列表
for game in games:
    gameId = game['gameId']
    gameIds.append(gameId)
# print('--------------------')
# print(gameIds[:20])#这里我们演示前20个游戏的gameId列表,你想获得多少都可以

#获取游戏数据
for i in gameIds[:20]:
    url2 = 'https://lol.sw.game.qq.com/lol/api/?c=Battle&a=combatGains&areaId=30&gameId=' + str(i) + '&r1=combatGains' #i是int型,需转成str型
    headers = {'Cookie': 'pgv_pvi=8636771328; pgv_pvid=454362090; eas_sid=A175H8A2o7T9Q7o9R2K306C805; RK=HWawDcwC+8; ptcz=241fe16d79e98480d78418fdd47931a86cc2fc0d28830ad3934fd566664b5547; ied_qq=o2294776060; uin_cookie=o2294776060; LOLWebSet_AreaBindInfo_2294776060=%257B%2522areaid%2522%253A%252230%2522%252C%2522areaname%2522%253A%2522%25E7%2594%25B7%25E7%2588%25B5%25E9%25A2%2586%25E5%259F%259F%2520%25E5%2585%25A8%25E7%25BD%2591%25E7%25BB%259C%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25222294776060%2522%252C%2522rolename%2522%253A%2522%25E6%2588%2591%25E4%25B8%25BA%25E5%25B0%258F%25E5%25A5%2588%25E4%25B8%258A%25E9%259D%2592%25E9%2593%259C%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C2294776060%257C30%257C2294776060*%257C%257C%257C%257C%2525E6%252588%252591%2525E4%2525B8%2525BA%2525E5%2525B0%25258F%2525E5%2525A5%252588%2525E4%2525B8%25258A%2525E9%25259D%252592%2525E9%252593%25259C*%257C%257C%257C1582919823%2522%252C%2522md5str%2522%253A%25226CA0A15915A8974E6683C6F4702DD9F1%2522%252C%2522roleareaid%2522%253A%252230%2522%252C%2522sPartition%2522%253A%252230%2522%257D; ptui_loginuin=2294776060; tvfe_boss_uuid=550a429e130b2663; o_cookie=2294776060; Qs_lvt_323937=1583745853; Qs_pv_323937=2711233408968657000; pgv_info=ssid=s2973764524; pgv_si=s8986649600; _qpsvr_localtk=0.8156297785618216; uin=o2294776060; skey=@PZsPWhqz5; p_uin=o2294776060; pt4_token=yrDkLg219IyzpY4EYO6kswYgCoZtkhNOvmrnkUS3IRI_; p_skey=IzbehE3gaZhmGLUlwQizCqv-ugNrnNxlxJdFCBLIpfI_; IED_LOG_INFO2=userUin%3D2294776060%26nickName%3D%2525E3%252581%2525BC%2525E3%252581%2525BC%2525E3%252581%252597%2525E3%252582%252593%2525E3%252582%25258A%2525E3%252581%25258F%2525E3%252581%252582%26userLoginTime%3D1583884301; lolqqcomrouteLine=index-tool_main_main_space_space_space_space','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    res2 = requests.get(url2,headers=headers)
    json2=json.loads(res2.text[18:]) #将前面不是json格式的去掉
    participants = json2['msg']['participants'] #获取一局游戏的10个人的战绩
    #找到自己的战绩
    for own in participants: 
        if own['summonerName'] =='我为小奈上青铜':#输入自己的游戏ID,如果匹配,就继续执行下面的代码,否则跳过
            try: #有的游戏某一项没有数据,用try防止报错,例如大乱斗没有插眼数据,就会报错
                stats = own['stats'] #转到stats这一项中,有战斗数据
                win = stats['win']  #是否胜利,win为赢,fail为输
                kills = stats['kills'] #击杀
                deaths = stats['deaths'] #死亡
                assists = stats['assists'] #助攻
                visionWardsBought = stats['visionWardsBoughtInGame']#买的真眼数
                wardsPlaced = stats['wardsPlaced'] #放置守卫数
                wardsKilled = stats['wardsKilled'] #击杀守卫数
                goldEarned = stats['goldEarned'] #游戏挣的金币
                minionsKilled = stats['minionsKilled'] #击杀小兵
                inhibitorKills = stats['inhibitorKills'] #摧毁水晶
                #你还想写什么可以按照这种方法找,游戏模式,使用英雄,出装,伤害等等都可以
                ws.append([win,kills,deaths,assists,visionWardsBought,wardsPlaced,wardsKilled,goldEarned,minionsKilled,inhibitorKills])
            except:
                print(i)#输出没游戏数据的gameId

        else:
            pass
wb.save('LOLdata\\LOLdata.xlsx')






