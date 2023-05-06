def move_disk(from_peg, to_peg):
    print("Move disk from peg", from_peg, "to peg", to_peg)

def dfs_simulation(n, start_peg, aux_peg, end_peg):
    stack = [(n, start_peg, aux_peg, end_peg)]

    while stack:
        num_disks, from_peg, temp_peg, to_peg = stack.pop()

        if num_disks == 1:
            move_disk(from_peg, to_peg)
        else:
            stack.append((num_disks-1, from_peg, to_peg, temp_peg))
            stack.append((1, from_peg, temp_peg, to_peg))
            stack.append((num_disks-1, temp_peg, from_peg, to_peg))

# Sample usage
n = 3
start_peg = 1
aux_peg = 2
end_peg = 3
dfs_simulation(n, start_peg, aux_peg, end_peg)