from flask import Blueprint

demo = Blueprint('demo', __name__)

# 导入 demo_views
# 用于对 demo blueprint 进行更多渲染
from .views import demo_view
