import pandas
import openpyxl
import requests
import json

# user_df = pandas.read_excel("users.xlsx")


# for index, rows in user_df.iterrows():
#     json = {
#         "name": rows.user_name,

#         "phone": rows.phone,
#         "email": rows.email,
#         "password": rows.passwd,
#         "conf_password": rows.passwd,
#         "id_type": "111",
#         "id_number": "222"
#     }

#     url = 'http://127.0.0.1:8000/users/'

#     r = requests.post(url, json=json)

#     print(r.status_code)


###############  FORMAT CHECKER  #################
allowed_fields = ["apple", "banana", "orange"]
alert_list = []

work_book = openpyxl.load_workbook("./tests.xlsx")
active_cell = work_book.active
active_list = list(active_cell)

active_cell_row = []
active_cell_col = []
active_cell_val = []
active_cell_all = []

for x in active_list:
    for y in x:
        if y.value != None:
            active_cell_row.append(y.row)
            active_cell_col.append(y.column)
            active_cell_val.append(y.value)
            active_cell_all.append([y.row, y.column, y.value])


# print(type(active_cell_row[4]))
present_fields = []
first_non_empty_row = min(active_cell_row)
last_non_empty_row = max(active_cell_row)
first_non_empty_column = min(active_cell_col)
last_non_empty_column = max(active_cell_col)

# print(first_non_empty_row)
for x in active_cell_all:
    if x[0] == first_non_empty_row:
        present_fields.append((x[0], x[1], x[2]))
print(f"present_fields : {present_fields}")
print(f"first_non_empty_row : {first_non_empty_row}")
print(f"last_non_empty_row :{last_non_empty_row}")
print(f"first_non_empty_column :{first_non_empty_column}")
print(f"last_non_empty_column :{last_non_empty_column}")
if allowed_fields != present_fields:
    alert_list.append(
        ("improper file structuring , plz download sample file and try again", "alert"))
    # RETURN
