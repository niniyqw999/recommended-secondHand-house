import requests from "./axiosconfig";

//用户注册
export const register = (data) => {
    return requests({
        url: "/register",
        method: "post",
        data
    });
};
//用户登录
export const login = (data) => {
    return requests({
        url: "/login",
        method: "post",
        data
    });
};
//爬虫启动数据准备
export const getData = () => {
    return requests({
        url: "/get-data",
        method: "get"
    });
};
//首页二手房表格数据渲染
export const getHouseData = (num) => {
    return requests({
        url: "/house-get/" + num,
        method: "get"
    });
};
//用户添加收藏
export const addCollect = (id) => {
    return requests({
        url: "/house-like/" + id,
        method: "get"
    });
};
//获取用户收藏的房源id数组
export const getCollectId = () => {
    return requests({
        url: "/liked-get-id",
        method: "get"
    });
};
//用户取消收藏
export const deleteCollect = (id) => {
    return requests({
        url: "/house-unlike/" + id,
        method: "get"
    });
};
//用户个人中心收藏房源数据渲染
export const getCollectData = () => {
    return requests({
        url: "/liked-get",
        method: "get"
    });
};
//搜索相关房源信息并保存用户搜索偏好
export const searchHouse = (data) => {
    return requests({
        url: "/house-search",
        method: "post",
        data
    });
};
//用户反馈信息提交
export const feedback = (data) => {
    return requests({
        url: "/feedback",
        method: "post",
        data
    });
};
//房源轨迹分布获取
export const getHouseTrack = () => {
    return requests({
        url: "/house-track",
        method: "get"
    }
    );
}
//获取房源可视化数据
export const getHouseVisual = () => {
    return requests({
        url: "/house-visual",
        method: "get"
    });
}
