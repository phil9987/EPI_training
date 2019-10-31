from test_framework import generic_test


def evaluate(expression):
    stack = []
    operators = {
        '+': lambda y, x : x + y,
        '-': lambda y, x : x - y,
        '*': lambda y, x : x * y,
        '/': lambda y, x : x // y
    }
    for token in expression.split(','):
        if token in operators:
            stack.append(operators[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
