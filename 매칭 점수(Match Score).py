'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : 2019 KAKAO BLIND RECRUITMENT "매칭점수"
comment : 파이썬 re 함수에 대해 자세히 공부할 수 있는 문제였다.
'''

import re


class Node(object):
    def __init__(self, url):
        self.url = url
        self.basicscore = 0
        self.outlinks = []
        self.num_outlinks = 0
        self.matchscore = 0

    def insert_basicscore(self, basic_score):
        self.basicscore += basic_score
        self.matchscore += basic_score

    def insert_outlink(self, url):
        self.outlinks.append(url)
        self.num_outlinks += 1


def find_word(string, word):
    if not string:
        return 0
    string = string.lower()
    comp = re.compile('[^a-z]')
    string = comp.sub(' ', string)
    lt = re.findall(r'\b[a-z]+\b', string)
    cnt = 0
    for w in lt:
        if w == word:
            cnt += 1
    return cnt


def solution(word, pages):
    word = word.lower()
    page_list = []
    dic = {}
    for i, page in enumerate(pages):
        meta = re.search('<meta property.*?>', page)
        url = re.search('https.*(?=")', meta.group()).group()
        page_list.append(Node(url))
        dic[url] = i
        body_start = page.find('<body>', meta.end()) + 6
        body_end = page.find('</body>', body_start)
        body = page[body_start:body_end]

        idx = 0
        basic_score = 0

        while True:
            if not body:
                break
            temp = re.search('<a href.*?</a>', body)
            if not temp:
                basic_score += find_word(body, word)
                page_list[i].insert_basicscore(basic_score)
                break
            else:
                string = body[:temp.start()]
                basic_score += find_word(string, word)
                idx = temp.end()
                outlink = re.search('https.*(?=")', temp.group()).group()
                page_list[i].insert_outlink(outlink)
                body = body[idx:]

    for page in page_list:
        outlinks = page.outlinks
        for link in outlinks:
            if link in dic:
                idx = dic[link]
                page_list[idx].matchscore += (page.basicscore / page.num_outlinks)

    max_score = 0
    max_idx = 0
    for i, page in enumerate(page_list):
        if page.matchscore > max_score:
            max_score = page.matchscore
            max_idx = i

    return max_idx


# Example
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
word = "blind"
print(solution(word, pages))