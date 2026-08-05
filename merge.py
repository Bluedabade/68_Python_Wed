def merge_sort(arr, depth=0):
    indent = "    " * depth  # สร้างย่อหน้าตามความลึก
    print(f"{indent}➡️ กำลังแยก: {arr}")

    # Base Case: ถ้ามี 1 ตัว เรียงเสร็จแล้ว
    if len(arr) <= 1:
        print(f"{indent}✅ คืนค่า (Base Case): {arr}")
        return arr
    
    mid = len(arr) // 2
    
    # เรียกตัวเองซ้ำ (ส่ง depth+1 เพื่อขยับย่อหน้า)
    left = merge_sort(arr[:mid], depth+1)
    right = merge_sort(arr[mid:], depth+1)
    
    # --- เริ่มกระบวนการ Merge ---
    print(f"{indent}🔄 กำลังรวม: ซ้าย{left} vs ขวา{right}")
    
    result = []
    # ใช้ .copy() เพื่อไม่ให้กระทบค่าต้นฉบับตอน print (เผื่อไว้ดู debug)
    temp_left = left.copy()
    temp_right = right.copy()

    while temp_left and temp_right:
        # Print เทียบค่า
        if temp_left[0] < temp_right[0]:
            print(f"{indent}   ⚡ {temp_left[0]} < {temp_right[0]} (ซ้ายชนะ)")
            result.append(temp_left.pop(0))
        else:
            print(f"{indent}   ⚡ {temp_right[0]} < {temp_left[0]} (ขวาชนะ)")
            result.append(temp_right.pop(0))
            
    # รวมเศษที่เหลือ
    merged_result = result + temp_left + temp_right
    print(f"{indent}✨ ผลรวมรอบนี้: {merged_result}")
    return merged_result

# --- ทดสอบด้วยข้อมูล 4 ตัว (เพื่อให้ดู Log ง่าย) ---
numbers = [8, 3, 5, 2, 9]
print(len(numbers))
print("--- เริ่มต้น ---")
sorted_numbers = merge_sort(numbers)
print("\n--- ผลลัพธ์สุดท้าย ---")
print(sorted_numbers)