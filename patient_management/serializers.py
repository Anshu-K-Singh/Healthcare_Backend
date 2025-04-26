from rest_framework import serializers
from .models import Patient
from .models import Mapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'address']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ['id', 'patient', 'doctor']

    def validate(self, data):
        # Ensure the patient and doctor exist
        if not data.get('patient'):
            raise serializers.ValidationError({'patient': 'This field is required.'})
        if not data.get('doctor'):
            raise serializers.ValidationError({'doctor': 'This field is required.'})
        return data

    def create(self, validated_data):
        # Create the mapping
        return Mapping.objects.create(**validated_data)