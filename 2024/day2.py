from utils import Input, get_input

data = get_input(year=2024, day=2, _input=Input.GIVEN)

data = data.splitlines()


# Condition 1
def all_asc_or_desc(report: list[int]) -> bool:
    sort_asc, sort_desc = sorted(report), sorted(report, reverse=True)
    return report in (sort_asc, sort_desc)


# Condition 2
def differ_min_1_max_3(report: list[int]) -> bool:
    acceptable_diffs = [1, 2, 3]
    left, right = 0, 1
    while right < len(report):
        abs_diff = abs(report[left] - report[right])
        if abs_diff not in acceptable_diffs:
            return False
        left += 1
        right += 1
    return True


def is_safe(report: list[int]):
    # Check for condition 1
    all_levels_asc_or_desc = all_asc_or_desc(report)

    # Check for condition 2
    levels_differ_min_1_max_3 = differ_min_1_max_3(report)

    return all_levels_asc_or_desc and levels_differ_min_1_max_3


num_safe_reports_p1, num_safe_reports_p2 = 0, 0
for report in data:
    report = report.split(" ")
    report = [int(level) for level in report]

    safe = is_safe(report)
    if safe:
        num_safe_reports_p1 += 1

    # Check for single level tolerance
    # Check with subsets of len(report) - 1 levels. This is the same as removing one bad level.
    # If even one of these subsets is safe, then the whole report can be considered safe.
    safe_with_problem_dampener = any(
        [is_safe(report[:idx] + report[idx + 1 :]) for idx in range(len(report))]
    )
    if safe_with_problem_dampener:
        num_safe_reports_p2 += 1


# Part 1
print(f"{num_safe_reports_p1=}")
# Part 2
print(f"{num_safe_reports_p2=}")
