from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, error_messages={
                             'unique': '이미 있는 제목이다 임마!'})
    content = models.TextField(
        validators=[MinLengthValidator(10, '너무 짧군요 ! 10자 이상 입력해주세요.'), validate_symbols])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
