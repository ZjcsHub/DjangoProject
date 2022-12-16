from redis import StrictRedis

if __name__ == '__main__':
    # 创建redis对象，连接redis

    try:
        sr = StrictRedis()
        # 添加key name，value jckeats
        res = sr.set('name','jckeats')
        print(res)

        # 获取
        res = sr.get('name')
        print(res)

        # 修改
        res = sr.set('name','keats')
        print(res)

        # 删除
        res = sr.delete('name')
        print(res)

        # 删除多个
        res = sr.delete('a1','a2')
        print(res)

        # 获取数据库中所有的键
        res = sr.keys()
        print(res)

    except Exception as e:
        print(e)
