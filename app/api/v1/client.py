from flask import request
from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('client')

api.route('register', methods=['POST'])
def create_client():
    data = request.json()
    form = ClienForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email,
        }

    # 注册
    # 参数 检验
    pass

def __register_user_by_email():
    User.register_by_email()