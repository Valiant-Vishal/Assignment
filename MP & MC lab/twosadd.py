import add
import onesandtwos as ot

first = input('Enter the first number: ')
second = input("Enter the second number: ")

print(first,'-',second)

print("Step 1 -> twos compliment of second no.")
TC = ot.twoscompliment(second)
print(TC)

print("step 2 -> Add first no with ones compliment of second no")
Add = add.add(first, TC)
print(Add[0])

if Add[1] == '1':
    print("step 3 -> the result generated in step 2 have carry so discard the carry")
    print("Final result:",Add[0])
elif Add[1] == '0':
    print("step 3 -> No carry is generated ('-'ve) value 2's compliment of the result generated in step 2")
    print(ot.twoscompliment(Add[0]))