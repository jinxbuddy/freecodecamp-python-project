def arithmetic_arranger(problems, result_flag = True):


    firstx=''
    lastx=''
    dash=''
    resultx=''

    for problem in problems:
        first, sign, last= problem.split(' ')
        if  first.isdigit() is False or last.isdigit() is False:
            return "Error: Numbers must only contain digits."

        if sign != '+' and sign != '-':
            return "Error: Operator must be '+' or '-'."

        if len(first) > 4 or len(last) > 4:
            return "Error: Numbers cannot be more than four digits."


        result = ""
        if(sign == "+"):
            result = str(int(first) + int(last))
        elif(sign == "-"):
            result = str(int(first) - int(last))

        length = max(len(first), len(last)) + 2
        top= str(first.rjust(length))
        bottom = sign + str(last).rjust(length - 1)

        dashes = ''
        gap = str(result).rjust(length)
        for s in range(length):
            dashes += '-'

        if problem != problems[-1]:
            firstx += top + '    '
            lastx += bottom + '    '
            dash += dashes + '    '
            resultx += gap + '    '
        else:
            firstx += top
            lastx += bottom
            dash += dashes
            resultx += gap

    if result_flag:
        final = firstx + '\n' + lastx + '\n' + dash +'\n' + resultx
    else:
        final = firstx + '\n' + lastx + '\n' + dash
    return final



