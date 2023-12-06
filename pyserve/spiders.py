# 数据请求模块
import requests
# 数据解析模块
import parsel


def spider_house():
    # 模拟浏览器
    headers = {
        # 用户代理 表示浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/115.0.0.0'
                      'Safari/537.36'
    }
    # 请求链接
    url = 'https://m.lianjia.com/wh/ershoufang/index/'
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)  # 选择器对象
    lis = selector.css('.sellListContent li .info')  # 获取所有房源的li标签

    for li in lis:
        area_info = li.css('.positionInfo a::text').getall()  # 区域信息
        _name = area_info[0]  # 小区名称
        _region = area_info[1]  # 小区区域
        _price = li.css('.totalPrice span::text').get()  # 总价
        house_info = li.css('.houseInfo::text').get().split(' | ')  # 房源信息
        _hostype = house_info[0]  # 户型
        _size = house_info[1].replace('平米', '')  # 面积
        _direction = house_info[2]  # 朝向
        _hosplay = house_info[3]  # 装修
        _height = house_info[4]  # 楼层
        house_data = {
            _name,
            _region,
            _price,
            _hostype,
            _size,
            _direction,
            _hosplay,
            _height
        }
        return house_data
