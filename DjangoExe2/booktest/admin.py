from django.contrib import admin
from .models import BookInfo,HeroInfo,AreaInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle']


class AreaStackInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    # 控制底部可添加数目
    extra = 2

class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 # 指定每页显示个数
    list_display = ['id','atitle','title','parent']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle'] # 页面右侧过滤栏
    search_fields = ['atitle'] # 列表页上方搜索框

    # fields = ['aParent','atitle'] # 编辑也显示顺序
    fieldsets = (
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']})
    )

    # inlines = [AreaStackInline]
    inlines = [AreaTabularInline]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
admin.site.register(AreaInfo ,AreaInfoAdmin)