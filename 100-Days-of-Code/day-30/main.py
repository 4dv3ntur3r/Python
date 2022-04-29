# Error handling
# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asfdafa"])
    # if there is no specific error defined in the except it will be forgotten

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"They key {error_message} doen not exist.")
else:
    # When all the errors are dealt with this code section will run
    content = file.read()
    print(content)
finally:
    # This block will run no matter what will happen
    file.close()

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meter.")

bmi = weight / height ** 2
print(bmi)
