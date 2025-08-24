import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import time
import os

# COLORES PARA TERMINAL
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def clear():
    """Limpia la pantalla del terminal"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def show_banner():
    """Muestra el banner de la herramienta"""
    clear()
    time.sleep(1)
    print(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------------
       :g g   :         {Wh}|  {Gr}PHONE   TRACKER                   {Wh}|
       : o    `.        {Wh}|  {Gr}MODIFIED BY JMEIRACORBAL          {Wh}|
      :         ``.     {Wh}|  {Gr}ORIGINAL BY HUNXBYTS              {Wh}|
     :             `.   {Wh}--------------------------------------
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)
    time.sleep(0.5)

def track_phone():

    """Find phone numbers information"""
    print(f"\n {Wh}Enter phone number information:")
    
    country_code = input(f" {Wh}Country Code {Gr}Ex [34, 1, 81] {Wh}: {Gr}")
    phone_number = input(f" {Wh}Phone Number {Gr}Ex [666666666] {Wh}: {Gr}")
    
    # country code and number
    full_number = "+" + country_code + phone_number
    
    try:
        parsed_number = phonenumbers.parse(full_number)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, region_code, with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Full Number         :{Gr} {full_number}")
        print(f" {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezoneF}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider}")
        print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
        print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
        
        national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        print(f" {Wh}National format      :{Gr} {national_format}")
        
        is_portable = phonenumbers.is_possible_number(parsed_number)
        print(f" {Wh}Portable number      :{Gr} {is_portable}")
        
        timezone_info = timezone.time_zones_for_number(parsed_number)
        if timezone_info:
            print(f" {Wh}Best calling time    :{Gr} Check local time in {', '.join(timezone_info)}")
        
        if number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
            print(f" {Wh}Cost type            :{Gr} Premium rate (expensive)")
        elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
            print(f" {Wh}Cost type            :{Gr} Toll-free (free to call)")
        else:
            print(f" {Wh}Cost type            :{Gr} Standard rate")
            
    except Exception as e:
        print(f"{Re}Error: {e}")

def main():
    while True:
        show_banner()
        print(f"\n{Wh}[ {Gr}1 {Wh}] {Gr}Track a phone number")
        print(f"{Wh}[ {Gr}0 {Wh}] {Gr}Exit")
        
        try:
            choice = input(f"\n{Wh}[ + ] {Gr}Select Option : {Wh}")
            
            if choice == "1":
                track_phone()
                input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to check another number')
            elif choice == "0":
                print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
                time.sleep(2)
                break
            else:
                print(f'\n{Wh}[ {Re}! {Wh}] {Re}Invalid option')
                time.sleep(2)
                
        except KeyboardInterrupt:
            print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
            time.sleep(2)
            break
        except ValueError:
            print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
            time.sleep(2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
