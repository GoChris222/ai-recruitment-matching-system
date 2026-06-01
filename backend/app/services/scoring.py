from dateutil.parser import parse


def date_ranges_overlap(start_1, end_1, start_2, end_2):
    s1 = parse(start_1).date()
    e1 = parse(end_1).date()
    s2 = parse(start_2).date()
    e2 = parse(end_2).date()

    return max(s1, s2) <= min(e1, e2)


def score_availability(candidate, vacancy):
    for window in candidate.availability:
        if date_ranges_overlap(
            window.start_date,
            window.end_date,
            vacancy.start_date,
            vacancy.end_date
        ):
            return 1.0

    return 0.0


def score_location(candidate, vacancy):
    if vacancy.state in candidate.avoided_states:
        return 0.0

    if vacancy.location in candidate.preferred_locations:
        return 1.0

    if vacancy.state in candidate.preferred_states:
        return 0.8

    return 0.5


def score_skills(candidate, vacancy):
    if not vacancy.skills_required:
        return 1.0

    matched = set(candidate.skills).intersection(
        set(vacancy.skills_required)
    )

    return len(matched) / len(vacancy.skills_required)


def calculate_suitability(candidate, vacancy):
    score = (
        score_availability(candidate, vacancy) * 40
        + score_location(candidate, vacancy) * 30
        + score_skills(candidate, vacancy) * 30
    )

    return round(score)
