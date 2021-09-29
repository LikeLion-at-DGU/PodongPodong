from django.db import models
from django.urls import reverse


# 식당분류 모델
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 식당 모델
# 식당 기본 정보 : 식당분류, 가게이름, 위치, 전화번호, 오픈시간, 가게사진 (추가예정 : 좋아요(팔로우), 메뉴, 리뷰)
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    business_open_hour = models.DateTimeField()
    business_close_hour = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant:restaurant_detail', args=[self.id])
