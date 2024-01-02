'''
Pseudo code:

Design a program that determines the award a a person competing in a triathlon will recieve
read the time in minutes for all three events:
swimming
cycling 
running
calculate and display the total time taken to complete triathlon
reward is based on total time taken 
qulifiying time for award is 100mins
display award participent will recieve

critera: 
QT = within 0 - 100 mins, 
reward = provincial colors

QT2 = within 101- 105 mins
reward = provincial half colors

QT3 = 106 - 110 mins
provincial scroll

QT4 = 111+ mins 
no award

'''
# When program is run print greeting and short statement explaining hoe to confirm award  

greeting = 'Welcome to the award calculator'
request = 'Please record participent name and scores below  and press Enter to confirm award,'

print (greeting)
print(request)

#variable to request and store participent name
participent = input('Name:')

#Events

swimming = int(input('Swimming score: '))
cycling = int(input('Cycling score: '))
running = int(input('Running score'))

# Calculate scores to determine total points achieved
 
total_time = swimming + cycling + running

#convert int into string and output total time result

print ('Total time = ' + str(total_time))

# qt = Qualifying Time

'''

#qt award ranges
qt1 = 0<>100
qt2 = 101<>105
qt3 = 106<>110
qt4 = 111>

'''
#Check to see what range participent total score will be in and print results
if total_time in range (0,100):
    print(f'{participent} has achieved a Provincial colors award with {total_time} points')
elif total_time in range(101,105):
    print(f'{participent} has achieved a Provincial half colours award with {total_time} points')
elif total_time in range(106,110):
    print(f'{participent} has achieved a Provincial scroll award with {total_time} points')
else:
    print (f'{participent} has achieved a No award  with {total_time} points')


