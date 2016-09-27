def exercise(score):
    # 1
    if score < 50:
        evaluation = "Below Average"
    elif score < 70:
        evaluation = "Average"
    elif score < 90:
        evaluation = "Above average"
    else:
        evaluation = "Excellent"
        
    return evaluation

print(exercise(80))
