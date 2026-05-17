running_total = 0

num_of_friends = int(input('Number of people:'))

appetizers = float(input('enter price of appetizers:'))
main_courses = float(input('enter price of main course:'))
desserts = float(input('enter price of desserts:'))
drinks = float(input('enter price of drinks:'))

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip_percentage_want_to_give = float(input("tip want to give:"))
tip = running_total * tip_percentage_want_to_give
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill,2)
print('Each person pays:',each_pays)