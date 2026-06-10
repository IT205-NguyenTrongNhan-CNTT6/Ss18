
def get_validate_input(promt:"str",input_type : str = "string"):
    while True:
        user_input = input(promt)
        if not user_input:
            print("Dữ liệu không được để trống")
            continue
        if input_type == "int":
                try:
                    value = int(user_input)
                    if value < 0:
                        print("Dữ liệu phải là số nguyên dương!")
                        continue
                    return value
                except ValueError:
                    print("Dữ liệu không hợp lệ, Nhập lại!")
                    continue
        return user_input

def show_inventory(inventory):
    if not inventory:
        print("Dữ liệu danh sách rỗng")
        return

    print("----Danh Sách Tồn Kho----")
    print(f"{'ID':<10}| {'Tên Hàng Hóa':<15}| {'Số lượng tôn':<15}")
    for items in inventory:
        print(f"{items.get('id'):<12}| {items.get('name'):<17}| {items.get('quantity'):<17}")

def add_item(inventory):
    while True:
        print("---Nhập hàng hóa mới---")
        add_id = get_validate_input("Nhập mã hàng hóa: ")
        for item in inventory:
            if(add_id.lower() == item.get("id").lower()):
                print("Dữ liệu không được trùng")
                break
        else:
            add_name = get_validate_input("Nhập tên hàng hóa: ")
            add_quanlity = get_validate_input("Nhập số lượng tồn kho: ","int")

            new_item = {
                "id" : add_id,
                "name" : add_name,
                "quantity" : add_quanlity
            }
            inventory.append(new_item)
            print("Đã thêm")
            break

def upd_inventory(inventory):
    while True:
        print("---Cập Nhật Số Lượng Tồn Kho---")
        upd_id = get_validate_input("Nhập mã hàng hóa: ")
        for item in inventory:
            if(upd_id.lower() == item.get("id").lower()):
                print(f"Tìm thấy hàng hóa : {item.get('name')} (Số lượng hiện tại:{item.get("quantity")})") 
            upd_quanlity = get_validate_input("Nhập số lượng làm mới: ","int")
            inventory["quantity"] == upd_quanlity
            print("Đã tiến hành cập nhật")
        else :
            print("Không tìm thấy")


def menu():
    print("="*25)

    print("Quản Lý Kho Hàng - Grocery Store")
    print("="*25)
    print("1.Xem danh sách hàng tồn kho\n"+
          "2.Nhập thêm hàng hóa mới\n"+
          "3.Cập nhật số lượng tồn kho theo ID\n"+
          "4.Thoát")
    
def main():
    inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]   
    menu()
    while True: 
        choice = get_validate_input("Nhập lựa chọn của bạn: ")
        match choice :
            case '1':
                show_inventory(inventory)
            case '2':
                add_item(inventory)
            case '3':
                upd_inventory(inventory)
            case '4':
                print("Đã thoát chương trinh")
                break
            case _:
                print("Lựa chọn không hợp lệ")

main()