"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""


def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    file = open(filepath,  "r")
    lines = file.readlines()[1:]
    list_of_dictionaries = []
    for i in lines:
        temp_list = []
        temp_list.append(i.split(sep=","))
        identification = int(temp_list[0][0])
        title = temp_list[0][1]
        description = temp_list[0][2]
        price = float(temp_list[0][3][1:])
        dictionary = {"id": identification, "title":title, "description":description, "price":price}
        list_of_dictionaries.append(dictionary)
    return list_of_dictionaries

def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!\nWe feed each according to their need.")


def display_cookies(cookies):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n\n")
    for cookie in cookies:
        # print(f"#{cookies[cookie]["id"]} - {cookies[cookie]["title"]}\n{cookies[cookie]["description"]}\nPrice: ${cookies[cookie]["price"]}")
        print("#{} - {}\n{}\nPrice: ${:.2f}".format(cookie["id"], cookie["title"] , cookie["description"] , cookie["price"]))

def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    cookie = cookies[int(id) - 1]
    return cookie

# print(get_cookie_from_dict(1, bake_cookies("data/cookies.csv")))

def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    cookie_type = get_cookie_from_dict(id, cookies)
    cookie_name = cookie_type["title"]
    quantity = 0
    invalid_response = True
    while invalid_response:
        response = input(f"My favorite! How many {cookie_name}s would you like? ").strip()
        if response.isnumeric() is True and int(response) >= 0:
            quantity = int(response)
            invalid_response = False
    subtotal = (quantity * float(cookie_type["price"]))
    print("Your subtotal for {} {} is ${:.2f}.".format(quantity, cookie_name, subtotal))
    return quantity


# solicit_quantity(1, bake_cookies("data/cookies.csv"))

def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    looping = True
    list_of_sub_orders = []
    exit_options = ["finished", "done", "quit", "exit"]
    while looping:
        response = input("What is the id of the cookie you want to order? ")
        if response in exit_options:
            looping = False
        elif response.isnumeric() is False or int(response) not in range(1,11):
            print({"Your id input is invalid. Try again."})
        else:
            quantity = solicit_quantity(response, cookies)
            sub_order = {"id": int(response), "quantity": quantity}
            list_of_sub_orders.append(sub_order)
    return list_of_sub_orders

# solicit_order(bake_cookies("data/cookies.csv"))




def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    print("Thank you for your order. You have ordered:\n")
    total = 0
    for sub_order in order:
        sub_order = dict(sub_order)
        quantity = sub_order["quantity"]
        cookie_type = get_cookie_from_dict(sub_order["id"], cookies)
        cookie_name = cookie_type["title"]
        print("-{} {}".format(quantity, cookie_name))
        subtotal = quantity * cookie_type["price"]
        total += subtotal
    print("\n\nYour total is ${:.2f}.\nPlease pay with Bitcoin before picking-up.\n\nThank you!\n-The Python Cookie Shop Robot.".format(total))

# display_order_total(solicit_order(bake_cookies("data/cookies.csv")), bake_cookies("data/cookies.csv"))



def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)

run_shop(bake_cookies("data/cookies.csv"))