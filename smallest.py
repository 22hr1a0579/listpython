'''Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1'''


n = int(input())
elements = []
for _ in range(n):
    element = int(input())
    elements.append(element)
smallest_number = min(elements)
print(smallest_number)
