# 设置 cookie:
response.set_cookie(
        key,     #键
        value,   #值
        max_age, # 以秒为单位的cookie存活时间
        expires, # 失效时间，这是一个 datetime 的对象
        path,    # 存储的路径
        )

# 获取 cookie
request.cookies.get('key')

# 删除 cookie
response.delete_cookie('key')
