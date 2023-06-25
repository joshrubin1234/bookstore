from django.urls import path
from .views import CreateRatingView, CreateCommentView
from .views import ListCommentsView, AverageRatingView

app_name = 'ratings'

urlpatterns = [
    path('ratings/', CreateRatingView.as_view(), name='create_rating'),
    path('comments/', CreateCommentView.as_view(), name='create_comment'),
    path('comments/book/', ListCommentsView.as_view(), name='list_comments'),
    path('average-rating/', AverageRatingView.as_view(), name='average_rating'),
]
