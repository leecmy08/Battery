from django.conf import settings
from django.db import models

from drf_admin.utils.models import BaseModel


# Create your models here.
class ErrorLogs(BaseModel):
    """
    错误日志
    """
    username = models.CharField(max_length=32, verbose_name='用户')
    view = models.CharField(max_length=32, verbose_name='视图')
    desc = models.TextField(verbose_name='描述')
    ip = models.GenericIPAddressField(verbose_name='IP')
    detail = models.TextField(verbose_name='详情')

    objects = models.Manager()

    class Meta:
        db_table = 'monitor_errorlogs'
        verbose_name = '错误日志'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class IpBlackList(BaseModel):
    """
    ip黑名单
    """
    ip = models.GenericIPAddressField(unique=True, verbose_name='IP')

    objects = models.Manager()

    class Meta:
        db_table = 'monitor_ipblacklist'
        verbose_name = 'IP黑名单'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class OnlineUsers(BaseModel):
    """
    在线用户
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户')
    ip = models.GenericIPAddressField(verbose_name='IP')

    objects = models.Manager()

    class Meta:
        db_table = 'monitor_onlineusers'
        verbose_name = '在线用户123'
        verbose_name_plural = verbose_name
        ordering = ['-id']


#（一）	回收过程表格+示例数据
class Test_Info(BaseModel):
    recovery_time=models.DateTimeField(null=True, blank=True, verbose_name="回收时间")
    battery_id = models.CharField(max_length=256, null=True)  # CharField代表字符型， INtergerField是整形，在这里改完后执行两条迁移命令就好了
    battery_type = models.CharField(max_length=256, null=True)
    battery_category = models.CharField(max_length=256, null=True)
    manufacturer= models.CharField(max_length=256, null=True)
    nominal_capacity=models.IntegerField(null=True)
    standard_voltage=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    size=models.CharField(max_length=256, null=True)
    
#（二）	拆解表格
class Disassemble_Info(BaseModel):
    disassembly_time=models.DateTimeField(null=True, blank=True, verbose_name="拆解时间")
    battery_module_id= models.CharField(max_length=256, null=True)  # CharField代表字符型， INtergerField是整形，在这里改完后执行两条迁移命令就好了
    module_battery_model=models.CharField(max_length=256, null=True)
    battery_category=models.CharField(max_length=256, null=True)
    manufacturer= models.CharField(max_length=256, null=True)
    nominal_capacity=models.IntegerField(null=True)
    standard_voltage=models.FloatField(null=True)
    weight=models.FloatField(null=True)
    size=models.CharField(max_length=256, null=True)

#（三）	拆解统计表格
class Disassemble_Statistical_Info(BaseModel):
    disassemble_system_run_time=models.CharField(max_length=256, null=True)
    disassemble_battery_num=models.CharField(max_length=256, null=True)
    disassemble_battery_module_num=models.CharField(max_length=256, null=True)

#（四）	储能及电芯配置信息

class Energy_Storage_Info(BaseModel):
     energy_storage_unit_name=models.CharField(max_length=256, null=True)
     battery_type=models.CharField(max_length=256, null=True)
     battery_standard_voltage=models.FloatField(null=True)
     energy_storage_unit_capacity=models.IntegerField(null=True)
     energy_storage_unit_voltage=models.IntegerField(null=True)
     group_mode=models.CharField(max_length=256, null=True)
     run_time=models.FloatField(null=True)
     run_day222333=models.FloatField(null=True)
    
#（五）	实时数据
class Energy_Storage_Data(BaseModel):
     time_stamp=models.DateTimeField(null=True, blank=True, verbose_name="时间戳")
     energy_storage_unit_name=models.CharField(max_length=256, null=True)
     voltage_1=models.FloatField(null=True)
     voltage_2=models.FloatField(null=True)
     voltage_3=models.FloatField(null=True)
     voltage_4=models.FloatField(null=True)
     voltage_5=models.FloatField(null=True)
     voltage_6=models.FloatField(null=True)
     voltage_7=models.FloatField(null=True)
     voltage_8=models.FloatField(null=True)
     electric_current=models.FloatField(null=True)
     temp=models.FloatField(null=True)
#（六）	充电容量实时表
class Charge_Capacity_Data(BaseModel):
     time_stamp=models.DateTimeField(null=True, blank=True, verbose_name="时间戳")
     charge_capacity=models.FloatField(null=True)
     discharge_capacity=models.FloatField(null=True)

#（七）	所在地电价表
class Local_Electricity_Price(BaseModel):
     month=models.CharField(max_length=256, null=True)
     province=models.CharField(max_length=256, null=True)
     peak_price=models.FloatField(null=True)
     top_price=models.FloatField(null=True)
     valle_price=models.FloatField(null=True)
     flat_price=models.FloatField(null=True)
     public_subsidies=models.FloatField(null=True)
#（七）	外部交易数据
class External_Transaction_Data(BaseModel):
        name=models.FloatField(null=True)
        unit=models.FloatField(null=True)
        example=models.FloatField(null=True)
        collect_form=models.FloatField(null=True)
        data_type=models.FloatField(null=True)
#（八）	峰谷套利效益表
class PeakVally_Benefit_Data(BaseModel):
        month=models.CharField(max_length=256, null=True)
        charge_capacity=models.FloatField(null=True)
        charge_time=models.CharField(max_length=256, null=True)
        discharge_capacity=models.FloatField(null=True)
        discharge_time=models.CharField(max_length=256, null=True)
        Benefit=models.FloatField(null=True)
#（九）	调频效益表
class Frequency_Modulation_Benefit_Data(BaseModel):
        month=models.CharField(max_length=256, null=True)
        frequency_mile=models.FloatField(null=True)  
        frequency_day=models.FloatField(null=True)  
        frequency_coefficient=models.FloatField(null=True)  
        frequency_subsidies=models.FloatField(null=True)  
        frequency_benefit=models.FloatField(null=True)  
