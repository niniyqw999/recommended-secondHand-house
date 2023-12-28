# 数据请求模块
import requests
# 数据解析模块
import parsel


def spider_house():
    # 模拟浏览器
    headers = {
        # 用户代理 表示浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    # 请求链接
    url = 'https://wh.lianjia.com/ershoufang/rs/'
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)  # 选择器对象
    lis = selector.css('.sellListContent li .info')  # 获取所有房源的li标签

    #  创建一个数组存储房源信息
    house_list = []

    #  创建一个类
    class House:
        def __init__(self, _name, _region, _price, _hostype, _size, _direction, _hosplay, _height, _detail):
            self._name = _name
            self._region = _region
            self._price = _price
            self._hostype = _hostype
            self._size = _size
            self._direction = _direction
            self._hosplay = _hosplay
            self._height = _height
            self._detail = _detail

    for li in lis:
        area_info = li.css('.positionInfo a::text').getall()  # 区域信息
        house_info = li.css('.houseInfo::text').get().split(' | ')  # 房源信息
        detail = li.css('.title a::attr(href)').get()  # 跳转信息
        # house_data._name = area_info[0]  # 小区名称
        # house_data._region = area_info[1]  # 小区区域
        # house_data._price = li.css('.totalPrice span::text').get()  # 总价
        # house_data._hostype = house_info[0]  # 户型
        # house_data._size = house_info[1].replace('平米', '')  # 面积
        # house_data._direction = house_info[2]  # 朝向
        # house_data._hosplay = house_info[3]  # 装修
        # house_data._height = house_info[4]  # 楼层
        house_data = House(area_info[0], area_info[1], li.css('.totalPrice span::text').get(), house_info[0],
                           house_info[1].replace('平米', ''), house_info[2], house_info[3], house_info[4], detail)
        # print(house_data)
        house_list.append(house_data)

    # 返回房源列表信息
    return house_list
