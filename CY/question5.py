class URL:
    def __init__(self, scheme, netloc, path, query_params, fragment):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.query_params = query_params
        self.fragment = fragment
    
def url_parse(url):
    ls_sch = split2piece(url, "://")
    scheme = ls_sch[0]
    ls_netloc = split2piece(ls_sch[1], "/")
    netloc = ls_netloc[0]
    ls_path = split2piece(ls_netloc[1], "?")
    path = "/" + ls_path[0]
    ls_params = split2piece(ls_path[1], "#")
    query_params = get_params_dict(ls_params[0])
    fragment = ls_params[1]
    return URL(scheme, netloc, path, query_params, fragment)

def split2piece(str, split_str):
    count_split_str = len(split_str)
    return [str[:str.find(split_str)], str[str.find(split_str) + count_split_str :]]

def get_params_dict(str_params):
    dic_parm = {}
    ls_params = str_params.split("&")
    for str_p in ls_params:
        if str_p.find("=") > 0:
            ls_key_value = str_p.split("=")
            dic_parm[ls_key_value[0]] = ls_key_value[1]
    return dic_parm


model = url_parse("http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect")
#model = URL('aaa','bbb', 'cccc', {'__biz': 'MzA4MjEyNTA5Mw==', 'mid':'2652566513'}, 'eeee')
print(model.__dict__)