# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
#Input Format
#The first line contains n. The second line contains an array A[]  of n integers each separated by a space.
#Constraints:
# 2 <= n <=10
# -100 <= A[i] <= 100
#Output Format
#Print the runner-up score.
"""
Sample Input 0
5
2 3 6 6 5
Sample Output 0
5
Explanation 0
Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""
n = int(input())
arr = map(int, input().split())
new_list = list(map(int, arr))
best = -100
run_up = -100
if 2 <= n <= 10:
    for i in range(0, len(new_list)):
        if -100 <= new_list[i] <= 100:
            if new_list[i] > run_up and new_list[i] != best:
                if new_list[i] > best:
                    run_up = best
                    best = new_list[i]
                else:
                    run_up = new_list[i]
print(run_up)


    