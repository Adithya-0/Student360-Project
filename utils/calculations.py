def average(values):
    return sum(values) / len(values) if values else 0


def weighted_average(items, value_key="marks", weight_key="credits"):
    total_weight = sum(item[weight_key] for item in items)
    if total_weight == 0:
        return 0
    return sum(item[value_key] * item[weight_key] for item in items) / total_weight


def percentage_change(old, new):
    if old == 0:
        return 0
    return ((new - old) / old) * 100
