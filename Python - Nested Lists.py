if __name__ == '__main__':

    student=[]
    scores = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        student.append([name,score])
        scores.append(score)

scores = sorted(set(scores))
m = scores[1]

names = []

for val in student:
    if m == val[1]:
        names.append(val[0])

names=sorted(names)
for j in names:
    print(j)



