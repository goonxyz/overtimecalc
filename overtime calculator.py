hours = float(input('Enter full-time hours: '))
hourly_pay = float(input('Enter how much you earn an hour: $'))
overtime_hours_week1 = float(input('OT hours week 1 (use only this if paid weekly): '))
overtime_hours_week2 = float(input('OT hours week 2 (only use if paid biweekly): '))

overtime_pay = hourly_pay * 1.5
overtime = overtime_pay * (overtime_hours_week1 + overtime_hours_week2)

# Pay after taxes (.20 is a placeholder, a rough guess for paycheck tax total)
hourly_pay = hourly_pay - (hourly_pay * .20)

# Math for weekly pay, biweekly pay, monthly pay, and total salary
weekly_pay = float(hourly_pay) * float(hours)
weekly_pay_OT = weekly_pay + overtime

biweekly_OT_hours = overtime_hours_week1 + overtime_hours_week2
biweekly_pay = float(weekly_pay) * 2
biweekly_pay_OT = float(biweekly_pay) + overtime

monthly_pay = float(biweekly_pay)  * 2
monthly_pay_OT = float(monthly_pay) + overtime

print('----------------------------------------')
print('weekly pay: $' + str(weekly_pay))
print('weekly pay with', str(overtime_hours_week1), 'overtime hours worked: $' + str(weekly_pay_OT))

print('Biweekly pay: $' + str(biweekly_pay))
print('Biweekly pay with', str(biweekly_OT_hours), 'overtime hours worked: $' + str(biweekly_pay_OT))

print('monthly pay $' + str(monthly_pay))
print('monthly pay with', str(biweekly_OT_hours), 'overtime hours worked: $' + str(monthly_pay_OT))
print('----------------------------------------')