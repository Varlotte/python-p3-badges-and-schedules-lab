def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    name_list= []
    for name in names:
        name_list.append(f"Hello, my name is {name}.")
    return name_list
    

def assign_rooms(names):
    room_list= []
    for index, name in enumerate(names):
        room_list.append(f"Hello, {name}! You'll be assigned to room {index+1}!")
    return room_list

def printer(names):
    for str in batch_badge_creator(names):
        print(str)
    for str in assign_rooms(names):
        print(str)    

