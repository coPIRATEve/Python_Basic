def multiply_polynomials(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coeff1 in enumerate(poly1):
        for j, coeff2 in enumerate(poly2):
            result[i + j] += coeff1 * coeff2
    return result

def print_polynomial(poly, var='x'):
    terms = []
    for i, coeff in enumerate(poly):
        if coeff != 0:
            term = ''
            if coeff != 1 or i == 0:
                term += str(coeff)
            if i > 0:
                term += var
                if i > 1:
                    term += '^' + str(i)
            terms.append((i, term))
    # Sort terms by power in descending order
    terms.sort(reverse=True, key=lambda x: x[0])
    return ' + '.join(term for _, term in terms)

def main():
    print("Введите тип операции над многочленами (sum или diff):")
    op_type = input().strip()
    if op_type not in ['sum', 'diff']:
        print("Неверный тип операции")
        return

    print("Введите степень первого многочлена:")
    degree1 = int(input().strip())
    poly1 = []
    for i in range(degree1 + 1):
        print(f"Введите коэффициент x^{i}:")
        poly1.append(float(input().strip()))

    print("Введите степень второго многочлена:")
    degree2 = int(input().strip())
    poly2 = []
    for i in range(degree2 + 1):
        print(f"Введите коэффициент x^{i}:")
        poly2.append(float(input().strip()))

    if op_type == 'sum':
        if len(poly1) > len(poly2):
            poly2.extend([0] * (len(poly1) - len(poly2)))
        else:
            poly1.extend([0] * (len(poly2) - len(poly1)))
        result_poly = [a + b for a, b in zip(poly1, poly2)]
    else:
        if len(poly1) > len(poly2):
            poly2.extend([0] * (len(poly1) - len(poly2)))
        else:
            poly1.extend([0] * (len(poly2) - len(poly1)))
        result_poly = [a - b for a, b in zip(poly1, poly2)]

    print("Первый многочлен:", print_polynomial(poly1))
    print("Второй многочлен:", print_polynomial(poly2))
    print("Результат операции:", print_polynomial(result_poly))

    print("Введите число, на которое умножить результат:")
    num = float(input().strip())
    result_poly = [coeff * num for coeff in result_poly]
    print("Результат умножения:", print_polynomial(result_poly))

if __name__ == "__main__":
    main()
