from django.shortcuts import render
from django.views import View
from django.db import connection
from datetime import datetime
from django.http import JsonResponse
import random
import time
from threading import Thread
from django.conf import settings
# Create your views here.

class MainView(View):
    def get(self, request):
        html = 'dashboard.html'
        query = "SELECT b.name AS name, a.value AS val, a.created_at AS create_at FROM tb_dnp3_random_bin a JOIN tb_bin_def b ON a.division_id = b.id"
        result = DataQuery().selectQuery(query)
        # print(type(send_data))
        
        for val in result:
            val['create_at'] = val['create_at'].strftime('%Y-%m-%d %H:%M:%S')
        
        print(result)        
        context = {"result": result}
        # GetDataClass().runningThread()
        return render(request, html, context)

    def post(self, request):
        if request.POST['btn'] == "on":
            settings.FLAG = True
            GetDataClass().runningThread()
        elif request.POST['btn'] == "off":
            settings.FLAG = False
        
        a = 1000
        context = {"a" : a}

        return JsonResponse(context, safe=False)


    
# db insertquery
class InsertQuery():
    def insertAlpha(self):
        with connection.cursor() as cursor:
            max_temp = random.random()
            min_temp = random.random()
            aver_temp = random.random()
            temp_dif = random.random()
            query="INSERT INTO tb_tid_alpha (max_temp, min_temp, aver_temp, temp_dif) values (%s, %s, %s, %s)"
            values = (max_temp,min_temp,aver_temp,temp_dif)    
            cursor.execute(query, values)

    def insertBeta(self):
        with connection.cursor() as cursor:
            max_temp = random.random()
            aver_temp = random.random()
            temp_dif = random.random()
            query="INSERT INTO tb_tid_beta (max_temp, aver_temp, temp_dif) values (%s, %s, %s)"
            values = (max_temp, aver_temp,temp_dif)    
            cursor.execute(query, values)

    def insertGamma(self):
        with connection.cursor() as cursor:
            max_temp = random.random()
            aver_temp = random.random()
            temp_dif = random.random()
            query="INSERT INTO tb_tid_gamma (max_temp, aver_temp, temp_dif) values (%s, %s, %s)"
            values = (max_temp, aver_temp,temp_dif)    
            cursor.execute(query, values)

    def insertDelta(self):
        with connection.cursor() as cursor:
            max_temp = random.random()
            aver_temp = random.random()
            temp_dif = random.random()
            query="INSERT INTO tb_tid_delta (max_temp, aver_temp, temp_dif) values (%s, %s, %s)"
            values = (max_temp, aver_temp,temp_dif)    
            cursor.execute(query, values)                

# Thread 작동
class GetDataClass():
    def runningThread(self):
        if settings.IS_RUNNING_THREAD is None:
            try:
                IS_RUNNING_THREAD = Thread(target=self.get_data_thread_function, args=())
                IS_RUNNING_THREAD.daemon = True
                IS_RUNNING_THREAD.start()
            except Exception as e:
                print('예외가 발생했습니다.', e)
        else:
            return False    
        
        
    def get_data_thread_function(self):
            while settings.FLAG:
                InsertQuery().insertAlpha()
                InsertQuery().insertBeta()
                InsertQuery().insertGamma()
                InsertQuery().insertDelta()
                time.sleep(1)

# query setting
class DataQuery():
    def selectQuery(self, query, distinct=None):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]

                queryset = []
                temp = None
                for row in cursor.fetchall():
                    if distinct != None:  # 중복제거
                        if temp != row[distinct]:
                            queryset.append(dict(zip(columns, row)))
                            temp = row[distinct]
                    else:
                        queryset.append(dict(zip(columns, row)))
                return queryset
        except:
            print('DB Connection Error!')
