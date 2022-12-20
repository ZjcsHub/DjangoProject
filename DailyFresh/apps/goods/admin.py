from django.contrib import admin
from .models import GoodsType,IndexPromotionBanner
# Register your models here.

class IndexPromotionBannerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        '''保存时触发生成静态页面'''
        super().save_model(request,obj,form,change)
        # 发出任务，重新生成静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

    def delete_model(self, request, obj):
        super().delete_model(request,obj)
        # 发出任务，重新生成静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()


admin.site.register(GoodsType)
admin.site.register(IndexPromotionBanner,IndexPromotionBannerAdmin)