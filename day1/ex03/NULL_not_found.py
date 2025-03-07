def NULL_not_found(object: any)-> int:
    obj_type = type(object)
    if object is None:
        print(f"Nothing : {object} {type(object)}")
    elif type(object) == float:
        print(f"Cheese : {object} {type(object)}")
    elif type(object) == int:
        print(f"Zero : {object} {type(object)}")
    elif type(object) == str and object == "":
        print(f"Empty : {object} {type(object)}")
    elif type(object) == bool:
        print(f"Fake : {object} {type(object)}")
    else:
        print("Type not Found")
    return(1)

