from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery_tasks import celery_app
from django.conf import settings



@celery_app.task()
def generate_static_index_html():
    types = GoodsType.objects.all()
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')  # 轮播图
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')  # 促销活动信息

    for type in types:
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        type.image_banners = image_banners
        type.title_banners = title_banners

    context = {'types': types,
               'goods_banners': goods_banners,
               'promotion_banners': promotion_banners}

    # 加载模板文件
    temp = loader.get_template('static_index.html')
    static_index_html = temp.render(context)
    save_path = os.path.join(settings.BASE_DIR, 'static\\index.html')  # windows路径的问题
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(static_index_html)
