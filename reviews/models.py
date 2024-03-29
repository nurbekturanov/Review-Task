from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Review(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ReviewLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked_reviews"
    )
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.user} liked "{self.review}"'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="replies")
    parent_reply = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} replied to the {self.review}"
