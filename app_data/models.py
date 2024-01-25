from django.db import models
from django.utils.timezone import now

# Create your models here.
# 바이너리 데이터 정의
class BinaryDefinition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    
    class Meta:
        db_table = 'tb_bin_def'
        verbose_name_plural = '바이너리 데이터 정의'
    
    def __str__(self):
        return self.name

# 아날로그 데이터 정의
class AnalogDefinition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    
    class Meta:
        db_table = 'tb_analog_def'
        verbose_name_plural = '아날로그 데이터 정의'
    
    def __str__(self):
        return self.name

# 모두버스 프로토컬 A포인트 정의
class ModbusProtocolSideApoint(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100, null=False, blank=False)
    power_factor = models.FloatField(null=True, blank=False)
    dc_power = models.FloatField(null=True, blank=False)
    day_peak = models.FloatField(null=True, blank=False)
    month_peak = models.FloatField(null=True, blank=False)
    total_peak = models.FloatField(null=True, blank=False)
    # description = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tb_modbus_A'
        verbose_name_plural = 'Modbus 프로토컬 사이드 A포인트'

    def __str__(self):
        return self.name

# 모두버스 프로토컬 B포인트 정의
class ModbusProtocolSideBpoint(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100, null=False, blank=False)
    # description = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(default=now)
    power_factor = models.FloatField(null=True, blank=False)
    dc_power = models.FloatField(null=True, blank=False)
    day_peak = models.FloatField(null=True, blank=False)
    month_peak = models.FloatField(null=True, blank=False)
    total_peak = models.FloatField(null=True, blank=False)

    class Meta:
        db_table = 'tb_modbus_B'
        verbose_name_plural = 'Modbus 프로토컬 사이드 B포인트'

    def __str__(self):
        return self.name
        
# 모두버스 프로토컬 C포인트 정의
class ModbusProtocolSideCpoint(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100, null=False, blank=False)
    # description = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(default=now)
    power_factor = models.FloatField(null=True, blank=False)
    dc_power = models.FloatField(null=True, blank=False)
    day_peak = models.FloatField(null=True, blank=False)
    month_peak = models.FloatField(null=True, blank=False)
    total_peak = models.FloatField(null=True, blank=False)

    class Meta:
        db_table = 'tb_modbus_C'
        verbose_name_plural = 'Modbus 프로토컬 사이드 C포인트'

    def __str__(self):
        return self.name


        
# DNP3 수집 데이터 바이너리(랜덤생성 데이터)
class Dnp3RandomBin(models.Model):
    id = models.AutoField(primary_key=True)
    division = models.ForeignKey(BinaryDefinition, on_delete=models.CASCADE, null=False, blank=False)
    value = models.BooleanField(null=False, blank=False)
    created_at = models.DateTimeField(default=now)
    # datetime_id = models.IntegerField(null = False, blank=False)
    
    class Meta:
        db_table = 'tb_dnp3_random_bin'
        verbose_name_plural = 'DNP3 수집 데이터 바이너리'
    
    def __str__(self):
        return self.division.name

# DNP3 수집 데이터 아날로그(랜덤생성 데이터)
class Dnp3RandomAnalog(models.Model):
    id = models.AutoField(primary_key=True)
    division = models.ForeignKey(AnalogDefinition, on_delete=models.CASCADE, null=False, blank=False)
    value = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(default=now)
    # datetime_id = models.integerField(null = False, blank=False)
    
    class Meta:
        db_table = 'tb_dnp3_random_analog'
        verbose_name_plural = 'DNP3 수집 데이터 아날로그'
    
    def __str__(self):
        return self.division.name

#####OneM2M Protocol Side#######
# 환경데이터
class EnvironmentalData(models.Model):
    id = models.AutoField(primary_key=True)
    dust_10 = models.FloatField(null =True, blank=False)
    wind_speed = models.FloatField(null =True, blank=False)
    air_tem = models.FloatField(null =True, blank=False)
    air_press= models.FloatField(null=True,blank=False)
    dust_2 = models.FloatField(null =True, blank=False)
    wind_dir = models.FloatField(null =True, blank=False)
    air_hum = models.FloatField(null=True,blank=False)
    rainfall = models.FloatField(null=True,blank=False)

    class Meta:
        db_table = 'tb_environment'
        verbose_name_plural = '환경데이터'

    def __str__(self):
        return self.name    


class ThermalImageDataAlpha(models.Model):
    id = models.AutoField(primary_key=True)
    max_temp = models.FloatField(null=True,blank=False)
    min_temp = models.FloatField(null=True,blank=False)
    aver_temp = models.FloatField(null=True,blank=False)
    temp_dif = models.FloatField(null=True,blank=False)

    class Meta:
        db_table = 'tb_tid_alpha'
        verbose_name_plural = '열화상데이터 알파 point'

    def __str__(self):
        return self.name

class ThermalImageDataBeta(models.Model):
    id = models.AutoField(primary_key=True)
    max_temp = models.FloatField(null=True,blank=False)
    aver_temp = models.FloatField(null=True,blank=False)
    temp_dif = models.FloatField(null=True,blank=False)

    class Meta:
        db_table = 'tb_tid_beta'
        verbose_name_plural = '열화상데이터 베타 point'

    def __str__(self):
        return self.name

class ThermalImageDataGamma(models.Model):
    id = models.AutoField(primary_key=True)
    max_temp = models.FloatField(null=True,blank=False)
    aver_temp = models.FloatField(null=True,blank=False)
    temp_dif = models.FloatField(null=True,blank=False)

    class Meta:
        db_table = 'tb_tid_gamma'
        verbose_name_plural = '열화상데이터 감마 point'

    def __str__(self):
        return self.name

class ThermalImageDataDelta(models.Model):
    id = models.AutoField(primary_key=True)
    max_temp = models.FloatField(null=True,blank=False)
    aver_temp = models.FloatField(null=True,blank=False)
    temp_dif = models.FloatField(null=True,blank=False)

    class Meta:
        db_table = 'tb_tid_delta'
        verbose_name_plural = '열화상데이터 델타 point'

    def __str__(self):
        return self.name
