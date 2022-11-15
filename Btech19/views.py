from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializers, PodCategorySerializers, ModeliTovarovSerializers
from .models import Category, PodCategories, Modeli_tovarov


@api_view(['GET'])
def categorys_view(request):
    products = Category.objects.all()
    data = CategorySerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def podcategories_view(request):
    products = PodCategories.objects.all()
    data = PodCategorySerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def xiaomi_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def samsung_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def apple_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def honor_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def huawei_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def homephone_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def phone_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Naushnicki_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def PortativnoeAudio_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def VneshnieAkkumulyatori_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Zaryadnyi_ustr_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Kabeli_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Chehly_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def SteklaAndPlenki_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def SD_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def VseBrendy_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Samsung_Galaxy_Tab_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Apple_Ipad_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def HuweiMatepad_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Xiaomi_Tab_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Tablet_accessories_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def E_books_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def Smartclock_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def Fitnesclock_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def Sportclock_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def Kidsclock_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def UmnyeKolonki_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def Smarthome_view(request):
    products = Modeli_tovarov.objects.all()
    data = ModeliTovarovSerializers(products, many=True).data
    return Response(data=data)
