# solution: 정렬 후, 작은 수를 시작으로 그룹중 최댓값과 그룹크기 비교.

# start_input
print("인원수 : ", end='')
num = int(input())

print("공포도 : ", end='')
member = list(map(int, input().split()))
# end_input

member.sort()
grp_list = []
i = 0
while i < num: 
    grp=[]
    for j in range(i, num):
        grp.append(member[j])
        if len(grp) == max(grp):
            grp_list.append(grp)
            break

    i = j+1

# start_print
for i, grp in zip(range(len(grp_list)), grp_list):
    print("Group " + str(i) + " : " + str(grp_list[i]))

print("# : " + str(len(grp_list)))
# end_print