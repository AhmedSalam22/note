from rest_framework import serializers
from NoteAPI.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        note = Note.objects.create(author= user, **validated_data)

        return note