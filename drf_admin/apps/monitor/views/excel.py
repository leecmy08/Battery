import xlrd
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from monitor.models import Test_Info,Disassemble_Info,Disassemble_Statistical_Info,Energy_Storage_Info,Energy_Storage_Data,Charge_Capacity_Data,Local_Electricity_Price,External_Transaction_Data,PeakVally_Benefit_Data,Frequency_Modulation_Benefit_Data
from django.views import View
from django.db.models import Sum,Avg,Max,Min
from monitor.config.pagination import Pagination

def upload(request):
    return render(request,"upload.html")

#Test_Info接口
class ExcelUploadView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Test_Info.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Test_Info.objects.all()[pager.start: pager.end]
        else:
            test_list = Test_Info.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'recovery_time':test.recovery_time,
                'battery_id': test.battery_id,
                'battery_type': test.battery_type,
                'battery_category': test.battery_category
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Test_Info.objects.create(battery_id=a.value,battery_type=b.value,battery_category=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Disassemble_Info接口              
class DisassembleInfoView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Disassemble_Info.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Disassemble_Info.objects.all()[pager.start: pager.end]
        else:
            test_list = Disassemble_Info.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'disassembly_time': test.disassembly_time,
                'battery_module_id': test.battery_module_id,
                'module_battery_model': test.module_battery_model,  
                'battery_category': test.battery_category,
                'manufacturer': test.manufacturer,
                'nominal_capacity': test.nominal_capacity,
                'standard_voltage': test.standard_voltage,
                'weight': test.weight,
                'size': test.size

            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Disassemble_Info.objects.create(battery_module_id=a.value,module_battery_model=b.value,battery_category=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Disassemble_Statistical_Info接口              
class DisassembleStatisticalInfoView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Disassemble_Statistical_Info.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Disassemble_Statistical_Info.objects.all()[pager.start: pager.end]
        else:
            test_list = Disassemble_Statistical_Info.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'disassemble_system_run_time': test.disassemble_system_run_time,
                'disassemble_battery_num': test.disassemble_battery_num,
                'disassemble_battery_module_num': test.disassemble_battery_module_num,  
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Disassemble_Statistical_Info.objects.create(disassemble_system_run_time=a.value,disassemble_battery_num=b.value,disassemble_battery_module_num=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Energy_Storage_Info接口              
class EnergyStorageInfoView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Energy_Storage_Info.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Energy_Storage_Info.objects.all()[pager.start: pager.end]
        else:
            test_list = Energy_Storage_Info.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'energy_storage_unit_name': test.energy_storage_unit_name,
                'battery_type': test.battery_type,
                'battery_standard_voltage': test.battery_standard_voltage,  
                'energy_storage_unit_capacity': test.energy_storage_unit_capacity,  
                'energy_storage_unit_voltage': test.energy_storage_unit_voltage,  
                'group_mode': test.group_mode,  
                'run_time': test.run_time,  
                'run_day': test.run_day,                  
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Energy_Storage_Info.objects.create(energy_storage_unit_name=a.value,battery_type=b.value,battery_standard_voltage=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Energy_Storage_Data接口              
class EnergyStorageDataView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Energy_Storage_Data.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Energy_Storage_Data.objects.all()[pager.start: pager.end]
        else:
            test_list = Energy_Storage_Data.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'time_stamp': test.time_stamp,
                'energy_storage_unit_name': test.energy_storage_unit_name,
                'voltage_1': test.voltage_1,  
                'voltage_2': test.voltage_2,  
                'voltage_3': test.voltage_3,  
                'voltage_4': test.voltage_4,  
                'voltage_5': test.voltage_5,  
                'voltage_6': test.voltage_6,  
                'voltage_7': test.voltage_7, 
                'voltage_8': test.voltage_8, 
                'electric_current': test.electric_current, 
                'temp': test.temp,              
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Energy_Storage_Data.objects.create(time_stamp=a.value,energy_storage_unit_name=b.value,voltage_1=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Charge_Capacity_Data接口              
class ChargeCapacityDataView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Charge_Capacity_Data.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Charge_Capacity_Data.objects.all()[pager.start: pager.end]
        else:
            test_list = Charge_Capacity_Data.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'time_stamp': test.time_stamp,
                'charge_capacity': test.charge_capacity,
                'discharge_capacity': test.discharge_capacity,            
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Charge_Capacity_Data.objects.create(time_stamp=a.value,charge_capacity=b.value,discharge_capacity=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Local_Electricity_Price接口              
class LocalElectricityPriceView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Local_Electricity_Price.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Local_Electricity_Price.objects.all()[pager.start: pager.end]
        else:
            test_list = Local_Electricity_Price.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'month': test.month,
                'province': test.province,
                'peak_price': test.peak_price,  
                'top_price': test.top_price, 
                'valle_price': test.valle_price, 
                'flat_price': test.flat_price, 
                'public_subsidies': test.public_subsidies               
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Local_Electricity_Price.objects.create(month=a.value,province=b.value,peak_price=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#External_Transaction_Data接口              
class ExternalTransactionDataView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = External_Transaction_Data.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = External_Transaction_Data.objects.all()[pager.start: pager.end]
        else:
            test_list = External_Transaction_Data.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'name': test.name,
                'unit': test.unit,
                'example': test.example,  
                'collect_form': test.collect_form, 
                'data_type': test.data_type
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    External_Transaction_Data.objects.create(name=a.value,unit=b.value,example=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#PeakVally_Benefit_Data接口              
class PeakVallyBenefitDataView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = PeakVally_Benefit_Data.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = PeakVally_Benefit_Data.objects.all()[pager.start: pager.end]
        else:
            test_list = PeakVally_Benefit_Data.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'month': test.month,
                'charge_capacity': test.charge_capacity,
                'charge_time': test.charge_time,  
                'discharge_capacity': test.discharge_capacity, 
                'discharge_time': test.discharge_time,
                'Benefit': test.Benefit,
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    PeakVally_Benefit_Data.objects.create(month=a.value,charge_capacity=b.value,charge_time=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    
#Frequency_Modulation_Benefit_Data接口              
class FrequencyModulationBenefitDataView(View):
    def get(self, request):
        res = {
            'code': 200,
            'data': [],
            'total': 0
        }
        page = request.GET.get('page')
        size = request.GET.get('size')
        search=request.GET.get('search')
        total = Frequency_Modulation_Benefit_Data.objects.count()
        pager = Pagination(
            limit=int(size),
            all_count=int(total),
            current_page=int(page)
        )
        res['total'] = total
        if search=='':
           test_list = Frequency_Modulation_Benefit_Data.objects.all()[pager.start: pager.end]
        else:
            test_list = Frequency_Modulation_Benefit_Data.objects.all().filter(id=search)[pager.start: pager.end]
        for test in test_list:
            res['data'].append({
                'month': test.month,
                'frequency_mile': test.frequency_mile,
                'frequency_day': test.frequency_day,  
                'discharge_capacity': test.frequency_coefficient, 
                'frequency_subsidies': test.frequency_subsidies,
                'frequency_benefit': test.frequency_benefit,
            })
        return JsonResponse(res)
    
    def post(self, request):
        res = {
            'code': 200,
            'data': '数据上传成功'
        }
        file=request.FILES['file']
        print(file)
        type_file = file.name.split('.')[1]
        print(type_file)
        if type_file == 'xlsx':
            read_file = xlrd.open_workbook(filename=None,file_contents=file.read())
            file_table = read_file.sheets()[0]
            print(file_table)
            file_table_rows = file_table.nrows
            print(file_table_rows)
            with transaction.atomic():
                # 读表格数据，从第二行开始，一般第一行都是说明
                for i in range(1, file_table_rows):
                    print(i)
                    a=file_table.cell(i,0)
                    print(a.value)
                    b= file_table.cell(i,1)
                    print(b.value)
                    c=file_table.cell(i,2)
                    print(c.value)
                    Frequency_Modulation_Benefit_Data.objects.create(month=a.value,frequency_mile=b.value,frequency_day=c.value)   #把这里一起改了不就可以了吗?
            return JsonResponse(res)    





       
