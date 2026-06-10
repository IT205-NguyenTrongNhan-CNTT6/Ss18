def get_validate_input(prompt: str, input_type: str = "string"):
    while True:
        user_input = input(prompt)

        if not user_input:
            print("Dữ liệu không được để trống!")
            continue

        if input_type == "int":
            try:
                value = int(user_input)

                if value < 0:
                    print("Dữ liệu phải là số nguyên dương!")
                    continue

                return value

            except ValueError:
                print("Dữ liệu không hợp lệ, nhập lại!")
                continue

        return user_input


def show_inventory(inventory):
    if not inventory:
        print("Danh sách tồn kho rỗng!")
        return

    print("\n----- DANH SÁCH TỒN KHO -----")
    print(f"{'ID':<10}| {'Tên Hàng Hóa':<20}| {'Số lượng tồn':<15}")

    for item in inventory:
        print(
            f"{item.get('id'):<10}| "
            f"{item.get('name'):<20}| "
            f"{item.get('quantity'):<15}"
        )


def add_item(inventory):
    while True:
        print("\n--- NHẬP HÀNG HÓA MỚI ---")

        add_id = get_validate_input("Nhập mã hàng hóa: ")

        for item in inventory:
            if add_id.lower() == item.get("id").lower():
                print("Mã hàng hóa đã tồn tại!")
                break
        else:
            add_name = get_validate_input("Nhập tên hàng hóa: ")
            add_quantity = get_validate_input(
                "Nhập số lượng tồn kho: ", "int"
            )

            new_item = {
                "id": add_id,
                "name": add_name,
                "quantity": add_quantity
            }

            inventory.append(new_item)

            print("Đã thêm hàng hóa thành công!")
            break


def upd_inventory(inventory):
    print("\n--- CẬP NHẬT SỐ LƯỢNG TỒN KHO ---")

    upd_id = get_validate_input("Nhập mã hàng hóa: ")

    for item in inventory:
        if upd_id.lower() == item.get("id").lower():

            print(
                f"Tìm thấy hàng hóa: {item.get('name')} "
                f"(Số lượng hiện tại: {item.get('quantity')})"
            )

            upd_quantity = get_validate_input(
                "Nhập số lượng mới: ", "int"
            )

            item["quantity"] = upd_quantity

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy hàng hóa!")


def menu():
    print("\n" + "=" * 35)
    print("QUẢN LÝ KHO HÀNG - GROCERY STORE")
    print("=" * 35)

    print("1. Xem danh sách hàng tồn kho\n"+
          "2. Nhập thêm hàng hóa mới\n"+
          "3. Cập nhật số lượng tồn kho theo ID\n"+
          "4. Thoát")


def main():
    inventory = [
        {
            'id': 'G01',
            'name': 'Gạo tẻ',
            'quantity': 50
        },
        {
            'id': 'G02',
            'name': 'Mì tôm',
            'quantity': 120
        }
    ]

    while True:
        menu()

        choice = get_validate_input(
            "Nhập lựa chọn của bạn: "
        )

        match choice:
            case '1':
                show_inventory(inventory)

            case '2':
                add_item(inventory)

            case '3':
                upd_inventory(inventory)

            case '4':
                print("Đã thoát chương trình!")
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()