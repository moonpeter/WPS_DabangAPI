from rest_framework import serializers
from rest_framework.fields import DictField, CharField, ListField, SerializerMethodField
from rest_framework.relations import StringRelatedField

from .models import PostRoom, PostImage, Broker, MaintenanceFee, RoomOption, PostAddress, RoomSecurity, SalesForm, \
    OptionItem, SecuritySafetyFacilities, ComplexInformation, ComplexImage, RecommendComplex


class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = (
            'pk', 'companyName', 'address', 'managerName', 'tel', 'image', 'companyNumber', 'brokerage',
            'dabangCreated_at', 'successCount'
        )

    # def create(self, validated_data):
    #     broker = validated_data.pop('broker')
    #     instance = Broker.objects.create(**validated_data)
    #     return instance
    # def create(self, validated_data):
    #     return Broker.objects.get_or_create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.manager = validated_data.get('manager', instance.manager)
    #     instance.tel = validated_data.get('tel', instance.tel)
    #     instance.save()
    #     return instance


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceFee
        fields = (
            'postRoom', 'admin', 'totalFee',
        )


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionItem
        fields = (
            'name',
        )


class SecuritySafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecuritySafetyFacilities
        fields = (
            'name',
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAddress
        fields = (
            'loadAddress', 'detailAddress',
        )


class SalesFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesForm
        fields = (
            'type', 'depositChar', 'monthlyChar', 'depositInt', 'monthlyInt',
        )


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = (
            'image',
        )


class RecommendComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendComplex
        fields = '__all__'


class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        field = 'image'


class ComplexInformationSerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField(source='compleximage_set', many=True, )
    # list = serializers.SerializerMethodField()RecommendComplex
    recommend = RecommendComplexSerializer(many=True, source='recommendcomplex_set')

    def get_list(self, obj):
        import random
        return_list = []
        TNF = False
        query_set_len = ComplexInformation.objects.all()
        query_set_len = len(query_set_len)
        rand_pk = random.randint(1, query_set_len)
        complex_pk = ComplexInformation.objects.get(pk=query_set_len)
        # if i in list

    class Meta:
        model = ComplexInformation
        fields = (
            'pk',
            'complexName',
            'buildDate',
            'totalCitizen',
            'personalPark',
            'totalNumber',
            'heatingSystem',
            'minMaxFloor',
            'buildingType',
            'constructionCompany',
            'fuel',
            'complexType',
            'floorAreaRatio',
            'dryWasteRate',
            'complexSale',
            'complexPrice',
            'areaSale',
            'areaPrice',
            'image',
            # 'list',
            'recommend',
        )


class PostListSerializer(serializers.ModelSerializer):
    broker = BrokerSerializer(read_only=True)
    management_set = serializers.StringRelatedField(source='management', many=True, read_only=True)
    option_set = serializers.StringRelatedField(source='option', many=True, read_only=True)
    securitySafety_set = serializers.StringRelatedField(source='securitySafety', many=True, read_only=True)
    address = AddressSerializer(read_only=True, allow_null=True)
    salesForm = SalesFormSerializer(read_only=True)
    postimage = serializers.StringRelatedField(source='postimage_set', many=True)
    complex = ComplexInformationSerializer(read_only=True, )

    class Meta:
        model = PostRoom
        fields = [
            'pk',
            'broker',
            'type',
            'description',
            'address',
            'lng',
            'lat',
            'salesForm',
            'floor',
            'totalFloor',
            'areaChar',
            'supplyAreaInt',
            'supplyAreaChar',
            'shortRent',
            'management_set',
            'parkingDetail',
            'parkingTF',
            'living_expenses',
            'living_expenses_detail',
            'moveInChar',
            'moveInDate',
            'option_set',
            'heatingType',
            'pet',
            'elevator',
            'builtIn',
            'veranda',
            'depositLoan',
            'totalCitizen',
            'totalPark',
            'complete',
            'securitySafety_set',
            'postimage',
            'complex',
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    address = DictField(child=CharField(), allow_empty=True, )
    salesForm = DictField(child=CharField(), )
    management_set = ListField()
    option_set = ListField()
    securitySafety_set = ListField()

    class Meta:
        model = PostRoom
        # fields = '__all__'
        fields = [
            'pk',
            'broker',
            'type',
            'description',
            'salesForm',
            'floor',
            'totalFloor',
            'areaChar',
            'supplyAreaInt',
            'supplyAreaChar',
            'shortRent',
            'management_set',
            'parkingDetail',
            'parkingTF',
            'living_expenses',
            'living_expenses_detail',
            'moveInChar',
            'moveInDate',
            'option_set',
            'heatingType',
            'pet',
            'elevator',
            'builtIn',
            'veranda',
            'depositLoan',
            'totalCitizen',
            'totalPark',
            'complete',
            'securitySafety_set',
            'address',
            # 'postimage',
        ]
