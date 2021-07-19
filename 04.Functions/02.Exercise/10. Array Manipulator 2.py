def exchange(data: list, idx: int):
    if 0 <= idx < len(data):
        return data[idx + 1:] + data[:idx + 1]

    print('Invalid index')
    return data


def max_min(com: str, type: str, data: list):
    filtered_numbers = []

    if type == 'odd':
        filtered_numbers = list(filter(lambda x: x % 2 == 1, data))

    elif type == 'even':
        filtered_numbers = list(filter(lambda x: x % 2 == 0, data))

    if len(filtered_numbers) == 0:
        return 'No matches'

    if com == 'max':
        for idx in range(len(data) - 1, -1, -1):
            if data[idx] == max(filtered_numbers):
                return idx

    elif com == 'min':
        for idx in range(len(data) - 1, -1, -1):
            if data[idx] == min(filtered_numbers):
                return idx


def first_last(comm: str, cnt: int, type: str, data: list):
    if cnt > len(data):
        return 'Invalid count'

    filtered_numbers = []

    if type == 'odd':
        filtered_numbers = list(filter(lambda x: x % 2 == 1, data))

    elif type == 'even':
        filtered_numbers = list(filter(lambda x: x % 2 == 0, data))

    if len(filtered_numbers) == 0:
        return []

    if cnt > len(filtered_numbers):
        cnt = len(filtered_numbers)

    if comm == 'first':
        return [filtered_numbers[idx] for idx in range(cnt)]

    elif comm == 'last':
        return list(reversed([filtered_numbers[idx] for idx in range(cnt - 1, -1, -1)]))


data = list(map(int, input().split()))
command = input()

while command != 'end':

    if 'exchange' in command:
        command, idx = command.split()
        idx = int(idx)
        data = exchange(data, idx)

    elif 'max' in command or 'min' in command:
        command, num_type = command.split()
        print(max_min(command, num_type, data))

    elif 'first' in command or 'last' in command:
        command, count, num_type = command.split()
        count = int(count)
        print(first_last(command, count, num_type, data))

    command = input()

print(data)