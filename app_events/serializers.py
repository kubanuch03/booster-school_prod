from rest_framework import serializers

from .models import Events




class EventSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    extended_image = serializers.SerializerMethodField()
    class Meta:
        model = Events
        fields = ['id','title','image','extended_image','datetime','duration','speaker_name','free_spots']

    
    def get_image(self, obj):
        if obj.image:
            return '/media/' + obj.image.url.split('/media/', 1)[-1]  # Добавляем '/media/' к началу части URL-адреса после '/media/'
        return None

    def get_extended_image(self, obj):
        if obj.extended_image:
            return '/media/' + obj.extended_image.url.split('/media/', 1)[-1]  # Добавляем '/media/' к началу части URL-адреса после '/media/'
        return None