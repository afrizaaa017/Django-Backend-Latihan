from rest_framework import serializers
from .models import Book
from rest_framework.validators import UniqueValidator

class BookSerializer(serializers.ModelSerializer):
    # Django / DRF validation 
    title = serializers.CharField(
        validators=[
            UniqueValidator(queryset=Book.objects.all(), message="Judul sudah ada.")
        ] 
    )

    class Meta:
        model = Book
        fields = '__all__'

    # Field-level validation
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    # Object-level validation (Kombinasi beberapa field)
    def validate(self, data):
        if data['title'].lower() == data['author'].lower():
            raise serializers.ValidationError("Judul dan penulis tidak boleh sama.")
        return data
