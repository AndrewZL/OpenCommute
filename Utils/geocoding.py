from geopy.geocoders import OpenMapQuest
import csv

key = '%apikey%'

geo_locator = OpenMapQuest(key)


def reverse_geocode(data, output_path='geocoded.csv'):
    """
    Get address from coordinates
    TODO: Convert csv I/O to pandas
    :param data: coordinate data from Toronto KSI
    :return:
    """
    d_out = []
    with open('KSI_CLEAN2.csv', mode='r') as fin:
        reader = csv.reader(fin)
        j = 0
        for row in reader:
            j += 1
            try:
                coordinates = [row[4], row[5]]
                result = geolocator.reverse(coordinates).address
                row.extend(result)
                d_out.append(row)
            except:
                print('Error')

    with open(output_path, 'w') as f_out:
        writer = csv.writer(f_out)
        writer.writerows(d_out)

