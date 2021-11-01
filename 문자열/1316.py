num = int(input())
count = 0
for i in range(num):
    word = input()
    for index in range(len(word)): #index로 접근
        if index != len(word)-1:
            if word[index] == word[index+1]:
                continue
            elif word[index] in word[index+1:]:
                break
        else:
            count+=1
print(count)
