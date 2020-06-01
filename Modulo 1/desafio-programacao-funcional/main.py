# Bibliotecas
from datetime import datetime
from operator import itemgetter

# Constantes
TARIFF_FIXED = 0.36
MINUTO = 60
TARIFF_DAY = 0.09
DAY = datetime.strptime('06:00:00', '%H:%M:%S').time()
NIGHT = datetime.strptime('22:00:00', '%H:%M:%S').time()

# Base de Dados
records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]

# Function


def calculate_minute_time(records):
    #this function calculates how many minutes each call takes.
    """Takes the values of the "end" and "start" keys for each dictionary 
    contained in the list. 
    Then, calculate difference between them and convert to minutes"""
    minute_time_list = []
    for record in records:
        minute_time = 0
        call_start = datetime.fromtimestamp(record['start'])
        call_end = datetime.fromtimestamp(record['end'])
        if DAY <= call_start.time() <= NIGHT:
            if call_end.time() > NIGHT:
                call_end = datetime.fromtimestamp(record['end']).time()
                time = (NIGHT - call_end).seconds
            else:
                time = record['end'] - record['start']

            minute_time = (time % 3600) // 60
        minute_time_list.append(minute_time)

    return minute_time_list


def calculate_tariff_value(time_list):
    #This function calculates the fare value of each source per minute
    list_tariff_value = []
    for time in time_list:
        value = (time * TARIFF_DAY) + TARIFF_FIXED
        list_tariff_value.append(value)

    return list_tariff_value


def record_tariff(records, list_tariff_value):
    """This function creates a new list with dictionaries 
    for each link for each customer"""

    records_tariff = []

    i = 0
    for record in records:
        client = {}
        client['source'] = record['source']
        client['total'] = list_tariff_value[i]
        records_tariff.append(client)
        i += 1

    return records_tariff


def agroup_order(new_records):
    """This function groups the dictionary by source, 
    updating the total and sorting by total"""
    dic_group_by_client = {}
    agrouped_ordered = []
    for record in new_records:
        if record['source'] in dic_group_by_client:
            dic_group_by_client[record['source']] += record['total']
        else:
            dic_group_by_client[record['source']] = record['total']

    for key, value in dic_group_by_client.items():
        agrouped_ordered.append({'source': key, 'total': round(value, 2)})

    agrouped_ordered = sorted(agrouped_ordered, key=itemgetter('total'), reverse=True)

    return agrouped_ordered


def classify_by_phone_number(records):
    """This function is main function that returns a 
    desired dictionary list for solving the challenge"""
    time = calculate_minute_time(records)
    tariff = calculate_tariff_value(time)
    dic_record_tariff = record_tariff(records, tariff)
    result = agroup_order(dic_record_tariff)

    return result

print(classify_by_phone_number(records))