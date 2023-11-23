from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import ProductsSerializer, OptionsSerializer, ProductsListSerializer
from .models import DepositOptions, DepositProducts, LikeProducts


@api_view(['GET'])
def index(request):
    api_key = settings.FINANCE_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    bank_list = requests.get(url).json()



    # result = bank_list['result'].keys()
    return Response(bank_list)


# update_or_create 로직으로 다시 만든 데이터 저장 함수
@api_view(['GET'])
def save_DP(request):
    api_key = settings.FINANCE_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    bank_list = requests.get(url).json()

    for li in bank_list.get('result').get('baseList'):
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note': li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
            'dcls_strt_day': li.get('dcls_strt_day'),
            'dcls_end_day': li.get('dcls_end_day'),
        }

        product, created = DepositProducts.objects.update_or_create(
            fin_prdt_cd=save_data['fin_prdt_cd'],
            defaults=save_data
        )

    for li in bank_list.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        save_trm = li.get('save_trm')

        product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)

        intr_rate = li.get('intr_rate')
        if intr_rate is None:
            intr_rate = -1

        intr_rate2 = li.get('intr_rate2')
        if intr_rate2 is None:
            intr_rate2 = -1

        save_data = {
            'product': product,
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        # Filter existing options based on fin_prdt_cd and save_trm
        existing_options = DepositOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            save_trm=save_trm
        )

        if existing_options.exists():
            # If options exist, update the first one (you might want to add more logic here)
            existing_options.update(**save_data)
        else:
            # If no options exist, create a new one
            DepositOptions.objects.create(**save_data)
    DepositOptions.objects.filter(intr_rate = -1).delete()

    return JsonResponse({'message': 'Data saved successfully'})


@api_view(['GET'])
def save_SP(request):
    api_key = settings.FINANCE_API_KEY

    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    bank_list = requests.get(url).json()

    for li in bank_list.get('result').get('baseList'):
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'etc_note': li.get('etc_note'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'join_way': li.get('join_way'),
            'spcl_cnd': li.get('spcl_cnd'),
            'dcls_strt_day': li.get('dcls_strt_day'),
            'dcls_end_day': li.get('dcls_end_day'),
        }

        product, created = DepositProducts.objects.update_or_create(
            fin_prdt_cd=save_data['fin_prdt_cd'],
            defaults=save_data
        )

    for li in bank_list.get('result').get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        save_trm = li.get('save_trm')

        product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)

        intr_rate = li.get('intr_rate')
        if intr_rate is None:
            intr_rate = -1

        intr_rate2 = li.get('intr_rate2')
        if intr_rate2 is None:
            intr_rate2 = -1

        save_data = {
            'product': product,
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }

        # Filter existing options based on fin_prdt_cd and save_trm
        existing_options = DepositOptions.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            save_trm=save_trm
        )

        if existing_options.exists():
            # If options exist, update the first one (you might want to add more logic here)
            existing_options.update(**save_data)
        else:
            # If no options exist, create a new one
            DepositOptions.objects.create(**save_data)
    DepositOptions.objects.filter(intr_rate = -1).delete()

    return JsonResponse({'message': 'Data saved successfully'})


# 요청사항이 'GET'이라면, DepositProducts의 모든 정보를 요청하여 조회하기
# 요청사항이 'POST'라면, DepositProducts가 정보가 생성되는지 확인
@api_view(['GET'])
def deposit_products(request):
    finlifes = get_list_or_404(DepositProducts)
    serializer = ProductsListSerializer(finlifes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_deposit_item(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = ProductsSerializer(product)
    return Response(serializer.data)


# 상품 리스트의 pk값과 options pk 값이 일치하면 pk의 옵션들 모두 출력 
@api_view(['GET'])
def deposit_PO(request, fin_prdt_cd):
    option_list = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = OptionsSerializer(option_list, many=True)
    return Response(serializer.data)


def top_rate(request):
    save_trms = [6, 12, 24, 36]
    recommendations = []

    for save_trm in save_trms:
        # Filter options for the current save_trm
        options = DepositOptions.objects.filter(save_trm=save_trm)

        # Sort options by interest rate in descending order
        sorted_options = sorted(options, key=lambda x: x.intr_rate, reverse=True)

        # Take the top 2 options
        top_options = sorted_options[:3]

        for top_option in top_options:
            top_product = top_option.product

            option_serializer = OptionsSerializer(top_option)
            product_serializer = ProductsSerializer(top_product)

            recommendation_data = {
                'save_trm': save_trm,
                'deposit_product': product_serializer.data,
                'options': option_serializer.data,
            }

            recommendations.append(recommendation_data)

    # Return the recommendations
    response_data = {'recommendations': recommendations}
    return JsonResponse(response_data)

@api_view(['POST'])
def likes(request, product_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=product_cd)

    if request.user in product.like_users.all():
        product.like_users.remove(request.user)
        liked = False
    else:
        product.like_users.add(request.user)
        liked = True

    return JsonResponse({'liked': liked})


@api_view(['GET'])
def liked_products(request):
    liked_products = LikeProducts.objects.filter(user_id=request.user).values('product_id')
    product_ids = [item['product_id'] for item in liked_products]
    
    # Fetch the liked products using the retrieved product ids
    liked_products_data = DepositProducts.objects.filter(fin_prdt_cd__in=product_ids)
    
    serializer = ProductsSerializer(liked_products_data, many=True)
    return Response(serializer.data)


