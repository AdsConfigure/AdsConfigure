import requests
import json
import time
import datetime
from urllib import parse
import threading
import sys

readmePath = sys.argv[3]

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 x-ab-param: li_edu_page=old;qap_question_author=0;qap_question_visitor= 0;tp_topic_style=0;pf_noti_entry_num=2;tp_dingyue_video=0;top_test_4_liguangyi=1;se_ffzx_jushen1=0;zr_slotpaidexp=1;tp_zrec=1;li_paid_answer_exp=0;tp_contents=1;li_sp_mqbk=0;li_vip_verti_search=0;li_panswer_topic=0;zr_expslotpaid=1;pf_adjust=1 x-ab-pb: CmJpAUMAVgzsCkcADwuEAk8BtQuQAmALtwB0ATQMnwLPC7QKBwzgC4gBUguJAuQKpgFrAUABWAHSATsC1wsbAIkM9At9AmoBmwuNAQoCTAu0AAELZwBtAtwLRQIqAlsCNww/ABIxAhUBAQABAAADAQACAAACCwABAAABAAAAAgEAAAAAAAAAAAECAAMAAAEAAAABAAABAA==',

}

url='https://www.zhihu.com/people/yy6969'

voteupCounttemp = 0
thankedCounttemp = 0
followerCounttemp = 0
changecount=0

def getzhihustatus():
    global voteupCounttemp
    global thankedCounttemp
    global followerCounttemp
    global changecount
    global readmePath
    r = requests.get(url=url, headers=headers)
    index1 = r.text.find('zhihu:voteupCount" content="')
    index2 = r.text.find('"/><meta itemProp="zhihu:thankedCount"')
    s = ''
    for i in range(index1, index2):
        s = s + r.text[i]
    voteupCount = int(s.replace('zhihu:voteupCount" content="', ''))

    if(voteupCounttemp==0):
        voteupCounttemp=voteupCount
    if(voteupCounttemp!=voteupCount):
        changecount=voteupCount-voteupCounttemp
        if(changecount>0):
            with open(readmePath, "a") as readme:
                s=time.strftime('%Y-%m-%d  %H:%M:%S')+f'   点赞数 +{changecount} >>>> {voteupCount}'
                readme.write(s)
        elif(changecount<0):
            with open(readmePath, "a") as readme:
                s=time.strftime('%Y-%m-%d  %H:%M:%S')+f'   点赞数 {changecount} >>>> {voteupCount}'
                readme.write(s)
    voteupCounttemp=voteupCount

    index1 = r.text.find('"zhihu:thankedCount" content="')
    index2 = r.text.find('"/><meta itemProp="zhihu:followerCount"')
    s = ''
    for i in range(index1, index2):
        s = s + r.text[i]
    thankedCount = int(s.replace('"zhihu:thankedCount" content="', ''))
    if (thankedCounttemp == 0):
        thankedCounttemp = thankedCount

    if (thankedCounttemp != thankedCount):
        changecount = thankedCount - thankedCounttemp
        if (changecount > 0):
            with open(readmePath, "a") as readme:
                readme.write(time.strftime('%Y-%m-%d  %H:%M:%S')+f'   喜欢数 +{changecount} >>>> {thankedCount}')
        elif (changecount < 0):
            with open(readmePath, "a") as readme:
                readme.write(time.strftime('%Y-%m-%d  %H:%M:%S')+f'   喜欢数 {changecount} >>>> {thankedCount}')
        thankedCounttemp=thankedCount

    index1 = r.text.find('itemProp="zhihu:followerCount" content="')
    index2 = r.text.find('"/><meta itemProp="zhihu:answerCount"')
    s = ''
    for i in range(index1, index2):
        s = s + r.text[i]
    followerCount = int(s.replace('itemProp="zhihu:followerCount" content="', ''))
    if (followerCounttemp == 0):
        followerCounttemp = followerCount

    if (followerCounttemp != followerCount):
        changecount = followerCount - followerCounttemp
        if (changecount > 0):
            with open(readmePath, "a") as readme:
                readme.write(time.strftime('%Y-%m-%d  %H:%M:%S')+f'   粉丝数 +{changecount} >>>> {followerCount}')
        elif (changecount < 0):
            with open(readmePath, "a") as readme:
                readme.write(time.strftime('%Y-%m-%d  %H:%M:%S')+f'   粉丝数 {changecount} >>>> {followerCount}')
        followerCounttemp=followerCount
    changecount = 0


if __name__=='__main__':
    a=1
    while(True):
        a=a+1
        if a>60:
            break
            
        try:
            getzhihustatus()
            time.sleep(1)
        except Exception as e:
            with open(readmePath, "w") as readme:
                readme.write("Exception:"+str(e))
            break
            pass
        
    
 
# newContent = re.sub(r"(?<=<!\-\-START_SECTION:zhihu\-followers\-\->)[\s\S]*(?=<!\-\-END_SECTION:zhihu\-followers\-\->)",
#                     f"\n{zhihu}\n", content)

#     with open(readmePath, "w") as readme:
#         readme.write(newContent)
