import sys

get_line: iter = lambda: map(int, sys.stdin.readline().rstrip().split())
get_input: int = lambda: int(sys.stdin.readline())

N = get_input()
arr = {
    0: {'selected': 0, 'non_selected': 0, 'input': 0},
    1: {'selected': 0, 'non_selected': 0, 'input': 0},
    2: {'selected': 0, 'non_selected': 0, 'input': 0},
}
for i in range(3, N + 3):
    now = get_input()
    arr[i] = {
        'selected': max(
            arr[i - 1]['input'] + arr[i - 3]['selected'],
            arr[i - 2]['non_selected'],
            arr[i - 2]['selected']
        ) + now,
        'non_selected': max(
            arr[i - 1]['selected'],
            arr[i - 1]['non_selected']
        ),
        'input': now
    }

print(arr[N + 2]['selected'])
