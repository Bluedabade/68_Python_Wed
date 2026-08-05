def merge_sort(arr):
    # ถ้าข้อมูลมี 1 ตัวหรือน้อยกว่า ถือว่าเรียงแล้ว
    if len(arr) <= 1:
        return arr
    # หาตำแหน่งกึ่งกลางของข้อมูล
    mid = len(arr) // 2
    # แบ่งข้อมูลออกเป็นฝั่งซ้าย แล้วเรียก merge_sort ซ้ำ
    left = merge_sort(arr[:mid])
    # แบ่งข้อมูลออกเป็นฝั่งขวา แล้วเรียก merge_sort ซ้ำ
    right = merge_sort(arr[mid:])
    # สร้าง list ว่างไว้เก็บผลลัพธ์ที่เรียงแล้ว
    result = []
    # เปรียบเทียบค่าของข้อมูลฝั่งซ้ายและฝั่งขวา
    while left and right:
        if left[0] < right[0]:          # ถ้าค่าฝั่งซ้ายเล็กกว่า
            result.append(left.pop(0))  # นำค่าฝั่งซ้ายมาใส่
        else:                           # ถ้าค่าฝั่งขวาเล็กกว่า
            result.append(right.pop(0)) # นำค่าฝั่งขวามาใส่  
    # รวมค่าที่เหลือทั้งหมด (ถ้ามี) แล้วส่งกลับ
    return result + left + right
# --- ตัวอย่างการใช้งาน ---
numbers = [8, 3, 5, 2, 9]
sorted_numbers = merge_sort(numbers)
print("ผลลัพธ์:", sorted_numbers)