def validate_row(row, criteria, maybe=False):
    criteria_nums = [int(x) for x in criteria.split(" ")]
    if criteria_nums[0] == 0:
        return not any(row)
    i = 0
    j = 0
    count = 0
    while i < len(row):
        val = row[i]
        if val:
            count += 1
        else:
            if count > 0:
                if count == criteria_nums[j]:
                    count = 0
                    j += 1
                    if j >= len(criteria_nums):
                        break
                else:
                    return False
        i += 1
    if not maybe:
        if count > 0:
            if count == criteria_nums[j]:
                j += 1
            else:
                return False
        if j < len(criteria_nums):
            return False
    if i < len(row):
        if any(row[i:]):
            return False
    return True

def generate_rows(criteria, n):
    rows = []
    generate_rows_helper(criteria, n, [], rows)
    return rows

def generate_rows_helper(criteria, n, current_row, rows):
    if n == 0:
        if validate_row(current_row, criteria):
            rows.append(current_row)
        return
    generate_rows_helper(criteria, n-1, current_row + [True], rows)
    generate_rows_helper(criteria, n-1, current_row + [False], rows)

def generate_matrix(row_criterias, col_criterias):
    rows = [generate_rows(x, len(col_criterias)) for x in row_criterias]
    result = []
    generate_matrix_helper(col_criterias, rows, 0, [], result)
    return result
    
def generate_matrix_helper(col_criterias, rows, i, matrix, result):
    for col in range(len(col_criterias)):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        if not validate_row(temp, col_criterias[col], maybe=(i < len(rows))):
            return
    if i >= len(rows):
        result.append(matrix)
        return
    for row in rows[i]:
        generate_matrix_helper(col_criterias, rows, i+1, matrix + [row], result)

row_criterias = [x.strip() for x in input("Enter row criterias separated by comma... ").split(",")]
col_criterias = [x.strip() for x in input("Enter column criterias separated by comma... ").split(",")]
print("\n\n".join(["\n".join([" ".join("@" if z else "." for z in y) for y in x]) for x in generate_matrix(row_criterias, col_criterias)]))
input()