a_file = open("test.txt", mode="w")
try:
    a_file.write("나는 실패해본 적이 없다.\n")
    a_file.write("1만 가지의 방법을 찾아냈을 뿐이다.\n")
finally:
    a_file.close()

