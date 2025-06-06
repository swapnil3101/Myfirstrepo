
def add_toffins(fun):
    def wrapper():
        print("before toffins added to your ice_cream")
        fun()
        print("after toffins added to your ice_cream")
    return wrapper()


@add_toffins
def get_ice_cream():
    print("Here is your icecream...Enjoy")

get_ice_cream()