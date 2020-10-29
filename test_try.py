# try...except...else...finally语句执行细节
def count_queue():
    try:
        print("I am" + "1")
        print("I am" + "2")
        print("I am" + 3)
        print("I am" + "4")
    except TypeError as e:
        print("I am Error")
        print("I am" + n)
    except:
        print("I am 31")
    finally:
        print("I am finally")
    print("I am 9999")
if __name__ == "__main__":
    count_queue()
    print("end")