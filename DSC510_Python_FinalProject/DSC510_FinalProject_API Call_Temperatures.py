# DSC 510
# Week 12
# Programming Assignment 12.1 Final Project
# Author: Madhuri Basava
# 11/17/2022

import requests
import re

'''This project is used to get the weather data based on either city/state or
zipcode from two APIs(GEO API and Weather API)'''

'''printing weather information in a proper format'''


def pretty_print(temp_scale, data):
    print("\nCurrent weather conditions for " + data["name"])
    print("-" * 45)
    # print(data)

    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]

    # default temperatures to Fahrenheit
    print(
        "Current Temperature: {:15}{: <2}".format(temp, '\u00b0' + temp_scale))
    print("Minimum Temperature: {:15}{: <2}".format(temp_min,
                                                    '\u00b0' + temp_scale))
    print("Maximum Temperature: {:15}{: <2}".format(temp_max,
                                                    '\u00b0' + temp_scale))

    print("{} {:25}{: <2}".format("Pressure:", pressure, 'hPa'))
    print("{} {:27}{: <2}".format("Humidity:", humidity, '%'))
    print("{:28} {} ".format("Description:", data["weather"][0][
        "description"]))
    print("{:35}{: <15}".format("Clouds icon:", data["weather"][0][
        "icon"]))
    print("-" * 45)


'''Weather lookup based on latitude and longitude'''


def lookup_weather(lat, lon, apikey):
    temp_scale = 'F'
    units = "&units=imperial"
    while True:
        temp_scale = input("Please enter either 'K' for kelvin or "
                           "'F' for fahrenheit or 'C' for celsius or any "
                           "other character to exit: ")
        if len(temp_scale) > 0:
            temp_scale = temp_scale.upper()
        else:
            continue

        if temp_scale == 'F':
            units = "&units=imperial"
        elif temp_scale == 'C':
            units = "&units=metric"
        elif temp_scale == 'K':
            units = ""
        else:
            break

        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            query_string = "lat=" + str(lat) + "&lon=" + str(lon) + \
                           "&appid=" + apikey + units
            headers = {'cache-control': 'no-cache'}
            response = requests.request("GET", url, headers=headers,
                                        params=query_string)
            print("API call in lookup_weather() : " + url + "?" + query_string)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            print("Http Error:", http_error)
        except requests.exceptions.ConnectionError as connection_error:
            print("Error Connecting:", connection_error)
            print("Please check if the internet is up and running")
        except requests.exceptions.Timeout as timeout_error:
            print("Timeout Error:", timeout_error)
        except requests.exceptions.RequestException as request_error:
            print("OOps: Something Else", request_error)
        else:
            print("Weather lookup API connection is successful")
            data = response.json()
            # print("after try in lookup_weather() function", data)
            pretty_print(temp_scale, data)  # default to Fahrenheit


'''creating API request to get the latitude and longitude data from either
city/state or zipcode'''


def geocode_lookup(url, headers, q, apikey, lookup_flag):
    try:
        # submit data to the url to get the response back
        if lookup_flag == 'city':
            # query_param = 'q'
            query_string = "q=" + q + "&appid=" + apikey
        elif lookup_flag == 'zip_code':
            # query_param = 'zip'
            query_string = "zip=" + q + "&appid=" + apikey
        else:
            print("Query string is incorrect")

        response = requests.request("GET", url, headers=headers,
                                    params=query_string)
        print("API call in geocode_lookup() : " + url + "?" + query_string)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        print("Http Error:", http_error)
    except requests.exceptions.ConnectionError as connection_error:
        print("Error Connecting:", connection_error)
        print("Please check if the internet is up and running")
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error:", timeout_error)
    except requests.exceptions.RequestException as request_error:
        print("OOps: Something Else", request_error)
    else:
        data = response.json()
        lat = 0
        lon = 0
        # print(data, "in getAPIResponse()")
        if lookup_flag == 'city':
            if len(data) == 0:
                print("User entered incorrect data")
            else:
                print("Geo lookup for city API connection is successful")
                for item in data:
                    lat = item["lat"]
                    lon = item["lon"]
                    lookup_weather(lat, lon, apikey)  # calling weather API
                    # with latitude and longitude
        elif lookup_flag == 'zip_code':
            print("Geo lookup for zipcode API connection is successful")
            lat = data["lat"]
            lon = data["lon"]
            lookup_weather(lat, lon, apikey)  # calling weather API with
            # latitude and longitude


'''get city and state code from user and create an API request to get the
latitude and longitude'''


def city_lookup():
    while True:
        city_name = input("Please enter the city name: ")
        state_code = input("Please enter the state code: ")
        if len(state_code) == 0:
            print("State code is mandatory")
            continue
        else:
            break
    country_code = "US"
    apikey = "c428923ef5f286f96f45b1b8bd5d9348"

    # url = "https://api.openweathermap.org/data/2.5/weather"
    url = "http://api.openweathermap.org/geo/1.0/direct"
    q = city_name + "," + state_code + "," + country_code
    headers = {'cache-control': 'no-cache'}
    lookup_flag = 'city'
    geocode_lookup(url, headers, q, apikey, lookup_flag)


''' get zip code from user and create an API request to get the latitude 
and longitude'''


def zipcode_lookup():
    result = False
    while True:
        zip_code = input("Please enter the Zipcode: ")
        pattern = "^[0-9]{5}(?:-[0-9]{4})?$"
        result = re.match(pattern, zip_code)
        if result:
            break
        else:
            print("zip code is not correct")
            continue

    country_code = "US"
    apikey = "c428923ef5f286f96f45b1b8bd5d9348"

    url = "http://api.openweathermap.org/geo/1.0/zip"
    q = zip_code + "," + country_code
    # print("q is " + q)
    headers = {'cache-control': 'no-cache'}
    lookup_flag = 'zip_code'
    geocode_lookup(url, headers, q, apikey, lookup_flag)


''' main function for calling either city lookup to zipcode lookup'''


def main():
    print("Welcome Michael Eller!")
    while True:
        lookup = input(
            "Please enter either 'city' or 'zipcode' or 'x' for exit? ")
        if lookup.lower() == 'city':
            city_lookup()
        elif lookup.lower() == 'zipcode':
            zipcode_lookup()
        elif lookup.lower() == 'x':
            break
        else:
            continue


''' calling main() function  '''
if __name__ == "__main__":
    main()
