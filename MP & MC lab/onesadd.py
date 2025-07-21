import add
import onesandtwos as ot

first = input('Enter the first number: ')
second = input("Enter the second number: ")
print(first,'-',second)
print("Step 1 -> ones compliment of second no.")
OC = ot.onescompliment(second)
print(OC)

print("step 2 -> Add first no with ones compliment of second no")
Add = add.add(first, OC)
print(Add[0])

if Add[1] == '1':
    print("step 3 -> Add by carry of 1 with the result generated in step 2")
    Add = add.add(Add[0], '1')
    print(Add[0])
elif Add[1] == '0':
    print("step 3 -> No carry is generated ('-'ve) value 1's compliment of the result generated in step 2")
    print(ot.onescompliment(Add[0]))