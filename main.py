import pandas as pd
import datetime
from colorama import init, Back, Fore
import warnings
from random import choice

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None
init()

def graffiti():
    text = [' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '\n', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', '\n', ' ', ' ', '/', ':', ':', '\\', '~', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', '\n', ' ', '/', ':', '/', '\\', ':', '\\', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', '/', ':', '/', '_', '_', '/', ' ', ' ', '/', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', '_', '_', '\\', ' ', '/', ':', '/', '_', '_', '/', ' ', '\\', ':', '\\', '_', '_', '\\', '\n', ' ', '\\', '/', '_', '_', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '\\', '/', '_', '_', '/', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', '/', ':', '/', ' ', ' ', '/', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '\n', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', '\n', ' ', ' ', '/', ':', ':', '\\', '~', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '/', ':', ':', '\\', '~', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '_', '\\', ':', '\\', '~', '\\', ' ', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', '\n', ' ', '/', ':', '/', '\\', ':', '\\', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', '/', ':', '/', '\\', ':', '\\', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', '/', '\\', ' ', '\\', ':', '\\', ' ', '\\', ' ', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', '_', '_', '\\', '\n', ' ', '\\', '/', '_', '_', '\\', ':', '\\', ' ', '\\', '/', '_', '_', '/', ' ', '\\', '/', '_', '_', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', '\\', ':', '\\', ' ', '\\', ':', '\\', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '\\', '/', '_', '_', '/', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', '\\', ':', '\\', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '\n', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', '\n', ' ', ' ', ' ', '\\', ':', '\\', '~', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', '\n', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', '/', ':', '/', '_', '_', '/', ' ', '\\', ':', '\\', '_', '_', '\\', '\n', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '/', ':', '/', ' ', ' ', '/', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', '\\', '/', '_', '_', '/', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', ' ', ' ', '\\', ' ', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '/', ':', '/', ' ', ' ', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', ':', '\\', '_', '_', '\\', ' ', ' ', ' ', ' ', '\n', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\\', '/', '_', '_', '/', ' ', ' ', ' ', ' ', '\n']
    list_string = list(text)
    Forecolors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.BLACK, Fore.MAGENTA, Fore.WHITE,
                  Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLACK_EX, Fore.LIGHTGREEN_EX,
                  Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX]

    for i in list_string:
        print(choice(Forecolors), i, end="", sep="")
    print(Fore.RESET)

graffiti()

print(f"{Fore.GREEN}>>Welcome to IK Cohort Auto QC.\n",
      "This software should be used to check cohorts automatically\n",
      "Designed and developed: Nabil Hassan\n\n", Fore.WHITE,
      "_" * 80
      )

try:
    print(Fore.CYAN)
    prim = str(input(f"Please drag and drop source CSV file and press enter: ")).strip('"')
    sec = str(input(f"Please drag and drop the Uplevel GC Cohort CSV file and press enter: ")).strip('"')
    print(Fore.RESET)
except Exception as e:
    print(Fore.RED)
    input(f"{e}\nThere was a problem reading the file")
    quit()

try:
    primary = pd.read_csv(prim, skiprows=3, parse_dates=[["Start Date", "Start Time"], ["End Date", "End Time"]],
                          keep_default_na='')
    secondary = pd.read_csv(sec, sep='|', skiprows=1,
                            parse_dates=[["Start Date", "Start Time"], ["End Date", "End Time"]], keep_default_na='')
except Exception as e:
    print(Fore.RED)
    input(f"{e}\nThere was a problem processing the files.")
    quit()


def checker(prim, sec, error, error_in_this_data_row):
    prim_list = prim.strip(";").split(";")
    sec_list = sec.strip(";").split(';')

    prim_list = list((i.replace('\r', '').replace('\n', '') for i in prim_list))
    sec_list = list((i.replace('\r', '').replace('\n', '') for i in sec_list))

    for item in prim_list:
        if item not in sec_list:
            error += 1
            error_in_this_data_row += 1

    return error, error_in_this_data_row


print(f"{Fore.GREEN}\nChecking data shape")
if primary.shape[0] == secondary.shape[0]:
    print(f"Data shape {primary.shape} are same ...proceeding")
else:
    print(Fore.RED, f"Data shape of \n Primary = {primary.shape} \n Secondary = {secondary.shape}")
    print('No of data do not match in both files')
    print("Data is not of required shape ...please try again", Fore.RESET)
    print("\n\n\n**Contact Me:\n"
          "nabil@interviewkickstart.com")
    input("Press enter to quit.")
    quit()

try:
    headers = list(primary.keys())
    headers.remove('Topic Code')
    headers.remove('Status')
except Exception as e:
    print(Fore.RED)
    input(f"{e}\nData header name does not have Topic Code &/or Status column to be dropped...please try again")
    quit()

final_data = {'Origin': [], 'No of error': []}
error = 0
error_freq_list = []

for header in headers:
    final_data[header] = []

try:
    for i in range(len(primary)):
        error_in_this_data_row = 0
        for header in headers:
            final_data[header].append(primary[header][i])

            if primary[header][i] == secondary[header][i]:
                final_data[header].append('')
            else:

                if header in ["Start Date_Start Time", "End Date_End Time"]:

                    if type(primary[header][i]) == str and len(primary[header][i]) > 1:
                        primary[header][i] = datetime.datetime.strptime(primary[header][i], '%Y-%m-%d %H:%M:%S')
                    if type(secondary[header][i]) == str and len(secondary[header][i]) > 1:
                        secondary[header][i] = datetime.datetime.strptime(secondary[header][i], '%Y-%m-%d %H:%M:%S')

                    if type(primary[header][i]) != str and type(secondary[header][i]) != str:
                        if primary[header][i].date() != secondary[header][i].date():
                            error += 1
                            error_in_this_data_row += 1
                        if primary[header][i].time() != secondary[header][i].time():
                            error += 1
                            error_in_this_data_row += 1
                        final_data[header].append(str(secondary[header][i]) + "(Missing/Wrong value)")
                        final_data[header].append('')
                        continue
                if header in ["Helpful Material"]:
                    error, error_in_this_data_row = checker(primary[header][i], secondary[header][i], error,
                                                            error_in_this_data_row)
                    diff = (set(primary[header][i].split(";")) - set(secondary[header][i].split(";")))
                    final_data[header].append(str(diff)[1:-1] + "(Missing/Wrong value)")
                    final_data[header].append('')
                    continue
                final_data[header].append(str(secondary[header][i]) + "(Missing/Wrong value)")
                error += 1
                error_in_this_data_row += 1
            final_data[header].append('')
        for item in ['Source', 'Uplevel', '']:
            final_data['Origin'].append(item)
        for j in range(2):
            final_data['No of error'].append(f'Errors : {error_in_this_data_row}')
        final_data['No of error'].append('')
        error_freq_list.append(error_in_this_data_row)
except Exception as e:
    print(Fore.RED)
    input(f"{e}\nThere was a problem in generating the score")
    quit()

print(Fore.WHITE, "\n\nScore = ", error * -1, Fore.RESET)

final_data = pd.DataFrame(final_data)
file_name = f"Output({str(datetime.datetime.now().strftime('%d_%m_%y %H_%M_%S'))}).csv"
final_data.to_csv(file_name)
print(Fore.MAGENTA, f"\nOutput file generated: {Fore.LIGHTRED_EX}{file_name}")
input(f"\nPress enter to exit.")
