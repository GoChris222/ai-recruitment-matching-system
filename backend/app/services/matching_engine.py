from app.services.scoring import calculate_suitability


def match_candidates_to_vacancy(vacancy, candidates):
    matches = []

    for candidate in candidates:
        suitability = calculate_suitability(candidate, vacancy)

        matches.append({
            "candidate_id": candidate.id,
            "candidate_name": candidate.name,
            "suitability_score": suitability
        })

    matches.sort(
        key=lambda x: x["suitability_score"],
        reverse=True
    )

    return matches
