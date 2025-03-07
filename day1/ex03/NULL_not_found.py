def NULL_not_found(object: any)-> int:
    obj_type = type(object)
    if object is None:
        print(f"{obj_type.__name__} : {object} {type(object)}")
    elif type(object) == float:
        print(f"{obj_type.__name__} : {object} {type(object)}")
    elif type(object) == int:
        print(f"{obj_type.__name__} : {object} {type(object)}")
    elif object is Empty:
        print(f"{obj_type.__name__} : {object} {type(object)}")
    elif type(object) == bool:
        print(f"{obj_type.__name__} : {object} {type(object)}")
    else:
        print("Type not Found")
    return(1)

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
