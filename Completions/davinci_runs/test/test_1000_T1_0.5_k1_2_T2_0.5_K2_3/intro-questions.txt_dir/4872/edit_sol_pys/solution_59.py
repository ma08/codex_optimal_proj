
def house_of_cats(legs):
    if legs % 4 == 0:
        return [legs // 4, 0]
    if legs % 4 == 1:
        return [legs // 4, 1]
    if legs % 4 == 2:
        return [legs // 4, 2]
    if legs % 4 == 3:
        return [legs // 4, 3]


print(house_of_cats(8))
