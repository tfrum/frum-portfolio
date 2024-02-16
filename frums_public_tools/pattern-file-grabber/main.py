# This is a hastily made open source demo of a closed source project of mine called pattern-file-grabber.

'''
   This script operates by taking a base URL, then arguments for what parts of that URL you'd like to increment.
   It's a basic string searching algorithm--nothing special. It will increment time-series data forward in time.
   This should work without much changing on most government pdf reports.

   Most government departments post on the same day each month, so that should also usually work.
   
   Ultimately, this is not meant to scrape every possible report from every possible date, but it would
   be easy enough to do that.

   At the moment it will automatically grab anything within a 12 month calendar period per each year until the 
   current year, so Putting in a February report url will grab, retroactively, January. But it will miss
   Reports that are offset sometimes.

   I also didn't fully implement error handling here.
   
   This also won't work with funky dates because of how the re library behaves. dates like 202302 won't
   be parsed properly. Solving this requires that we cut up urls into string arrays and run a check for matching patterns
   on each item to break them up.

   Other s


   * TODO
     - Finish manual pattern algorithms
     - Add in openAI API pipeline to generate potential URLs
     - Functionality to call RAGgedy-Annelyzer's PDF-to-vector database ingestor.
        - Or whatever I call the open source version of that. Seems the RAG landscape has changed
          a bit in the last six months.
     - Start making open source version of raggedy_annelyzer
     - Implement error handling
     - Implement url parser function.
     - Parse for reserved characters in urls, substitute them for themselves, then reinsert their codes on download.
     - Support for dates older than 2013 in manual mode.
     - Parse every possible day option.
'''

# Remember to make it so string months can handle january | JANUARY | jan type edge cases
# Reimplement year functionality

import re
import datetime
import calendar
import os
import requests

def run():
    # This dictionary defines possible date types and display names for those types.
    date_types = {
        1: ("month", "Month"),
        2: ("numeric_month", "Numeric Month"),
        3: ("year", "Year")
    }

    #Grab the current date to serve as an upper bound for our dynamic search.
    current_date = datetime.datetime.now()
    date_limit = (current_date.strftime('%B'), current_date.year % 100)

    # A dictionary to store out user substrings in.
    substrings_and_types = {}
 
    # We'll grab our URL here
    input_url = get_user_input(input_url, date_types, substrings_and_types)

    url_list = generate_urls(input_url, substrings_and_types, date_limit)

    for url in url_list:
        print(url)

    download_files(url_list)
    

def get_user_input(input_url, date_types, substrings_and_types):
    # Prompt for input URL
    input_url = input("\nInput a base URL below:\n")
    
    # Print possible substring pattern types
    print("\nIdentify substring patterns and their types when prompted.")
    print("Possible substring pattern types include:")
    for key, (date_type, display_name) in date_types.items():
        print(f'[{key}] {display_name}')

    while True:


        # Get substring pattern
        substring = input("\nEnter a date pattern to locate in the url (or press Enter to finish): ")
        if not substring:
            break

        choice = input("Enter the number for the pattern type: ")

        try:
            choice_index = int(choice)
            pattern_type = date_types.get(choice_index, ("", ""))[0]
            substrings_and_types[substring] = pattern_type
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            
    return input_url


def reserved_char_parser(base_url):
    # checks for and replaces reserved character string like "%20"
    print()

def url_date_cutter(base_url):
    # Called if check_substrings_in_url throws negative
    print()


def generate_urls(base_url, substrings_and_types, date_limit):
    check_substrings_in_url(base_url, substrings_and_types)    
    working_url = base_url
    url_list = []

    while True:
        # If we're counting months, we want to just do twelve iterations. Both month types
        # should increment together, since monthly reports are released, well, monthly.
        for count in range(12):
            for substring, pattern_type in substrings_and_types.items():
                # Handle our string months
                if pattern_type == "month":
                    if count == 0:
                        current_month = substring
                    working_url, current_month = increment_month(working_url, current_month)
                # Handle our numeric months, which is simpler than string months.
                if pattern_type == "numeric_month":
                    starting_num_month = substring
                    if count == 0:
                        current_num_month = substring
                    working_url, current_num_month = increment_numeric_month(working_url, current_num_month, starting_num_month)
                if pattern_type == "year" and count == 11:
                    print("")
                    #STRIPPED
            url_list.append(working_url)
            
        break
    return url_list
    



def check_substrings_in_url(base_url, substrings_and_types):
    for substring in substrings_and_types.keys():
        if substring not in base_url:
            print(f"Error: Substring '{substring}' not found in the base URL.")
            exit(0)
        else:
            print(f'{substring} found in base URL!')
    

def increment_month(working_url, current_month):
     # List of month names for conversion
    month_names = list(calendar.month_name)[1:]

    # Find the index of the current month
    current_month_index = month_names.index(current_month.capitalize())

    # Increment the month index, handle wrapping from December to January
    next_month_index = (current_month_index + 1) % 12
    next_month_str = month_names[next_month_index]

    # Replace the current month with the next month in the URL
    updated_url = re.sub(rf'{current_month}\b', next_month_str, working_url, flags=re.IGNORECASE)

    return updated_url, next_month_str

def increment_numeric_month(working_url, current_num_month, starting_num_month):
    # Increment the numeric month
    next_num_month = (int(current_num_month) % 12) + 1
    # Replace the original numeric month with the incremented one in the URL
    if starting_num_month[0] == "0" and next_num_month < 10:
        updated_url = re.sub(rf'\b{current_num_month}\b', f'0{next_num_month}', working_url)
        return updated_url, str(f'0{next_num_month}')
    else:
        updated_url = re.sub(rf'\b{current_num_month}\b', str(next_num_month), working_url)
        return updated_url, next_num_month

# def increment_year():
    # Stripped because I used local Llama 7b to handle my edge cases.


def download_files(url_list, download_folder="downloads"):
    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for url in url_list:
        try:
            # Get the file name from the URL and get the request.
            file_name = os.path.join(download_folder, os.path.basename(url))
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a file in the downloads folder
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {url}")
            else:
                print(f"Failed to download: {url}, Status Code: {response.status_code}")

        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
            continue  # Move to the next URL in case of an error


if __name__ == '__main__':
    run()
