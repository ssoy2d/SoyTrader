def calculate_ai_score(stock):

    score = 50

    # 등락률
    if stock["change"] > 3:
        score += 15
    elif stock["change"] > 1:
        score += 10
    elif stock["change"] < -3:
        score -= 15
    elif stock["change"] < -1:
        score -= 8

    # 거래량
    if stock["volume"] > 5_000_000:
        score += 10
    elif stock["volume"] > 1_000_000:
        score += 5

    score = max(0, min(score, 100))

    return score