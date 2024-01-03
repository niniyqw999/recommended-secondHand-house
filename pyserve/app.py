import json

from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from models import User, House, UserSelect, UserFeedback
from flask_cors import CORS
from spiders import spider_house, spider_tracks

# 使用Flask类创建一个app对象
# __name__:代表当前app.py这个模块
app = Flask(__name__)

# 绑定配置文件
app.config['MONGODB_SETTINGS'] = {  # 通过MONGODB_SETTINGS配置MongoEngine
    'db': 'second-house'
}
# 初始化MongoEngine配置
db = MongoEngine(app)


# 创建一个路由和试图函数的映射
@app.route('/')
def hello_world():
    return 'Hello World!'


# 在每次请求处理之前执行的钩子
@app.before_request
def before_request():
    if request.path in ['/api/login', '/api/register']:
        return  # 不对登录和注册请求进行token验证
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({
            'message': '无效token',
            'code': 401
        })


# 在每次请求处理之后执行的钩子
@app.after_request
def after_request(response):
    # 在这里可以对响应进行一些额外的处理
    # response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Expose-Headers'] = 'Authorization'  # 在这里添加你想要暴露的响应头属性
    return response


# 用户注册
@app.route('/api/register', methods=['POST'])
def user_register():
    data = request.json  # 获取前端发送的数据
    if User.objects(username=data.get('username')).first():  # 判断用户名是否存在
        return jsonify({
            'message': '用户名已经注册过了',
            'code': 409
        })
    else:
        user = User(username=data.get('username'), password=data.get('password'))  # 添加数据
        user.save()  # 保存添加
        return jsonify({
            'message': '用户注册成功',
            'code': 200
        })


# 用户登录
@app.route('/api/login', methods=['POST'])
def user_login():
    data = request.json  # 获取前端发送的数据
    user = User.objects(username=data.get('username')).first()
    if user:
        if user.password == data.get('password'):
            response = make_response(jsonify({
                'message': '用户登录成功',
                'code': 200
            }))
            response.headers['Authorization'] = f'Bearer {user.username}'
            response.access_control_expose_headers = 'Authorization'
            return response
        else:
            return jsonify({
                'message': '密码错误',
                'code': 400
            })
    else:
        return jsonify({
            'message': '用户不存在',
            'code': 404
        })


# 获取二手房数据
@app.route('/api/house-get/<int:num>', methods=['GET'])
def house_get(num):
    # 实时爬取房源
    spider_data = spider_house()
    # print(spider_data)
    # 逐个房源信息插入数据
    for item in spider_data:
        if House.objects(name=item._name, price=item._price).first():
            print('已经爬取过了的房源')
        else:
            house = House(name=item._name, region=item._region,
                          price=item._price, hostype=item._hostype,
                          size=item._size, direction=item._direction,
                          hosplay=item._hosplay, height=item._height, detail=item._detail)
            house.save()
            print('保存房源信息成功')
    houses = House.objects().limit(num)
    return jsonify({
        'houseData': houses,
        'code': 200
    })


# 二手房房源添加收藏
@app.route('/api/house-like/<hosid>', methods=['GET'])
def house_like(hosid):
    token = request.headers.get('Authorization').split(' ')[1]
    mylike = User.objects(username=token).first()
    # 判断id是否已经存在
    # 存在即移出
    if hosid in mylike.liked_house:
        mylike.liked_house.remove(hosid)
        mylike.save()
        return jsonify({
            'message': '取消收藏成功',
            'code': 204
        })
    # 不存在则添加收藏
    else:
        mylike.liked_house.append(hosid)
        mylike.save()
        return jsonify({
            'message': '添加收藏成功',
            'code': 200
        })


# 获取用户收藏的二手房id
@app.route('/api/liked-get-id', methods=['GET'])
def liked_get_id():
    token = request.headers.get('Authorization').split(' ')[1]  # 获取请求的token
    mylike = User.objects(username=token).first()  # 通过token找寻相应用户收藏的房源id集合
    return jsonify({
        'data': mylike.liked_house,
        'code': 200
    })


#  获取用户收藏的二手房数据
@app.route('/api/liked-get', methods=['GET'])
def liked_get():
    liked_data = []  # 存储收藏的房源数据
    token = request.headers.get('Authorization').split(' ')[1]  # 获取请求的token
    mylike = User.objects(username=token).first()  # 通过token找寻相应用户收藏的房源id集合
    #  遍历所有id获取房源具体信息
    for value in mylike.liked_house:
        house = House.objects(id=value).first()
        liked_data.append(house)  # 插入获取的房源数据
    return jsonify({
        'houseData': liked_data,
        'code': 200
    })


# 搜索相关二手房数据
@app.route('/api/house-search', methods=['POST'])
def house_search():
    data = request.json  # 获取前端发送的数据
    token = request.headers.get('Authorization').split(' ')[1]  # 获取请求的token
    # 存储用户的搜索偏好
    selected = UserSelect(username=token, name=data.get('name'), region=data.get('region'),
                          direction=data.get('direction'), hostype=data.get('hostype'))
    selected.save()
    print('保存用户偏好成功')
    # 定义查询条件
    query = {}
    # 添加条件
    if data.get('name'):
        query['name'] = data.get('name')
    if data.get('region'):
        query['region'] = data.get('region')
    if data.get('direction'):
        query['direction'] = data.get('direction')
    if data.get('hostype'):
        query['hostype'] = data.get('hostype')
    # 查询符合条件的数据
    house = House.objects(__raw__=query)
    if house:
        return jsonify({
            'houseData': house,
            'code': 200
        })
    else:
        return jsonify({
            'message': '没有相关房源信息',
            'code': 204
        })


# 用户反馈信息保存
@app.route('/api/feedback', methods=['POST'])
def feedback():
    data = request.json  # 获取前端发送的数据
    token = request.headers.get('Authorization').split(' ')[1]  # 获取请求的token
    feedbacks = UserFeedback(username=token, uiScore=data.get('uiScore'), funScore=data.get('funScore'),
                             totalScore=data.get('totalScore'), content=data.get('content'))
    feedbacks.save()
    print('用户反馈保存成功')
    return jsonify({
        'message': '反馈提交成功',
        'code': 200
    })


# 房源轨迹获取
@app.route('/api/house-track', methods=['GET'])
def house_track():
    # 实时爬取轨迹
    spider_data = spider_tracks()
    return jsonify({
        'tracksData': spider_data,
        'code': 200
    })


CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # 设置所有接口都允许被跨域访问

if __name__ == '__main__':
    app.debug = True
    app.run()
