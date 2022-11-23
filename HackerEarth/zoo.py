# You are required to enter a word that consists of  and  
# that denote the number of Zs and Os respectively. 
# The input word is considered similar to word zoo if y = 2x
# For example, words such as zzoooo and zzzoooooo are similar to word zoo 
# but not the words such as zzooo and zzzooooo.
word = input()
x = "z"
y = "o"
# couting the number of x and y in word
count_x = word.count(x)
count_y = word.count(y)
if count_y == (count_x * 2):
    print("Yes")
else:
    print("No")
# print("xs are {} and ys are {} in the word {}".format(count_x, count_y, word))
