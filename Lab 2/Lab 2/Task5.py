#Explanation: Recursive function (reverse) takes string pointer (str) as input and calls itself with next location to passed pointer (str+1). Recursion continues this way, when pointer reaches ‘\0’, all functions accumulated in stack print char at passed location (str) and return one by one.
#Time Complexity: O(n)

def rev (str):
    if (str == ""):
        return ""
    else:
        return rev (str[1:]) + str[0]


print (rev("Hello"))