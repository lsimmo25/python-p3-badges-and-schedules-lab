def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges

def assign_rooms(names):
    room_assignments = []
    room_number = 1
    for name in names:
        if room_number <= 8:
            message = f"Hello, {name}! You'll be assigned to room {room_number}!"
            room_assignments.append(message)
            room_number += 1
        else:
            break
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)
    for room in room_assignments:
        print(room)
    
