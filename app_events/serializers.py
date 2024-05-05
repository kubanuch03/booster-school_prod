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
            return obj.image.url if 'request' not in self.context else self.context['request'].build_absolute_uri(obj.image.url)
        return None
    
    def get_extended_image(self, obj):
        if obj.extended_image:
            return obj.extended_image.url if 'request' not in self.context else self.context['request'].build_absolute_uri(obj.extended_image.url)
        return None