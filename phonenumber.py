import phonenumbers

from phonenumbers import timezone, geocoder, carrier

number=input("Enter your Phone Number with +__ : ")
phone=phonenumbers.parse(number)
time=phonenumbers.timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=phonenumbers.geocoder.description_for_number(phone,"en")
city_info = phonenumbers.geocoder.description_for_number(phone, "en", script="Latn")
city_info = city_info if city_info != reg else None


print("Phone Number:" , phone)

print("Carrier Name:", car)

print("Time Zones:",time)

print("region:",reg)

if city_info:
    print("City:", city_info)







