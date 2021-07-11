from bs4 import BeautifulSoup
import requests
import re
import sys

handle = sys.argv[1]
token = sys.argv[2]
readmePath = sys.argv[3]

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 x-ab-param: li_edu_page=old;qap_question_author=0;qap_question_visitor= 0;tp_topic_style=0;pf_noti_entry_num=2;tp_dingyue_video=0;top_test_4_liguangyi=1;se_ffzx_jushen1=0;zr_slotpaidexp=1;tp_zrec=1;li_paid_answer_exp=0;tp_contents=1;li_sp_mqbk=0;li_vip_verti_search=0;li_panswer_topic=0;zr_expslotpaid=1;pf_adjust=1 x-ab-pb: CmJpAUMAVgzsCkcADwuEAk8BtQuQAmALtwB0ATQMnwLPC7QKBwzgC4gBUguJAuQKpgFrAUABWAHSATsC1wsbAIkM9At9AmoBmwuNAQoCTAu0AAELZwBtAtwLRQIqAlsCNww/ABIxAhUBAQABAAADAQACAAACCwABAAABAAAAAgEAAAAAAAAAAAECAAMAAAEAAAABAAABAA==",
    'Host': "www.zhihu.com",
    'Origin': "http://www.zhihu.com",
    'Pragma': "no-cache",
    'Referer': "http://www.zhihu.com/"
}

url = 'https://www.zhihu.com/people/yy6969'

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

# %%
stars = soup.find_all(name='div', attrs={'class': 'css-vurnku'})
print(stars[1].text)  # 点赞、喜欢、收藏

follows = soup.find_all(name='strong', attrs={'class': 'NumberBoard-itemValue'})
print(follows[1].text)  # 关注

# %%


agree, like, collection = re.findall('[0-9,]+', stars[1].text)

zhihu = '获得{}次赞同，{}次喜欢，{}次收藏，{}个关注'.format(agree, like, collection, follows[1].text)

with open(readmePath, "r") as readme:
    content = readme.read()

newContent = re.sub(r"(?<=<!\-\-START_SECTION:zhihu\-followers\-\->)[\s\S]*(?=<!\-\-END_SECTION:zhihu\-followers\-\->)",
                    f"\n{zhihu}\n", content)

with open(readmePath, "w") as readme:
    readme.write(newContent)
