# signals.py
from django.db.models.signals import post_migrate
from django.apps import apps
from .models import Train




def create_initial_trains(sender, **kwargs):
    MyTrainModel = apps.get_model('myapp', 'Train')
    if sender.name == 'myapp':
        if not MyTrainModel.objects.exists():
            pre_train_data=[
                    MyTrainModel.objects.create(train_number='101', train_name='Speedy Express', from_station_code='NDLS', to_station_code='BOM', total_seats_1ac=40, total_seats_2ac=50, total_seats_3ac=60, fare_1ac=150, fare_2ac=120, fare_3ac=80, train_available=True, runs_on='M,W,F'),
                    MyTrainModel.objects.create(train_number='202', train_name='Comfort Cruiser', from_station_code='BOM', to_station_code='DEL', total_seats_1ac=35, total_seats_2ac=45, total_seats_3ac=55, fare_1ac=130, fare_2ac=110, fare_3ac=70, train_available=True, runs_on='T,Th,Sa'),
                    MyTrainModel.objects.create(train_number='303', train_name='Local Sprinter', from_station_code='KOL', to_station_code='HYD', total_seats_1ac=20, total_seats_2ac=25, total_seats_3ac=30, fare_1ac=100, fare_2ac=90, fare_3ac=60, train_available=True, runs_on='Su'),
                    MyTrainModel.objects.create(train_number='404', train_name='Express Voyager', from_station_code='DEL', to_station_code='MUM', total_seats_1ac=42, total_seats_2ac=52, total_seats_3ac=62, fare_1ac=160, fare_2ac=130, fare_3ac=85, train_available=True, runs_on='W,Th,Sa'),
                    MyTrainModel.objects.create(train_number='505', train_name='City Connect', from_station_code='BAN', to_station_code='CHN', total_seats_1ac=38, total_seats_2ac=48, total_seats_3ac=58, fare_1ac=145, fare_2ac=115, fare_3ac=75, train_available=True, runs_on='M,W,F'),
                    MyTrainModel.objects.create(train_number='606', train_name='Rapid Transit', from_station_code='HYD', to_station_code='PUN', total_seats_1ac=30, total_seats_2ac=40, total_seats_3ac=50, fare_1ac=120, fare_2ac=100, fare_3ac=65, train_available=True, runs_on='T,Th,Su'),
                    MyTrainModel.objects.create(train_number='707', train_name='Express Liner', from_station_code='MUM', to_station_code='KOL', total_seats_1ac=45, total_seats_2ac=55, total_seats_3ac=65, fare_1ac=170, fare_2ac=140, fare_3ac=90, train_available=True, runs_on='W,F,Su'),
                    MyTrainModel.objects.create(train_number='808', train_name='Metro Sprint', from_station_code='DEL', to_station_code='BAN', total_seats_1ac=33, total_seats_2ac=43, total_seats_3ac=53, fare_1ac=140, fare_2ac=110, fare_3ac=72, train_available=True, runs_on='M,Th,Sa'),
                    MyTrainModel.objects.create(train_number='909', train_name='Coastal Express', from_station_code='CHN', to_station_code='HYD', total_seats_1ac=25, total_seats_2ac=35, total_seats_3ac=45, fare_1ac=110, fare_2ac=95, fare_3ac=62, train_available=True, runs_on='T,F,Su'),
                    MyTrainModel.objects.create(train_number='111', train_name='Highland Voyager', from_station_code='PUN', to_station_code='DEL', total_seats_1ac=37, total_seats_2ac=47, total_seats_3ac=57, fare_1ac=155, fare_2ac=125, fare_3ac=82, train_available=True, runs_on='M,W,F,Sa'),
                    MyTrainModel.objects.create(train_number='222', train_name='Sunrise Express', from_station_code='KOL', to_station_code='MUM', total_seats_1ac=28, total_seats_2ac=38, total_seats_3ac=48, fare_1ac=125, fare_2ac=105, fare_3ac=68, train_available=True, runs_on='T,Th,Su'),
                    MyTrainModel.objects.create(train_number='333', train_name='Valley Voyager', from_station_code='BAN', to_station_code='CHN', total_seats_1ac=41, total_seats_2ac=51, total_seats_3ac=61, fare_1ac=165, fare_2ac=135, fare_3ac=88, train_available=True, runs_on='M,W,F')
]
            for data in pre_train_data:
                instance = MyTrainModel(**data)
                instance.save()
    
post_migrate.connect(create_initial_trains, sender=apps.get_app_config('myapp'))
