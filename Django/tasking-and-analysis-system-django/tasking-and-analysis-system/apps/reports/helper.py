import datetime
from apps.constants import General, ReportsFields
from django.contrib import messages
from django.shortcuts import render


def get_selected_date_list(farm, start_date, end_date):
    """
     This function returns list from range of selected start and end dates.
     :param farm:selected upload object
     :param start_date:DateField
     :param end_date:DateField
     return list of selected dates
     """
    delta = datetime.timedelta(days=1)
    current_date = start_date
    selected_date_list = []
    while current_date <= end_date:
        key_in_dictionary = current_date.strftime(General.DATE_FORMAT)
        if key_in_dictionary in farm.data.keys():
            selected_date_list.append(key_in_dictionary)
        current_date += delta
    return selected_date_list


def __get_average(farm, selected_date_list):
    """
    This function returns average of selected farm's data
     in range of selected days.
    :param farm: Upload model instance
    :param selected_date_list:list
    :return average of selected farm's data:
    """

    overall_result = 0
    for date in selected_date_list:
        overall_result += farm.data[date]
    return format(overall_result / len(selected_date_list), ".2f")


# TODO rename to show meaning of it
def get_report_data(farm, selected_date_list):
    """
    This function returns whole data including header columns names
    for writing in report xlsx file with the following columns:
    - columns:Id, farm name, dates from date_list, average of selected farm's data in range of selected days
    - ReportsFields.FARM_NAME
    -selected_date_list
    -ReportsFields.AVERAGE
    :param farm:
    :param selected_date_list:
    :return list of gotten data:
    """
    return [
               # columns' names
               [General.ID.capitalize(), ReportsFields.FARM_NAME]
               + selected_date_list
               + [ReportsFields.AVERAGE]
           ] + \
           [
               # existing data from DB
               [farm.id, farm.farm]
               + [farm.data[day] for day in selected_date_list]
               + [__get_average(farm, selected_date_list)]
           ]
