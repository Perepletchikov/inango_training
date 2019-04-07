# -*- coding: utf-8 -*-


class Palindrome:
    def __init__(self):
        pass

    @staticmethod
    def recursion(input_string):
        result = ''
        if len(input_string) > 1:
            if input_string[0] == input_string[-1]:
                letter = input_string[0]
                input_string = input_string[1:-1]
                result = letter + Palindrome.recursion(input_string) + letter
                return result
            else:
                input_string_right = input_string[:-1]
                input_string_left = input_string[1:]
                result_right = Palindrome.recursion(input_string_right)
                result_left = Palindrome.recursion(input_string_left)
                if len(result_right) > len(result_left):
                    return result_right
                else:
                    return result_left
        else:
            if len(result) > 0:
                return result[len(result)/2:] + input_string + result[:len(result)/2]
            else:
                return input_string


if __name__ == '__main__':
    print(Palindrome.recursion("dfghgtd"))