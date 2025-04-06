import json

new = True
order = []


def add():
    global new
    id = (input("請輸入訂單編號：")).upper()

    if not new:
        with open('orders.json', 'r', encoding='UTF-8') as f:
            load_json = json.load(f)
            for i in load_json:
                if id == i["order_id"]:
                    print("=> 錯誤：訂單編號 "+id+" 已存在！")
                    return 0

    new = False
    with open('orders.json', 'w', encoding='UTF-8') as f:
        customer = input("請輸入顧客姓名：")
        items = []
        have = False

        while True:
            name = None
            price = None
            quantity = None
            dict1 = {"order_id": '', "customer": '', "items": ''}
            dict2 = {"name": '', "price": '', "quantity": ''}

            name = input("請輸入訂單項目名稱（輸入空白結束）：")
            if name == "" and not have:
                print("=> 至少需要一個訂單項目")
            elif name == "" and have:
                dict1["order_id"] = id
                dict1["customer"] = customer
                dict1["items"] = items
                order.append(dict1)
                json.dump(order, f, ensure_ascii=False, indent=4)
                print("=> 訂單 "+id+" 已新增！")
                break
            else:
                have = True
                while True:
                    price = ""
                    price = input("請輸入價格：")
                    if price.isdigit():
                        break
                    elif price[0] == "-" and price[1:].isdigit():
                        print("=> 錯誤：價格不能為負數，請重新輸入")
                    else:
                        print("=> 錯誤：價格或數量必須為整數，請重新輸入")

                while True:
                    quantity = None
                    quantity = input("請輸入數量：")

                    if quantity == '0' or (quantity[0] == "-" and
                                           quantity[1:].isdigit()):
                        print("=> 錯誤：數量必須為正整數，請重新輸入")
                    elif quantity.isdigit():
                        break
                    else:
                        print("=> 錯誤：價格或數量必須為整數，請重新輸入")
                dict2["name"] = name
                dict2["price"] = (int)(price)
                dict2["quantity"] = (int)(quantity)
                items.append(dict2)


def show():
    print("\n==================== 訂單報表 ====================")
    o = 0
    with open('orders.json', 'r', encoding='UTF-8') as f:
        load_json = json.load(f)
        for i in load_json:
            price = 0
            o += 1
            print(f"訂單 #{o}\n訂單編號: {i["order_id"]}\n客戶姓名: {i["customer"]}")
            print("--------------------------------------------------")
            print(f"商品名稱{'':　<1}單價{'':　<3}數量{'':　<3}小計{'':　<3}")
            print("--------------------------------------------------")
            for j in i["items"]:
                print(f"{j["name"]:　<5}{j["price"]: <10,}{j["quantity"]: <10,}\
{j["price"]*j["quantity"]: <10,}")
                price += j["price"]*j["quantity"]
            print("--------------------------------------------------")
            print(f"訂單總額: {price:,}")
            print("==================================================\n")


def meal():
    with open('orders.json', 'r', encoding='UTF-8') as f:
        load_json = json.load(f)
        o = 0
        menu = None

        for i in load_json:
            o += 1
            print(str(o)+". 訂單編號: "+str(i["order_id"])+" - 客戶: " +
                  str(i["customer"]))
        print("================================")

        while True:
            menu = input("請選擇要出餐的訂單編號 (輸入數字或按 Enter 取消):")
            if menu == "":
                return 0
            elif menu.isdigit():
                menu = int(menu)-1
                break
            else:
                print("=> 錯誤：請輸入有效的數字")

        with open('output_orders.json', 'w', encoding='UTF-8') as g:
            json.dump(load_json[menu], g, ensure_ascii=False, indent=4)
        print("=> 訂單 "+str(load_json[menu]["order_id"])+" 已出餐完成\n出餐訂單詳細資料：")

        price = 0
        print("\n==================== 出餐訂單 ====================")
        print("訂單編號: "+load_json[menu]["order_id"])
        print("客戶姓名: "+load_json[menu]["customer"])
        print("--------------------------------------------------")
        print(f"商品名稱{'':　<1}單價{'':　<3}數量{'':　<3}小計{'':　<3}")
        print("--------------------------------------------------")
        for j in load_json[menu]["items"]:
            print(f"{j["name"]:　<5}{j["price"]: <10,}{j["quantity"]: <10,}\
{j["price"]*j["quantity"]: <10,}")
            price += j["price"]*j["quantity"]
        print("--------------------------------------------------")
        print(f"訂單總額: {price:,}")
        print("==================================================\n")

    with open('orders.json', 'w', encoding='UTF-8') as f:
        load_json.pop(menu)
        json.dump(load_json, f, ensure_ascii=False, indent=4)


with open('orders.json', 'w', encoding='UTF-8') as f:
    f.close()

while True:
    print("***************選單***************\n1. 新增訂單\n2. 顯示訂單報表\n3. 出餐處理\n\
4. 離開\n**********************************")
    menu = input("請選擇操作項目(Enter 離開)：")
    if menu == '1':
        add()
    elif menu == '2':
        show()
    elif menu == '3':
        meal()
    elif menu == '4':
        break
    else:
        print("=> 請輸入有效的選項（1-4）")
