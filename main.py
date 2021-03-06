from week0.matrix import test_matrices
from week0.ship import ship
from week0.swap import test_swappers
from week1.listAndLoops import for_loop, while_loop, recursive_loop
from week1.fibonacci import fibonacci
from week1.recurFactorial import tester
from week2.classFactorial import factorialll
from week2.factors import factorsTester
from week2.primes import primesTester


main_menu = []

math_sub_menu = [
    ["Fibonacci", fibonacci],
    ["Recur Factorial", tester],
    ["Class Factorial", factorialll],
    ["Primes Finder", primesTester],
    ["Factors Finder", factorsTester],
    ["Ship", ship],
]

display_sub_menu = [
    ["Matrix", test_matrices],
    ["Swap", test_swappers],
    ["For Loop", for_loop],
    ["While Loop", while_loop],
    ["Recursive Loop", recursive_loop],
]

week3_sub_menu = [
    ["Icecream", "/Users/nadirahaddach/Saathvika-Ajith/week3/icecream.py"],
]

week2_sub_menu = [
    ["Class Factorial", factorialll],
    ["Factors Finder", factorsTester],
    ["Primes Finder", primesTester],
]

week1_sub_menu = [
    ["Fibonacci", fibonacci],
    ["Recur Factorial", tester],
    ["For Loop", for_loop],
    ["While Loop", while_loop],
    ["Recursive Loop", recursive_loop],
]

week0_sub_menu = [
    ["Ship", ship],
    ["Matrix", test_matrices],
    ["Swap", test_swappers],
]

# Menu banner is typically defined by menu owner
border = "\033[36m⊹ ⊱ ❖ ⊰ ⊹ ════════════════════\033[36m"
banner = f"\033[37m\n{border}\nPlease Select An Option\n{border}\033[37m"

# def menu/
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control

def menu():
    title = "Weekly Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["════ ══ ⊰ Categories:"])
    menu_list.append(["Math", math_submenu])
    menu_list.append(["Display", display_submenu])
    menu_list.append(["════ ══ ⊰ Weeks:"])
    menu_list.append(["Week 3", week3_submenu])
    menu_list.append(["Week 2", week2_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 0", week0_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def math_submenu():
    title = "Math Submenu" + banner
    buildMenu(title, math_sub_menu)

def display_submenu():
    title = "Display Submenu" + banner
    buildMenu(title, display_sub_menu)

def week3_submenu():
    title = "Week 3 Submenu" + banner
    buildMenu(title, week3_sub_menu)

def week2_submenu():
    title = "Week 2 Submenu" + banner
    buildMenu(title, week2_sub_menu)

def week1_submenu():
    title = "Week 1 Submenu" + banner
    buildMenu(title, week1_sub_menu)

def week0_submenu():
    title = "Week 0 Submenu" + banner
    buildMenu(title, week0_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '| ⇨ ', value[0])

    # get user choice
    choice = input("Type your choice ⊱ ")
    print()
    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    print()
    buildMenu(banner, options)  # recursion, start menu over again

if __name__ == "__main__":
    menu()
