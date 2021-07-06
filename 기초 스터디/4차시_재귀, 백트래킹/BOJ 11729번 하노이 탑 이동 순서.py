import sys

N = int(sys.stdin.readline().rstrip())

print(2 ** N - 1)


def move_disk(disk_num, start_peg, end_peg):
    print(f"{start_peg} {end_peg}")


def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)

    mid_peg = (6 - start_peg - end_peg)

    hanoi(num_disks - 1, start_peg, mid_peg)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, mid_peg, end_peg)


hanoi(N, 1, 3)