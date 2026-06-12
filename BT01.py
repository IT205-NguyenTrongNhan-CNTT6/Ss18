


def menu():
    print("="*30)
    print("Quản Lý Đơn Hàng - Agent Order")
    print("="*30)
    print("1.Xem danh sách đơn hàng hiện có\n"+
          "2.Tạo mới đơn hàng đại lý\n"+
          "3.Cập nhật trạng thái thanh toán\n"+
          "4.Tính tổng doanh thu & chiếu khấu\n"+
          "5.Thoát chương trình")
    
def get_validate_input(prompt:str, input_type: str = "str"):
    while True:
        
            user_input = input(prompt)
            if not user_input:
                print("Dữ liệu không được trống")
                continue
            try:
                if user_input == "int":
                    value = int(user_input)
                    if value < 0 :
                        print("Dữ liệu không là số âm")
                        continue 
                    return value
            except ValueError:
                print("Dữ liệu không hợp lệ")
                continue
            return user_input     

def show_order(orders):
    if not orders:
        print("Danh sách rỗng")
        return
    print(f"{"Mã Đơn":<10}| {"Tên Đại Lý":<30}| {"Giá Trị":<15}| {"Trạng Thái":<15}")
    for item in orders:
        print(f"{item.get('id'):<10}| {item.get('name'):<30}| {item.get('price'):15}| {item.get('status',"Unpaid"):<15}")

def add_order(orders):
    if not orders:
        print("Danh sách rỗng")
        return
    print("-----Tạo Mới Đơn Hàng-----")
    while True:
        
        add_id = get_validate_input("Nhập mã đơn hàng: ")
        for order in orders:
           if (add_id.lower() == order.get("id").lower()):
               print("LỖI: Đã trùng id hãy nhập lại")
               break 
        else: 
            add_name = get_validate_input("Nhập tên đại lý: ")
            add_price = get_validate_input("Nhập giá trị đơn hàng: ","int")

            new_order = {
                "id": add_id,
                "name": add_name,
                "price": add_price
            }
            orders.append(new_order)
            print(f"Đã thêm {add_id} thành công")
            break

def upd_order(orders):
    if not orders:
        print("Danh sách rỗng")
        return 
    print("---Cập Nhật Trạng Thái Thanh Toán---")
    while True: 
        upd_id = get_validate_input("Nhập mã đơn hàng: ")
        for order in orders: 
            if (upd_id.lower() == order.get("id").lower() and order.get("status") == "Paid"):
                print("Đơn hàng này đã được thanh toán trước đó [Err-04]")
                return
            elif(upd_id.lower() == order.get("id").lower()):
                print(f"Đã tìm thấy đơn hàng {order.get("name")} (Giá trị: {order.get("price")})")
                order['status'] = "Paid"
                print("Đã cập nhật trạng thái")
                return
        else: 
            print("Không tìm thấy đơn hàng nào cả [Err-03]")

def revenue(orders):
    total = 0 
    rate_dis = 0 
    for order in orders: 
        if order.get("status") == "Paid" and order.get("price") >= 40000000:
            rate_dis = 0.5
            total += order.get("price")
        elif order.get("status") == "Paid" and order.get("price") < 20000000:
            rate_dis = 0
            total += order.get("price")
    discount = total * rate_dis
    print("---Báo Cáo Danh Thu---")
    print(f"Tổng danh thu thực tế đã thanh toán: {total}")
    print(f"Sô tiền chiết khấu đại lý nhận lại: {discount}")
    


def main():
    orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]
    while True:
        menu()
        choice = get_validate_input("Nhập vào lựa chọn của bạn: ")
        match choice: 
            case '1':
                show_order(orders)
            case '2':
                add_order(orders)
            case '3':
                upd_order(orders)
            case '4':
                revenue(orders)
            case '5':
                print("Đã thoát chương trình")
                break
            case _:
                print("Dữ liệu không hợp lệ")

main()