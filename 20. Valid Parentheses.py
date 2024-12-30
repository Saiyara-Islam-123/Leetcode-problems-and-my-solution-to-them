dict_bracket = {
    "(": ")",
    "[": "]",
    "{": "}"

}
start_bracket = ["(", "{", "["]
end_bracket = [")", "}", "]"]


class Solution(object):

    def isValid(self, s):

        class Stack:
            def __init__(self):
                self.list = []

            def push(self, x):
                self.list.append(x)

            def pop(self):
                last_element = self.list[-1]
                self.list.pop(len(self.list) - 1)
                return last_element

            def is_empty(self):
                return len(self.list) == 0

        stack = Stack()

        for i in range(len(s)):
            if s[i] in start_bracket:
                stack.push(s[i])
            elif s[i] in end_bracket:

                if stack.is_empty():
                    return False

                if s[i] != dict_bracket[stack.pop()]:
                    return False

        return len(stack.list) == 0