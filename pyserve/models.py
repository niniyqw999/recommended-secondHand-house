import mongoengine as me


# 用户喜好收集表
class UserSelect(me.Document):
    username = me.StringField()
    name = me.StringField()
    region = me.StringField()
    direction = me.StringField()
    hostype = me.StringField()


# 用户反馈收集表
class UserFeedback(me.Document):
    username = me.StringField()
    uiScore = me.IntField()
    funScore = me.IntField()
    totalScore = me.IntField()
    content = me.StringField()


# 用户信息表
class User(me.Document):
    username = me.StringField(required=True)
    password = me.StringField(required=True)
    liked_house = me.ListField()


# 二手房信息表
class House(me.Document):
    name = me.StringField()
    region = me.StringField()
    price = me.FloatField()
    hostype = me.StringField()
    size = me.FloatField()
    direction = me.StringField()
    hosplay = me.StringField()
    height = me.StringField()
    detail = me.StringField()
