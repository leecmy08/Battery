# -*- coding: utf-8 -*-
"""
@author   : Wang Meng
@github   : https://github.com/tianpangji 
@software : PyCharm 
@file     : urls.py
@create   : 2020/9/9 20:07
"""
from django.urls import path, include

from drf_admin.utils import routers
from monitor.views import users, service, error, ip, crud,excel

router = routers.AdminRouter()
router.register(r'ip', ip.IpBlackListViewSet, basename="ip")  # ip黑名单管理
urlpatterns = [
    path('users/', users.OnlineUsersListAPIView.as_view()),  # 在线用户监控
    path('service/', service.ServiceMonitorAPIView.as_view()),  # 服务监控
    path('error/', error.ErrorLogAPIView.as_view()),  # 错误日志监控
    path('crud/', crud.CRUDListAPIView.as_view()),  # CRUD变更记录
    path('upload1/',excel.ExcelUploadView.as_view()),    #test_info 表
    path('disassembleinfo/',excel.DisassembleInfoView.as_view()),    #Disassemble_Info 表
    path('disassemblestatisticalinfo/',excel.DisassembleStatisticalInfoView.as_view()),    #DisassembleStatisticalInfoView 表
    path('energystorageinfo/',excel.EnergyStorageInfoView.as_view()),                     #EnergyStorageInfoView表
    path('energystoragedata/',excel.EnergyStorageDataView.as_view()),    #EnergyStorageDataView 表
    path('chargecapacitydata/',excel.ChargeCapacityDataView.as_view()),    #ChargeCapacityDataView 表
    path('localelectricityprice/',excel.LocalElectricityPriceView.as_view()),    #LocalElectricityPriceView 表
    path('externaltransactiondata/',excel.ExternalTransactionDataView.as_view()),    #ExternalTransactionDataView 表
    path('peakvallybenefitdata/',excel.PeakVallyBenefitDataView.as_view()),    #PeakVallyBenefitDataView 表
    path('frequencymodulationbenefitdata/',excel.FrequencyModulationBenefitDataView.as_view()),    #FrequencyModulationBenefitDataView 表
    


    
    path('', include(router.urls)),
]
