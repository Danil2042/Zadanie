Question_1 = int(input())
Count = Question_1 // Question_1

while Count != Question_1 + 1:
    line_1 = "*" * Count
    Otvet_1 = line_1.center(Question_1 + Count)
    if Count == 1:
        print(Otvet_1)
    line_2 = '**' * Count
    Otvet_2 = line_2.center(Question_1 + Count)
    print(Otvet_2)
    Count += 1
