from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = "Creates initial train data"

    def handle(self, *args, **options):
        MyTrainModel = apps.get_model("myapp", "Train")
        if not MyTrainModel.objects.exists():
            pre_train_data = [
                {
                    "train_number": "1010",
                    "train_name": "TRAIN 1",
                    "from_station_code": "ST1",
                    "to_station_code": "ST20",
                    "total_seats_1ac": 40,
                    "total_seats_2ac": 50,
                    "total_seats_3ac": 60,
                    "fare_1ac": 150,
                    "fare_2ac": 120,
                    "fare_3ac": 80,
                    "train_available": True,
                    "runs_on": "M,W,F",
                },
                {
                    "train_number": "1020",
                    "train_name": "TRAIN 2",
                    "from_station_code": "ST3",
                    "to_station_code": "ST15",
                    "total_seats_1ac": 35,
                    "total_seats_2ac": 45,
                    "total_seats_3ac": 55,
                    "fare_1ac": 330,
                    "fare_2ac": 210,
                    "fare_3ac": 170,
                    "train_available": True,
                    "runs_on": "T,Th,Sa",
                },
                {
                    "train_number": "1030",
                    "train_name": "TRAIN 3",
                    "from_station_code": "ST5",
                    "to_station_code": "ST17",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 300,
                    "fare_2ac": 190,
                    "fare_3ac": 100,
                    "train_available": True,
                    "runs_on": "Su",
                },
                {
                    "train_number": "1040",
                    "train_name": "TRAIN 4",
                    "from_station_code": "ST8",
                    "to_station_code": "ST12",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 350,
                    "fare_2ac": 290,
                    "fare_3ac": 160,
                    "train_available": True,
                    "runs_on": "W,Th,Sa",
                },
                {
                    "train_number": "1050",
                    "train_name": "TRAIN 5",
                    "from_station_code": "ST9",
                    "to_station_code": "ST20",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 300,
                    "fare_2ac": 190,
                    "fare_3ac": 100,
                    "train_available": True,
                    "runs_on": "Su",
                },
                {
                    "train_number": "1060",
                    "train_name": "TRAIN 6",
                    "from_station_code": "ST13",
                    "to_station_code": "ST19",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 300,
                    "fare_2ac": 190,
                    "fare_3ac": 120,
                    "train_available": True,
                    "runs_on": "T,Th,Su",
                },
                {
                    "train_number": "1009",
                    "train_name": "TRAIN 1R",
                    "from_station_code": "ST5",
                    "to_station_code": "ST17",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 460,
                    "fare_2ac": 390,
                    "fare_3ac": 160,
                    "train_available": True,
                    "runs_on": "Su",
                },
                {
                    "train_number": "1019",
                    "train_name": "TRAIN 2R",
                    "from_station_code": "ST15",
                    "to_station_code": "ST3",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 100,
                    "fare_2ac": 90,
                    "fare_3ac": 60,
                    "train_available": True,
                    "runs_on": "M,Th,Sa",
                },
                {
                    "train_number": "1029",
                    "train_name": "TRAIN 3R",
                    "from_station_code": "ST17",
                    "to_station_code": "ST5",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 400,
                    "fare_2ac": 290,
                    "fare_3ac": 150,
                    "train_available": True,
                    "runs_on": "T,F,Su",
                },
                {
                    "train_number": "1039",
                    "train_name": "TRAIN 4R",
                    "from_station_code": "ST12",
                    "to_station_code": "ST8",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 500,
                    "fare_2ac": 390,
                    "fare_3ac": 260,
                    "train_available": True,
                    "runs_on": "M,W,F,Sa",
                },
                {
                    "train_number": "1049",
                    "train_name": "TRAIN 5R",
                    "from_station_code": "ST20",
                    "to_station_code": "ST9",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 500,
                    "fare_2ac": 290,
                    "fare_3ac": 160,
                    "train_available": True,
                    "runs_on": "T,Th,Su",
                },
                {
                    "train_number": "1059",
                    "train_name": "TRAIN 6R",
                    "from_station_code": "ST19",
                    "to_station_code": "ST13",
                    "total_seats_1ac": 20,
                    "total_seats_2ac": 25,
                    "total_seats_3ac": 30,
                    "fare_1ac": 390,
                    "fare_2ac": 190,
                    "fare_3ac": 160,
                    "train_available": True,
                    "runs_on": "M,W,F",
                },
            ]

            for data in pre_train_data:
                instance = MyTrainModel.objects.create(**data)
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created train: {instance}")
                )
            self.stdout.write(
                self.style.SUCCESS("Initial train data creation complete")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("Train data already exists. Skipping creation.")
            )
