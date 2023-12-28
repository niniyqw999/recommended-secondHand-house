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
//首页二手房表格数据渲染
export const getHouseData = (num) => {
    return requests({
        url: "/house-get/" + num,
        method: "get"
    });
};
