import pandas as pd
import os
import datetime
import pyfiglet

result = pyfiglet.figlet_format("Auto Fast QC", )
print(result)

print(">>Welcome to IK Cohort Auto QC.\n",
      "This software should be used to check cohorts automatically\n",
      "Designed and developed: Nabil Hassan\n\n",
      "_" * 80
      )

try:
    prim = str(input("Please drag and drop source CSV file and press enter: ")).strip('"')
    sec = str(input("Please drag and drop the Uplevel GC Cohort CSV file and press enter: ")).strip('"')
except Exception as e:
    print(e)
    input("There was a problem reading the file")
    quit()

try:
    primary = pd.read_csv(prim, skiprows=3, parse_dates=[["Start Date", "Start Time"], ["End Date", "End Time"]],
                          keep_default_na='')
    secondary = pd.read_csv(sec, sep='|', skiprows=1,
                            parse_dates=[["Start Date", "Start Time"], ["End Date", "End Time"]], keep_default_na='')
except Exception as e:
    input(f"{e}\nThere was a problem processing the files.")
    quit()


def checker(prim, sec, error, error_in_this_data_row):
    prim_list = prim.strip(";").split(";")
    sec_list = sec.strip(";").split(';')

    for item in prim_list:
        if item not in sec_list:
            error += 1
            error_in_this_data_row += 1

    return error, error_in_this_data_row


print("\nChecking data shape")
if primary.shape[0] == secondary.shape[0]:
    print(f"Data shape {primary.shape} are same ...proceeding")
else:
    print(f"Data shape of \n Primary = {primary.shape} \n Secondary = {secondary.shape}")
    primary_resource_name = list(primary['Resource Name'])
    secondary_resource_name = list(secondary['Resource Name'])
    print("Data is not of required shape ...please try again")
    print("\n\n\n**Contact Me:\n"
          "nabil@interviewkickstart.com")
    input("Press enter to quit.")
    quit()

try:
    headers = list(primary.keys())
    headers.remove('Topic Code')
    headers.remove('Status')
except Exception as e:
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
                if header in ["Start Date_Start Time", "End Date_End Time"] and \
                        type(primary[header][i]) != str and \
                        type(secondary[header][i]) != str:
                    if primary[header][i].date() == secondary[header][i].date():
                        pass
                    else:
                        error += 1
                        error_in_this_data_row += 1
                    if primary[header][i].time() == secondary[header][i].time():
                        pass
                    else:
                        error += 1
                        error_in_this_data_row += 1
                    final_data[header].append(str(secondary[header][i]) + "(Missing/Wrong value)")
                    final_data[header].append('')
                    continue
                if header in ["Helpful Material"]:
                    error, error_in_this_data_row = checker(primary[header][i], secondary[header][i], error,
                                                            error_in_this_data_row)
                    final_data[header].append(str(secondary[header][i]) + "(Missing/Wrong value)")
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
    input(f"{e}\nThere was a problem in generating the score")
    quit()

print("\n\nScore = -", error)

final_data = pd.DataFrame(final_data)
file_name = f"Output({str(datetime.datetime.now().strftime('%d_%m_%y %H_%M_%S'))}).csv"
final_data.to_csv(file_name)
print(f"\nOutput file generated {file_name}")
input("\nPress enter to exit.")
