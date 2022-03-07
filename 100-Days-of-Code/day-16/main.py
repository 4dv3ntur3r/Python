# import another_module
# print(another_module.another_varible)
#
# from turtle import Turtle, Screen
#
# tammy = Turtle()
# print(tammy)
# tammy.shape("turtle")
# tammy.color("Cyan", "Green")
# tammy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squiretel", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"
print(table)