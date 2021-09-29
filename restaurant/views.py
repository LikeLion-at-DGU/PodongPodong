from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from restaurant.models import Category, Restaurant


# 식당보기 > 식당 리스트가 나오는 페이지
class RestaurantListView(ListView):
    # 어떤 테이블에서 객체 리스트를 가져올 것인지 지정해주기
    model = Restaurant
    # 템플릿 파일로 넘겨주는 객체 리스트의 이름 지정
    context_object_name = 'restaurant_list'
    # 템플릿 파일 위치 지정
    template_name = 'restaurant/category.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 현재 선택된 식당 분류
        context['category'] = Category.objects.all()
        # 선택된 식당 분류에 해당하는 식당 목록
        context['restaurant_list'] = Restaurant.objects.all()
        return context


def RestaurantList(request, id):
    category = Category.objects.all()
    restaurant = Restaurant.objects.all()
    if id:
        current_category = get_object_or_404(Category, id=id)
        restaurant = Restaurant.objects.filter(category=current_category) #다시 필터를 걸어 해당 카테고리 내부의 것들만 모은다.
    context = {'category': category, 'restaurant_list': restaurant}
    return render(request, 'restaurant/category.html', context)


class RestaurantDetailView(DetailView):
    model = Restaurant
    context_object_name = 'restaurant_detail'
    template_name = 'restaurant/restaurant.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # 현재 선택된 식당
        context['restaurant'] = self.restaurant
        return context

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            self.restaurant = Restaurant.objects.get(pk=kwargs['pk'])
        return super().get(request, *args, **kwargs)