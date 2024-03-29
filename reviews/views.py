from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Review, ReviewLike
from .serializers import ReviewSerializer, ReplySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related("author").all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        review = self.get_object()
        user = request.user

        like = ReviewLike.objects.filter(user=user, review=review).first()

        if like:
            like.delete()
            return Response(
                {"message": "Like removed successfully"}, status=status.HTTP_200_OK
            )

        else:
            like, created = ReviewLike.objects.get_or_create(user=user, review=review)
            return Response(
                ReviewSerializer(review).data, status=status.HTTP_201_CREATED
            )

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def reply(self, request, pk=None):
        review = self.get_object()
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
