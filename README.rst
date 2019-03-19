suit_extensions
===============

suit_extensions是一个用于扩展及优化\ `django-suit <https://github.com/darklow/django-suit/tree/v.0.2.26>`__\ 功能的应用

安装步骤
--------

1. ``pip install git+https://github.com/kliyes/suit_extensions@master``

2. ``INSTALLED_APPS``\ 配置：

   .. code:: python

      INSTALLED_APPS = [
          'suit_extensions',
          'suit',
          'django.contrib.admin',
          ...
      ]

3. 增加\ ``SUIT_CONFIG``\ 配置项，内容参考\ `django-suit配置 <https://django-suit.readthedocs.io/en/develop/configuration.html>`__\ ，新增了3个配置项，分别为：

   .. code:: python

      {
          # 是否根据自定义MENU来生成面包屑
          "GENERATE_BREADCRUMBS_FROM_MENU": True,
          # 是否隐藏对象修改界面的工具箱
          "HIDE_OBJECT_TOOLS": True,
          # 是否隐藏对象修改界面的"保存并..."按钮
          "HIDE_SAVE_AND_MORE_BUTTON": True
      }

使用方法
--------

admin class
~~~~~~~~~~~

####ExtensionModelAdminMixin

同时继承\ ``ExtensionModelAdminMixin``\ 和\ ``ModelAdmin``

.. code:: python

   from django.contrib import admin

   from suit_extensions.mixins import ExtensionModelAdminMixin


   @admin.register(ExampleModel)
   class ExampleAdmin(ExtensionModelAdminMixin, admin.ModelAdmin):
       pass

``suit_extensions``\ 已经对默认的\ ``admin.UserAdmin``\ 和\ ``admin.GroupAdmin``\ 做了修改，如果需要进一步自定义：

.. code:: python

   from django.contrib.auth import get_user_model

   from suit_extensions.admin import ExtendedUserAdmin


   UserModel = get_user_model()


   class MyUserAdmin(ExtendedUserAdmin):
       pass

   admin.site.unregister(UserModel)
   admin.site.register(UserModel, MyUserAdmin)

OperationModelAdminMixin
^^^^^^^^^^^^^^^^^^^^^^^^

在列表页面每一项最后增加一个操作列，默认包括修改和删除按钮：

.. code:: python

   from suit_extensions.mixins import OperationModelAdminMixin


   @admin.register(ExampleModel)
   class ExampleAdmin(OperationModelAdminMixin, admin.ModelAdmin):
       pass

也可修改\ ``operations_list``\ 属性添加自定义操作

datepicker/timepicker
~~~~~~~~~~~~~~~~~~~~~

``django``\ 自带的日期/时间选择器十分不人性化，比如无法快速切换年份（只能逐月选择），\ ``suit_extensions``\ 使用\ ``datepicker``\ 和\ ``timepicker``\ 进行了重写，效果如下：

.. figure:: https://ws2.sinaimg.cn/large/006tKfTcgy1g186hgi2j8j30r40iqgo9.jpg
   :alt: datepicker

   datepicker

.. figure:: https://ws4.sinaimg.cn/large/006tKfTcgy1g186hraqduj30ta0ck75x.jpg
   :alt: timepicker

   timepicker

编写\ ``form``\ ：

.. code:: python

   # forms.py
   from django import forms
   from django.contrib.auth import get_user_model

   from suit_extensions.widgets import DateTimePickerWidget


   UserModel = get_user_model()


   class UserAdminForm(forms.ModelForm):

       class Meta:
           model = UserModel
           fields = "__all__"
           widgets = {
               "last_login": DateTimePickerWidget(
                   datepicker_options={"orientation": "top"}
               ),
               "date_joined": DateTimePickerWidget()
           }

``admin``\ 指定使用上述\ ``form``\ ：

.. code:: python

   # admin.py
   from django.contrib import admin
   from django.contrib.auth import get_user_model

   from suit_extensions.admin import ExtendedUserAdmin

   from .form import UserAdminForm


   UserModel = get_user_model()


   class UserAdmin(ExtendedUserAdmin):
       form = UserAdminForm


   admin.site.unregister(UserModel)
   admin.site.register(UserModel, UserAdmin)

``DateTimePickerWidget``\ 支持两个初始化\ ``dict``\ 类型参数：\ ``datepicker_options``\ 和\ ``timepicker_options``\ ，具体参数值请参考：

``datepicker``\ ：https://bootstrap-datepicker.readthedocs.io/en/latest/options.html

``timepicker``\ ：http://jdewit.github.io/bootstrap-timepicker

功能列表
--------

1. 利用\ ``MENU``\ 配置项进行面包屑配置，并使其保持和左侧菜单栏完全一致；
2. 引入\ ``datepicker``\ 和\ ``timepicker``\ js库替换\ ``django``\ 自带的时间日期选择器；
