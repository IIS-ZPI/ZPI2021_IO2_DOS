import sample.core
import sample.helpers

print(sample.core.get_hmm())

if sample.helpers.get_answer() == True:
    x = input("It works!!!")
else:
    x = input("It doesn't work!!!")
