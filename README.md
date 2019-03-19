# suit_extensions

suit_extensions是一个用于扩展及优化[django-suit](https://github.com/darklow/django-suit/tree/v.0.2.26)功能的应用

## 安装步骤
1. ```pip install git+https://github.com/kliyes/suit_extensions@master```

2. `INSTALLED_APPS`配置：

   ```python
   INSTALLED_APPS = [
     'suit_extensions',
     'suit',
     'django.contrib.admin',
     ...
   ]
   ```

3. 增加`SUIT_CONFIG`配置项，内容参考[django-suit配置](https://django-suit.readthedocs.io/en/develop/configuration.html)，新增了3个配置项，分别为：

   ```python
   {
     # 是否根据自定义MENU来生成面包屑
     "GENERATE_BREADCRUMBS_FROM_MENU": True,
     # 是否隐藏对象修改界面的工具箱
     "HIDE_OBJECT_TOOLS": True,
     # 是否隐藏对象修改界面的"保存并..."按钮
     "HIDE_SAVE_AND_MORE_BUTTON": True
   }
   ```

## 使用方法

### admin class

同时继承`ExtensionModelAdminMixin`和`ModelAdmin`

```python
from django.contrib import admin

from suit_extensions.mixins import ExtensionModelAdminMixin


@admin.register(ExampleModel)
class ExampleAdmin(ExtensionModelAdminMixin, admin.ModelAdmin):
  pass
```

`suit_extensions`已经对默认的`admin.UserAdmin`和`admin.GroupAdmin`做了修改，如果需要进一步自定义：

```python
from django.contrib.auth import get_user_model

from suit_extensions.admin import ExtendedUserAdmin


UserModel = get_user_model()


class MyUserAdmin(ExtendedUserAdmin):
  pass

admin.site.unregister(UserModel)
admin.site.register(UserModel, MyUserAdmin)
```

## 功能列表

1. 利用`MENU`配置项进行面包屑配置，并使其保持和左侧菜单栏完全一致；
2. 引入`datepicker`和`timepicker`js库替换django自带的时间日期选择器；
