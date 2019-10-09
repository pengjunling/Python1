av_catlog = {
    '欧美':{
        'www.1.com':['免费','很好'],
        'www.2.com':['1kuaiqian','buhao']
    },
    'stu01': 'oldboy'
}
b = {
    'stu01':'alex',
    1:2,
    2:3,
    3:4
}
av_catlog['欧美']['www.1.com'][1] = '不好'
print(av_catlog['欧美']['www.1.com'][1])
print(av_catlog)
print(av_catlog.values())
print(av_catlog.keys())
print(av_catlog.update(b))
print(av_catlog)
print(av_catlog.items())