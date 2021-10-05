# guest list
guest_list = ['hercules', 'wonder woman', 'batman', 'superman']

invitee1 = guest_list[0]
invitee2 = guest_list[1]
invitee3 = guest_list[2]
invitee4 = guest_list[3]

print(f"Hello, {invitee1.title()}, you are invited to dinner.")
print(f"Hello, {invitee2.title()}, you are invited to dinner.")
print(f"Hello, {invitee3.title()}, you are invited to dinner.")
print(f"Hello, {invitee4.title()}, you are invited to dinner.")

print(f"There are {len(guest_list)} guest invited for dinner.")

# changing guest list
print(f"Unfortunately, {invitee3.title()} can't make dinner.")

guest_list[3] = 'hulk'
invitee3 = guest_list[3]

print(f"\nHello, {invitee1.title()}, you are invited to dinner.")
print(f"Hello, {invitee2.title()}, you are invited to dinner.")
print(f"Hello, {invitee3.title()}, you are invited to dinner.")
print(f"Hello, {invitee4.title()}, you are invited to dinner.")

# more guests
print("\nI've found us a bigger dinner table!")

guest_list.insert(0, 'betty baker')
guest_list.insert(2, 'clarke gable')
guest_list.append('harry styles')

print(f"\n{guest_list[0].title()}, you are also invited.")
print(f"{guest_list[2].title()}, you are also invited.")
print(f"{guest_list[-1].title()}, you are also invited.")

# shrinking guest list
print("\n\nOh no! The new table won't arrive in time.  Only space for 2 guests.")
popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, but I can't invite you to dinner!")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, but I can't invite you to dinner!")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, but I can't invite you to dinner!")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, but I can't invite you to dinner!")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, but I can't invite you to dinner!")

print(f"\n\nSo, {guest_list[0].title()}, you are still invited to dinner.")
print(f"So, {guest_list[1].title()}, you are still invited to dinner.")

del guest_list[:]
print(guest_list)