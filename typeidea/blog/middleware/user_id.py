import uuid

USER_KEY = 'uid'
TEM_YEARS = 60 * 60 * 24 * 365 * 10


class UserIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        uid = self.generate_uid(request)
        request.uid = uid  # request是一个类的实例，所以可以动态赋值
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEM_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        try:
            uid = request.COOKIES[USER_KEY]  # 如果已经设置过就用这个
        except KeyError:
            uid = uuid.uuid4().hex  # 没有设置过就创建
            return uid
