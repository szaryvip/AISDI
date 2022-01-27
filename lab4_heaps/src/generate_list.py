from random import randint


def generate_list():
    mylist = []
    for i in range(100000):
        mylist.append(randint(1, 300000))
    return mylist


def save_list_to_csv(path, mylist):
    with open(path, 'w') as file:
        file.write(str(mylist))


if __name__ == "__main__":
    mylist = generate_list()
    save_list_to_csv('src/random_list.txt', mylist)
