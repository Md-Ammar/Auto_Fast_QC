import pandas as pd
import os

os.system("Color 0a")

print(">>Welcome to IK Cohort Auto QC.\n",
      "This software should be used to check cohorts automatically\n",
      "Designed and developed: Nabil Hassan\n\n",
      "_"*80
      )

try:
    prim = str(input("Please drag and drop source CSV file and press enter: ")).strip('"')
    sec = str(input("Please drag and drop the Uplevel GC Cohort CSV file and press enter: ")).strip('"')
except:
    input("There was a problem reading the file")

try:
    primary = pd.read_csv(prim, skiprows=3,
                          parse_dates=[["Start Date", 'Start Time'], ['End Date', 'End Time']], keep_default_na='')
    secondary = pd.read_csv(sec, sep='|', skiprows=1,
                            parse_dates=[["Start Date", 'Start Time'], ['End Date', 'End Time']], keep_default_na='')
except:
    input("There was a problem processing the files.")
    quit()

if primary.shape == secondary.shape:
    print(f"{primary.shape} is the shape of both datas")
else:
    print(f"Data shape of \n Primary = {primary.shape} \n Secondary = {secondary.shape}")
    primary_resource_name = list(primary['Resource Name'])
    secondary_resource_name = list(secondary['Resource Name'])
    print("Data is not of required shape ...please try again")
    print("\n\n\n**Contact Me:\n"
          "nabil@interviewkickstart.com")
    input("Press enter to quit.")
    quit()

headers = list(primary.keys())
headers.remove('Topic Code')
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
            if (primary[header][i]) != (secondary[header][i]):
                final_data[header].append(secondary[header][i])
                error += 1
                error_in_this_data_row += 1
            else:
                final_data[header].append('')
            final_data[header].append('')
        for item in ['Source', 'Uplevel', '']:
            final_data['Origin'].append(item)
        for j in range(2):
            final_data['No of error'].append(f'Errors : {error_in_this_data_row}')
        final_data['No of error'].append('')
        error_freq_list.append(error_in_this_data_row)
except:
    input("There was a problem in generating the score")
    quit()

# print('Error frequency list', error_freq_list)
# print("Total No of Errors = -", error)
print("Score =", error)

final_data = pd.DataFrame(final_data)
final_data.to_csv("final_data.csv")
print("Output file generated final_data.csv")
input("Press enter to exit.")

