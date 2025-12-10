import re
from ortools.sat.python import cp_model

def parse_line(line):
    lights_str = re.search(r'\[(.*?)\]', line).group(1)
    lights = [c == '#' for c in lights_str]

    button_groups = re.findall(r'\((.*?)\)', line)
    buttons = []
    for g in button_groups:
        nums = [int(x) for x in g.split(',')]
        if len(nums) == 1:
            buttons.append((nums[0],))  # make 1-element tuple
        else:
            buttons.append(tuple(nums))

    joltage_str = re.search(r'\{(.*?)\}', line).group(1)
    joltage = tuple([int(x) for x in joltage_str.split(',')])

    return {
        "lights": lights,
        "buttons": buttons,
        "joltage": joltage
    }

def read_input(path):
    with open(path, 'r') as f:
        raw = f.readlines()

    data = []
    for row in raw:
        row = row.strip()
        data.append(parse_line(row))

    return data


def ex1(machines):
    total = 0
    for machine in machines:
        target = machine["lights"]
        tree = {0: [[False for _ in range(len(machine["lights"]))]]}
        next_step = 0
        while True:
            current_step = next_step
            next_step = current_step + 1
            tree[next_step] = []
            for button in machine["buttons"]:
                for state in tree[current_step]:
                    temp_state = state.copy()
                    for toggle in button:
                        temp_state[toggle] = not temp_state[toggle]
                    tree[next_step].append(temp_state)
            if target in tree[next_step]:
                total += next_step
                break

    return total


def ex2(machines):
    total_presses = 0

    for idx, machine in enumerate(machines):
        model = cp_model.CpModel()

        target = machine["joltage"]
        buttons = machine["buttons"]

        num_buttons = len(buttons)
        num_capacitors = len(target)
        max_target = max(target)
        button_vars = []
        for i in range(num_buttons):
            button_vars.append(model.NewIntVar(0, max_target, f'btn_{i}'))

        for capacitor_idx in range(num_capacitors):
            affected_by = []
            for btn_idx, btn_affects in enumerate(buttons):
                if capacitor_idx in btn_affects:
                    affected_by.append(button_vars[btn_idx])

            model.Add(sum(affected_by) == target[capacitor_idx])

        model.Minimize(sum(button_vars))
        solver = cp_model.CpSolver()
        solver.Solve(model)

        total_presses += int(solver.ObjectiveValue())

    return total_presses

if __name__ == "__main__":
    machines = read_input("input1.txt")
    print(f"Ex1: {ex1(machines)}")
    print(f"Ex2: {ex2(machines)}")