from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict


# Create your views here.

# 课程机构列表功能
class OrgView(View):
    def get(self, request):
        # 查询所有机构和城市的字段信息
        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()

        # 统计后台机构的数量
        org_nums = all_orgs.count()

        # 使用第三方库pure-pagination对机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        return render(request, "org-list.html", {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums
        })
