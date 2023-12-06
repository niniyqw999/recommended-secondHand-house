from flask import Flask, request, jsonify, make_response
from flask_mongoengine import MongoEngine
from models import User, House
from flask_cors import CORS
from spiders import spider_house

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
            response.access_control_expose_headers='Authorization'
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
@app.route('/api/houseget/<num>',methods=['GET'])
def house_get(num):
    # 实时爬取房源
    spider_data = spider_house()
    house = House(name = spider_data._name)
    houses = House.objects().limit(num)
    return jsonify({
        'houseData': houses,
        'code': 200
    })


CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # 设置所有接口都允许被跨域访问

if __name__ == '__main__':
    app.debug = True
    app.run()