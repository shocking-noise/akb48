# -*- coding: utf-8 -*-
import urllib2
import re
import datetime
import time
import yaml

from BeautifulSoup import BeautifulSoup

URL = "http://www23.atpages.jp/akb49/?%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC"
soup = BeautifulSoup(urllib2.urlopen(URL).read())

out = []
team_list = ["A", "K", "B", "4", "student"]
for i, t in enumerate(soup('table', cellspacing="1", border="0")):
    for tr in t('tr'):
        if len(tr('td')[1]('span')) > 0:
            member = {}
            member["name"] = tr('td')[1]('a')[0].text
            member["kana"] = tr('td')[1]('span')[0].text
            member["nickname"] = re.sub(".*/>([^<]*)</td>.*", "\\1", str(tr('td')[1]))
            birthday = re.sub(u"[年月日]", "", re.sub(u"（.*", "", tr('td')[2].text))
            _tpl = time.strptime(birthday, "%Y%m%d")
            member["birthday"] = datetime.date(_tpl[0], _tpl[1], _tpl[2])
            member["team"] = team_list[i]
            member["join"] = re.sub(u"期", "", tr('td')[3].text)
            out.append(member)
yaml.dump(out, open("member.yaml", "w"))
