from django.db import models
import uuid 
import random
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Categories(BaseModel):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Question(BaseModel):
    category = models.ForeignKey(Categories, related_name='category', on_delete=models.CASCADE)
    question = models.TextField()
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        random.shuffle((answer_objs))
        data = []
        for answer_obj in answer_objs:
            data.append({
                'answer' : answer_obj.answer,
                'is_correct' : answer_obj.is_correct,
            })
        return data 

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(BaseModel):
    question = models.ForeignKey(Question,related_name='question_answer' , on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'