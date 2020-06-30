import json
import urllib.request as req

path_url_lst = [
    (
        'jsons/boxoffice_daily.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'
    ),
    (
        'jsons/boxoffice_weekly.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101'
    ),
    (
        'jsons/code.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/code/searchCodeList.json?key=430156241533f1d058c603178cc3ca0e&comCode=0105000000'
    ),
    (
        'jsons/movie_list.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e'
    ),
    (
        'jsons/movie_info.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20124079'
    ),
    (
        'jsons/company_list.json',
        'http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json?key=430156241533f1d058c603178cc3ca0e'
    ),
    (
        'jsons/company_info.json',
        'http://kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyInfo.json?key=430156241533f1d058c603178cc3ca0e&companyCd=20122497'
    ),
    (
        'jsons/people_list.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key=430156241533f1d058c603178cc3ca0e'
    ),
    (
        'jsons/people_info.json',
        'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.json?key=430156241533f1d058c603178cc3ca0e&peopleCd=20164556'
    ),
]

datas = list()
for path_url in path_url_lst:
    with open(path_url[0], 'w') as f:
        url = req.urlopen(path_url[1])
        data = str(url.read().decode('utf-8'))
        f.write(data)

    with open(path_url[0], 'r') as f:
        datas.append(json.load(f))