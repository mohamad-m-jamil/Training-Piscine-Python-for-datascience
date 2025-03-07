def all_thing_is_obj(object: any)-> int:
    obj_type = type(object)
    if  type(object) == list:
        print(f"{obj_type.__name__}: {type(object)}")
    elif type(object) == tuple:
        print(f"{obj_type.__name__}: {type(object)}")
    elif type(object) == set:
        print(f"{obj_type.__name__}: {type(object)}")
    elif type(object) == dict:
        print(f"{obj_type.__name__}: {type(object)}")
    elif type(object) == str:
        print(f"{object} is in the kitchen : {type(object)}")
    else :
        print("Type not found")
    return(42)
