from django.db import models


# Create your models here.

class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言')

    class Meta:
        verbose_name = u'留言信息'
        verbose_name_plural = verbose_name


"""
models 知识点

知识点：CharField必须指明最大长度
Meta信息中我们可以指定常见的类型：
db_table = "表名"
ordering = '-object_id'
verbose_name_plural = u"用户留言信息" 复数形式

"""
