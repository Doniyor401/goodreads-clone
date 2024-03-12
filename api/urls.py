from django.urls import path
# from api.views import BookReviewDetailAPIView, BookReviewsAPIView
from rest_framework.routers import DefaultRouter
from api.views import BookReviewViewSet

app_name = 'api'

router = DefaultRouter()
router.register('reviews', BookReviewViewSet, basename='review')

# urlpatterns = [
#     path("reviews/", BookReviewsAPIView.as_view(), name="review-list"),
#     path("reviews/<int:id>/", BookReviewDetailAPIView.as_view(), name="review-detail"),
# ]

urlpatterns = router.urls
