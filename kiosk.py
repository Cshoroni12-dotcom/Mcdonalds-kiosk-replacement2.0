#hello! so this is the second (personal) and the first project that i made in my academy
#translated to english at mar 24 11:01 pm
priceList = {'Bulgogi Burger': 3200, 'Shrimp Burger': 4000, 'Cheese Burger': 2800,
             'Sprite': 1500, 'Milk': 1200, 'Cola': 1500}

burgerCount = 0
drinkCount = 0   

def setMenu():
    global burgerCount, drinkCount
    return min(burgerCount, drinkCount)

totalPrice = 0


burgers = ['Bulgogi Burger', 'Shrimp Burger', 'Cheese Burger']
drinks = ['Sprite', 'Milk', 'Cola']
orderList = {}

print('D.Burger Self Order System')
sumon = 0

while True:
    orderType = int(input('Enter menu type (Burger:1/Drink:2/Exit:3): '))
 
    if orderType == 1:
        burger = input("Add burger:")
        if burger not in burgers:
            print("Menu not available.")
        else:
            num1 = int(input("Quantity:"))
            orderList[burger] = orderList.get(burger, 0) + num1
            burgerCount += num1
            sumon += priceList[burger] * num1
            print(f"{burger} added")
            print(f"Current cart: {orderList}")

    elif orderType == 2:
        drink = input("Add drink:")
        if drink not in drinks:
            print("Menu not available.")
        else:
            num2 = int(input("Quantity:"))
            orderList[drink] = orderList.get(drink, 0) + num2
            drinkCount += num2
            sumon += priceList[drink] * num2
            print(f"{drink} added")
            print(f"Current cart: {orderList}")

    elif orderType == 3:
        print("-------------------------")
        print("Order finished.")
        print("Check your order and total price.")
        print(f"Order details: {orderList}")

        if sumon >= 15000:
            print("You get cheese sticks!")
            orderList['Cheese Sticks'] = 1

        dc = setMenu()
        discount = dc * 500
        sumon -= discount

        print(f"Set discount: {discount}")
        print(f"Total price: {sumon} won")

        name = input("Edit order: y / Finalize order: n: ")

        if name == 'n':
            break

        elif name == 'y':
            what_broke = input("Enter item to cancel: ")

            if what_broke not in orderList:
                print("Item not found.")
            else:
                how_broke = int(input("Enter quantity to cancel: "))

                orderList[what_broke] -= how_broke
                sumon -= priceList[what_broke] * how_broke

                if what_broke in burgers:
                    burgerCount -= how_broke
                elif what_broke in drinks:
                    drinkCount -= how_broke

                if orderList[what_broke] <= 0:
                    del orderList[what_broke]

                print(f"{how_broke} of {what_broke} cancelled.")
                print("Check your order and total price.")
                print(f"Order details: {orderList}")
                print(f"Set discount: {discount}")
                print(f"Total price: {sumon} won")

    else:
        print("Please enter again.")
