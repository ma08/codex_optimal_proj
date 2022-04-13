

def main():
    """Bard - ประชาชน
    num_villagers = int(input()) # จำนวนประชาชน
    num_evenings = int(input()) # จำนวนคืน
    bard_list = [] # รายชื่อประชาชนที่มีการประชาสัมพันธ์กัน
    bard_list.append(1) # ประกาศว่ามีการประชาสัมพันธ์ระหว่าง Bard กับประชาชนทั้งหมด
    for _ in range(num_evenings): # วนลูปตามจำนวนคืน
        num_villagers_present = int(input()) # จำนวนประชาชนที่มาทำกิจกรรมกัน
        villager_list = [int(i) for i in input().split()] # รายชื่อประชาชนที่มาทำกิจกรรมกัน
        if 1 in villager_list: # ถ้ามีการประชาสัมพันธ์ระหว่าง Bard กับประชาชนในคืนนั้น
            for i in villager_list: # วนลูปตามประชาชนที่มาทำกิจกรรมกัน
                if i not in bard_list: # ถ้าประชาชนนั้นยังไม่มีการประชาสัมพันธ์กับ Bard
                    bard_list.append(i) # เพิ่มประชาชนนั้นในรายชื่อประชาชนที่มีการประชาสัมพันธ์กับ Bard
        else: # ถ้าไม่มีการประชาสัมพันธ์ระหว่าง Bard กับประชาชนในคืนนั้น
            for i in villager_list: # วนลูปตามประชาชนที่มาทำกิจกรรมกัน
                if i not in bard_list: # ถ้าประชาชนนั้นยังไม่มีการประชาสัมพันธ์กับ Bard
                    bard_list.append(i) # เพิ่มประชาชนนั้นในรายชื่อประชาชนที่มีการประชาสัมพันธ์กับ Bard
    bard_list.sort() # เรียงลำดับรายชื่อประชาชนที่มีการประชาสัมพันธ์กับ Bard
    for i in bard_list: # วนลูปตามประชาชนที่มีการประชาสัมพันธ์กับ Bard
        print(i) # แสดงประชาชนที่มีการประชาสัมพันธ์กับ Bard
    """

if __name__ == "__main__":
    main()
