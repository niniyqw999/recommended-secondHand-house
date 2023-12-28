import axios from 'axios'

//创建axios实例
const requests = axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,
})

//请求拦截器
requests.interceptors.request.use(config => {
    const token = localStorage.getItem('token')
    config.headers['Authorization'] = 'Bearer ' + token
    return config
}, error => {
    return Promise.reject(error)
}
)
//响应拦截器
requests.interceptors.response.use(response => {
    // console.log(response.headers)
    const { authorization } = response.headers
    if (authorization) {
        const token = authorization.split(' ')[1]
        authorization && localStorage.setItem('token', token)
    }
    return response.data
}, error => {
    if (error.response && error.response.status === 401) {
        localStorage.removeItem('token')
        window.location.href = '/login'
    }
    return Promise.reject(error)
})
export default requests