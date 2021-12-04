import os

# a = os.getcwd() + "/Result"
# os.chdir(a)
# print(os.getcwd())

# a = 'abcd '
# a = a.replace(" ", "-")
# print(a)

# info = f"- Basic Information about Technology -\n" + "-"*37
# print(info)

os.chdir('E:\Data-web-technologies\Result')
check_file = str(os.listdir())
if "163" in check_file:
    print(True)