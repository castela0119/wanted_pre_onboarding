from functools import total_ordering
from statistics import mode
from django.db import models
# from apps.user.models import User
import datetime
import apps

# Create your models here.
class Products(models.Model):
    title = models.CharField(verbose_name="제목", max_length=20)
    author = models.ForeignKey('user.User', verbose_name="게시자명", related_name="author_user", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="상품설명", max_length=200)
    once_funding = models.IntegerField(verbose_name="1회펀딩금액",)
    total_funding = models.IntegerField(verbose_name="현재펀딩금액", default=0)
    goal_price = models.IntegerField(verbose_name="목표펀딩금액",)
    goal_percent = models.IntegerField(verbose_name="달성률", default=0)
    applicants = models.ManyToManyField('user.User', default={}, related_name='product_applicants')
    today = models.DateField(verbose_name="오늘날짜", auto_now=True)
    end_day = models.DateField(verbose_name="종료날짜", auto_now=False)
    created_at = models.DateField(verbose_name="생성일", auto_now=True)
    updated_at = models.DateField(verbose_name="수정일", auto_now=True)

    class Meta:
        verbose_name_plural = "상품목록"
        db_table = "products"

    def __str__(self) -> str:
        return self.title