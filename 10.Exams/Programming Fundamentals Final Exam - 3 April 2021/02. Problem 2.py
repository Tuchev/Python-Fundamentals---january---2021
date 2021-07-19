# import re
# n = int(input())
#
# pattern = r"\!(?P<command>[A-Z][a-z][a-z]+)\!\:\[(?P<message>[a-zA-Z]+)\]"
# matches = ""
# encrypted_message = []
#
# for _ in range(n):
#     text = input()
#     if not re.search(pattern, text):
#         print("The message is invalid")
#     else:
#         matches = re.finditer(pattern, text)
#         for match in matches:
#             object_dict = match.groupdict()
#             command = object_dict["command"]
#             message = object_dict["message"]
#             for el in message:
#                 encrypted_message.append(ord(el))
#             print(f"{command}: {*encrypted_message, sep = ' '})