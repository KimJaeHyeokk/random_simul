from django.contrib import admin

# Register your models here.
from .models import *

# 바이너리
@admin.register(BinaryDefinition)
class BinaryDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('id', 'name', 'created_at',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 10

# 아날로그
@admin.register(AnalogDefinition)
class AnalogDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('id', 'name', 'created_at',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 10

# 모두버스 A
@admin.register(ModbusProtocolSideApoint)
class ModbusProtocolSideApointAdmin(admin.ModelAdmin):
    list_display = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_filter = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak',)
    list_display_links = ('id',)
    search_fields = ('power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_per_page = 10    

# 모두버스 B
@admin.register(ModbusProtocolSideBpoint)
class ModbusProtocolSideBpointAdmin(admin.ModelAdmin):
    list_display = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_filter = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak',)
    list_display_links = ('id',)
    search_fields = ('power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_per_page = 10      

# 모두버스 C
@admin.register(ModbusProtocolSideCpoint)
class ModbusProtocolSideCpointAdmin(admin.ModelAdmin):
    list_display = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_filter = ('id', 'power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak',)
    list_display_links = ('id',)
    search_fields = ('power_factor', 'dc_power', 'day_peak', 'month_peak', 'total_peak')
    list_per_page = 10              

# 바이너리 수집 데이터
@admin.register(Dnp3RandomBin)
class Dnp3RandomBinAdmin(admin.ModelAdmin):
    list_display = ('id', 'division', 'value', 'created_at')
    list_filter = ('id', 'division', 'created_at',)
    list_display_links = ('id', 'division')
    search_fields = ('division',)
    list_per_page = 10

# 아날로그 수집 데이터
@admin.register(Dnp3RandomAnalog)
class Dnp3RandomAnalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'division', 'value', 'created_at')
    list_filter = ('id', 'division', 'created_at',)
    list_display_links = ('id', 'division')
    search_fields = ('division',)
    list_per_page = 10

# 환경데이터
@admin.register(EnvironmentalData)
class EnvironmentalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'dust_10', 'wind_speed', 'air_tem', 'air_press', 'dust_2', 'wind_dir', 'air_hum', 'rainfall')
    list_filter = ('id', 'dust_10', 'wind_speed', 'air_tem', 'air_press', 'dust_2', 'wind_dir', 'air_hum', 'rainfall',)
    list_display_links = ('id',)
    search_fields = ('dust_10', 'wind_speed', 'air_tem', 'air_press', 'dust_2', 'wind_dir', 'air_hum', 'rainfall')
    list_per_page = 10    


@admin.register(ThermalImageDataAlpha)
class ThermalImageDataAlphaAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_temp', 'min_temp', 'aver_temp', 'temp_dif')
    list_filter = ('id', 'max_temp', 'min_temp', 'aver_temp', 'temp_dif')
    list_display_links = ('id',)
    search_fields = ('max_temp', 'min_temp', 'aver_temp', 'temp_dif')
    list_per_page = 10    

@admin.register(ThermalImageDataBeta)
class ThermalImageDataBetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_temp', 'aver_temp', 'temp_dif')
    list_filter = ('id', 'max_temp',  'aver_temp', 'temp_dif')
    list_display_links = ('id',)
    search_fields = ('max_temp', 'aver_temp', 'temp_dif')
    list_per_page = 10  

@admin.register(ThermalImageDataGamma)
class ThermalImageDataGammaAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_temp', 'aver_temp', 'temp_dif')
    list_filter = ('id', 'max_temp', 'aver_temp', 'temp_dif')
    list_display_links = ('id',)
    search_fields = ('max_temp', 'aver_temp', 'temp_dif')
    list_per_page = 10  

@admin.register(ThermalImageDataDelta)
class ThermalImageDataDeltaAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_temp', 'aver_temp', 'temp_dif')
    list_filter = ('id', 'max_temp', 'aver_temp', 'temp_dif')
    list_display_links = ('id',)
    search_fields = ('max_temp', 'aver_temp', 'temp_dif')
    list_per_page = 10  