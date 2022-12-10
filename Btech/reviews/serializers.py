from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(read_only=True)
    user = serializers.CurrentUserDefault()
    text = serializers.CharField(max_length=255)

    class Meta:
        model = Review
        fields = ["user", "text"]
        extra_kwargs = {"author": {"read_only": True}}

    def get_count_of_likes(self, obj):
        return Review.objects.filter(reviews=obj).count()
