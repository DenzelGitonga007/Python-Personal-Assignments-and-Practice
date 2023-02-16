# Import the part1 file
from part1 import * # imports all the functions in part1
import datetime
def get_from_date():
    from_date_str = input("Enter from date (mm/dd/yyyy): ")
    from_date = datetime.datetime.strptime(from_date_str, '%m/%d/%Y')
    return from_date
def get_to_date():
    to_date_str = input("Enter to date (mm/dd/yyyy): ")
    to_date = datetime.datetime.strptime(to_date_str, '%m/%d/%Y')
    return to_date

def calculate_tax_and_netpay(total_hours, hourly_rate, tax_rate):
    tax = float(total_hours) * float(hourly_rate) * (float(tax_rate) / 100)
    net_pay = float(total_hours) * float(hourly_rate) - tax
    return tax, net_pay

def display_employee_info(employee_data):
    print("----------------------------------------------------")
    print("Employee name:", employee_data['name'])
    print("From date:", employee_data['from_date'].strftime('%m/%d/%Y'))
    print("To date:", employee_data['to_date'].strftime('%m/%d/%Y'))
    print("Total hours:", employee_data['hours'])
    print("Hourly rate:", employee_data['hourly_rate'])
    print("Tax rate:", employee_data['tax_rate'])
    print("Gross pay:", employee_data['gross_pay'])
    print("Income tax:", employee_data['tax'])
    print("Net pay:", employee_data['net_pay'])
    print("----------------------------------------------------")

def display_total_info(total_data):
    print("----------------------------------------------------")
    print("Total number of employees:", total_data['employees'])
    print("Total hours:", total_data['hours'])
    print("Total tax:", total_data['tax'])
    print("Total gross pay:", total_data['gross_pay'])
    print("Total net pay:", total_data['net_pay'])
    print("----------------------------------------------------")

def main():
    employee_data = []
    total_data = {
    'employees': 0,
    'hours': 0,
    'tax': 0,
    'gross_pay': 0,
    'net_pay': 0
    }

    while True:
        name = get_name()
        if name == "End":
            break
        from_date = get_from_date()
        to_date = get_to_date()
        hours = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        gross_pay = get_gross_pay(hours, hourly_rate)
        tax, net_pay = calculate_tax_and_netpay(hours, hourly_rate, tax_rate)

        # store employee data in a list
        employee_data.append({
        'name': name,
        'from_date': from_date,
        'to_date': to_date,
        'hours': hours,
        'hourly_rate': hourly_rate,
        'tax_rate': tax_rate,
        'gross_pay': gross_pay,
        'tax': tax,
        'net_pay': net_pay
        })

        # update total

        total_data['employees'] += 1
        total_data['hours'] += hours
        total_data['tax'] += tax
        total_data['gross_pay'] += gross_pay
        total_data['net_pay'] += net_pay

    for employee in employee_data:
        display_employee_info(employee)
        display_total_info(total_data)



if __name__ == "__main__":
    main() 

