# 数据请求模块
import requests
# 数据解析模块
import parsel


# 爬取二手房房源数据
def spider_house():
    # 模拟浏览器
    headers = {
        # 用户代理 表示浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    #  创建一个数组存储房源信息
    house_list = []
    #  存储所有房源区域信息
    region_list = ['jiangran', 'jianghan', 'qiaoko', 'dongxihu', 'wucang', 'qingshan', 'hongshan', 'hanyang',
                   'donghugaoxin', 'jiangxia', 'caidian', 'huangbei', 'xinzhou', 'zhuankoukaifaqu', 'hannan']
    # 循环爬取每个区域的房源
    for region in region_list:
        print(f'正在采集{region}地区的房源数据')
        for page in range(1, 101):
            print(f'正在采集第{region}地区{page}页的房源数据')
            # 请求链接
            url = f'https://wh.lianjia.com/ershoufang/{region}/pg{page}/'
            response = requests.get(url=url, headers=headers)
            selector = parsel.Selector(response.text)  # 选择器对象
            lis = selector.css('.sellListContent li .info')  # 获取所有房源的li标签

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
                                   house_info[1].replace('平米', '') if len(house_info) > 1 else '',
                                   house_info[2] if len(house_info) > 2 else '',
                                   house_info[3] if len(house_info) > 3 else '',
                                   house_info[4] if len(house_info) > 4 else '',
                                   detail)
                # print(house_data)
                house_list.append(house_data)

    # 返回房源列表信息
    return house_list


# 爬取二手房分布坐标点
def spider_tracks():
    # 模拟浏览器
    headers = {
        # 用户代理 表示浏览器基本身份信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Cookie': 'SECKEY_ABVK=p6MshofTdJjoez3XoPPisTHgY2j9p28EBOO04xbFyjUUvuBCOtzs39uoCsT/yy+L/ccbrJxvnh8TFIdYs3O3Dw'
                  '%3D%3D; '
                  'BMAP_SECKEY'
                  '=p6MshofTdJjoez3XoPPisTHgY2j9p28EBOO04xbFyjVtvtn8CnsWpL5qu3vuGSSkhqKUlwnv96gWnP1fO3O5TdLvrVlhCwkWAFlf5kjGOyw23nPEzeKLhWKy6PmsbOM3QUNHXMHwVfHmTMgEgntKwCJRKXqvfwNTSAmVRpVNPAqEoLbrAehs5JXsL32PNqcjxsdE2YstwljDBZwAzdw2ag; lianjia_uuid=c8b8ae31-4603-4e70-b41b-9e5877452859; _smt_uid=657e7db9.4ed2702e; _ga=GA1.2.875050548.1702788539; select_city=420100; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1703655075,1703739863,1703925324,1704263022; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218c761b1c38b53-021aaded85d0f-4c657b58-1024000-18c761b1c39b95%22%2C%22%24device_id%22%3A%2218c761b1c38b53-021aaded85d0f-4c657b58-1024000-18c761b1c39b95%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.1363103658.1704263024; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1704271337; _ga_BGW2B8P0NN=GS1.2.1704271339.11.0.1704271339.0.0.0'

    }
    url = 'https://map.lianjia.com/map/420100/ESF/'
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)  # 选择器对象
    print(selector)
    labels = selector.css('.BMapLabel')
    print(labels)
    # 存储所有轨迹的数组
    tracks = []
    for label in labels:
        target = label.css('.district::attr(data-polygon_border)').get()
        house_track = [[float(point.split(",")[0]), float(point.split(",")[1]), 1] for point in target.split(";") if
                       point]
        tracks.extend(house_track)  # 合并数组
    return tracks
