## 模块
1. pipenv
2. django-2.2
3. djangorestframework-3.9.2
4. django-cors-headers-2.5.2
5. django-rest-swagger-2.2.0
6. djangorestframework-jwt

## 问题
通过restframework编写的restful api，需要解决用户验证、自动文档、跨域问题
### 1. rest api(djangorestframework)
### 2. JTW验证(djangorestframework-jwt)
```
config.headers['Authorization'] = `JWT ${token}`
```
### 3. 自动文档(django-rest-swagger)
登录路由跳转
```
url(r'^accounts/', include('rest_framework.urls','rest_framework_swagger.urls'))
```
### 4. cors(djangorestframework)
```
CORS_ORIGIN_WHITELIST = {
  // host
}
```