# treasure_chest = input().split("|")
# command_data = input()
# is_Empty = False
# stolen_elements = []
# rest_elements = []
#
# while not command_data == "Yohoho!":
#     command_data = command_data.split()
#
#     if command_data[0] == "Loot":
#         for el in range(0, len(command_data)):
#             if el == 0:
#                 continue
#             elif command_data[el] in treasure_chest:
#                 continue
#             else:
#                 treasure_chest.insert(0, command_data[el])
#
#     elif command_data[0] == "Drop":
#         index = int(command_data[1])
#         if index in range(len(treasure_chest)):
#             item = treasure_chest[index]
#             treasure_chest.remove(item)
#             treasure_chest.append(item)
#
#     elif command_data[0] == "Steal":
#         number_el_to_remove = int(command_data[1])
#         if len(treasure_chest) > number_el_to_remove:
#             stolen_elements = treasure_chest[len(treasure_chest)-number_el_to_remove::]
#             rest_elements = treasure_chest[:len(treasure_chest)-number_el_to_remove]
#             print(", ".join(stolen_elements))
#         else:
#             print(", ".join(treasure_chest))
#             treasure_chest.clear()
#             is_Empty = True
#
#     command_data = input()
#
# if is_Empty:
#     print("Failed treasure hunt.")
# else:
#     average_treasure_gain = 0
#     for el in range(len(rest_elements)):
#         average_treasure_gain += len(rest_elements[el])
#     print(f"Average treasure gain: {(average_treasure_gain / len(rest_elements)):.2f} pirate credits.")