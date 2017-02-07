from django.db import models
from django.utils import timezone


# models.Model 상속받은 클래스는 데이터베이스를 생성
class Post(models.Model):
    # 저자, 외래키로 연결 (auth 애플리케이션의 User 모델 사용)
    author = models.ForeignKey('auth.User')
    # 제목, 길이 제한 텍스트
    title = models.CharField(max_length=200)
    # 내용, 길이 제한 없는 텍스트
    content = models.TextField()
    # 생성일자, auto_now_add 이용해서 객체가 생성될 때의 시간을 자동으로 기록
    created_date = models.DateTimeField(auto_now_add=True)
    # 발행일자, 없는 값(null)을 혀용 / 빈 스트링(blank) 허용 : admin 페이지 위젯에 알려주기 위해
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        """
        실행 시 해당 인스턴스의 published_date에 현재시각을 기록하고 DB에 업데이트 해준다.
        """
        self.published_date = timezone.now()
        self.save()
