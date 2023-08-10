BOX_BALLS_LIMIT = 5

accepted_balls = 0
returned_balls = 0

light_balls_difference_total = 0
light_balls_difference_ratio = 0

heavy_balls_difference_total = 0
heavy_balls_difference_ratio = 0

total_boxes = 0

normal_boxes = 0
defected_boxes = 0

heavy_boxes = 0
equal_boxes = 0
light_boxes = 0

most_equal_box_balls_count = 0
most_equal_box_ball_weight = 0

most_equal_heavy_box_balls_count = 0
most_equal_heavy_box_ball_weight = 0

most_different_box_ball_value = 0
most_different_box_ball_ratio = 0
most_different_box_ball_sign = ""

least_different_box_ball_value = 0
least_different_box_ball_ratio = 100.0
least_different_box_ball_sign = ""

process = "Y"

while process.upper() == "Y":
    number_of_balls = 0

    while number_of_balls < BOX_BALLS_LIMIT:
        number_of_balls = int(input("Enter the number of balls: "))
        if number_of_balls < BOX_BALLS_LIMIT:
            print("The number of balls cannot exceed box balls limit!")

    print()
    different_value_1, different_value_2, prev_value, current_value, diff_have_left, total_weight = 0, 0, 0, 0, 1, 0

    for i in range(number_of_balls):
        ball_weight = 0

        while ball_weight <= 0:
            ball_weight = int(input(f"Enter the {i + 1}. ball's weight (mg): "))
            if ball_weight <= 0:
                print("Ball weight must be positive!\n")

        current_value = ball_weight
        total_weight += ball_weight

        if i == 0:
            different_value_1 = current_value
            prev_value = current_value
            continue

        if diff_have_left == 1:
            if current_value == prev_value:
                if different_value_2 == 0:
                    different_value_2 = current_value

                elif different_value_1 != different_value_2:
                    temp = different_value_1
                    different_value_1 = different_value_2
                    different_value_2 = temp

                    diff_have_left = 0

            else:
                if different_value_2 == 0:
                    different_value_2 = current_value

                elif different_value_1 != different_value_2:
                    diff_have_left = -1 if current_value != different_value_1 and current_value != different_value_2 else 0

                else:
                    different_value_2 = current_value
                    diff_have_left = 0

        else:
            if current_value != different_value_1:
                diff_have_left = -1

        if diff_have_left == -1:
            print("Defected box, the weight of only 1 ball may be different from the others!\n")

            total_boxes += 1
            defected_boxes += 1
            returned_balls += number_of_balls

            break

        elif i == number_of_balls - 1:
            total_boxes += 1
            normal_boxes += 1
            accepted_balls += number_of_balls

            if different_value_1 < different_value_2:
                heavy_boxes += 1
                heavy_balls_difference_total += different_value_2 - different_value_1
                heavy_balls_difference_ratio += (different_value_2 - different_value_1) * 100 / different_value_1

            elif different_value_1 > different_value_2:
                light_boxes += 1
                light_balls_difference_total += different_value_1 - different_value_2
                light_balls_difference_ratio += (different_value_1 - different_value_2) * 100 / different_value_1

            else:
                equal_boxes += 1

            if number_of_balls > most_equal_box_balls_count:
                most_equal_box_balls_count = number_of_balls
                most_equal_box_ball_weight = ball_weight

            if total_weight > most_equal_heavy_box_ball_weight:
                most_equal_heavy_box_ball_weight = different_value_1
                most_equal_heavy_box_balls_count = number_of_balls

            if different_value_1 != different_value_2:
                ball_sign = "heavier" if different_value_2 > different_value_1 else "lighter"

                largest_diff = abs(different_value_1 - different_value_2)

                if largest_diff > most_different_box_ball_value:
                    most_different_box_ball_value = largest_diff
                    most_different_box_ball_ratio = largest_diff * 100 / different_value_1

                    most_different_box_ball_sign = "heavier" if different_value_2 > different_value_1 else "lighter"

                print(f"The ball with a different weight is {ball_sign} "
                      f"than the others, difference is {largest_diff} mg "
                      f"and percentage is {largest_diff * 100 / different_value_1:.2f} %")

            else:
                print("The balls are all of equal weight. ")

            if different_value_1 != different_value_2:
                smallest_ratio = abs(different_value_1 - different_value_2) * 100 / different_value_1

                if smallest_ratio < least_different_box_ball_ratio:
                    least_different_box_ball_ratio = smallest_ratio
                    least_different_box_ball_value = abs(different_value_1 - different_value_2)

                    least_different_box_ball_sign = "heavier" if different_value_2 > different_value_1 else "lighter"

        else:
            prev_value = ball_weight

    process = input("\nDo you want to add more box (Y/N)?: ")

    while process.upper() != "Y" and process.upper() != "N":
        print("Invalid answer!\n")
        process = input("Do you want to add more box (Y/N)?: ")

print(f"\nNumber of boxes with manufacturing defects is {defected_boxes} and "
      f"percentage of all boxes is {defected_boxes * 100 / total_boxes:.2f} %. ")

print(f"\nNumber of returned balls is {returned_balls} and accepted balls number is {accepted_balls}. ")

print(f"\nNumber of boxes in which all balls are of equal weight is {equal_boxes} "
      f"and percentage is {equal_boxes * 100 / normal_boxes:.2f} %. ")
print(f"Number of boxes in which 1 ball is heavier than the others is {heavy_boxes} "
      f"and percentage is {heavy_boxes * 100 / normal_boxes:.2f} %. ")
print(f"Number of boxes in which 1 ball is lighter than the others is {light_boxes} "
      f"and percentage is {light_boxes * 100 / normal_boxes:.2f} %. ")

print(f"\nMeans of weight difference values of the heavier balls in boxes "
       f"where 1 ball is heavier than the others is {heavy_balls_difference_total / heavy_boxes:.2f} mg. ")
print(f"Averages of the weight difference percentages of the heavier balls in boxes where 1 ball is "
      f"heavier than the others is {heavy_balls_difference_ratio / heavy_boxes:.2f} %. ")

print(f"\nMeans of weight difference values of the lighter balls in boxes "
       f"where 1 ball is heavier than the others is {light_balls_difference_total / light_boxes:.2f} mg. ")
print(f"Averages of the weight difference percentages of the lighter balls in boxes where 1 ball is "
      f"heavier than the others is {light_balls_difference_ratio / light_boxes:.2f} %. ")

print(f"\nAmong the boxes in which all balls are of equal weight, "
       f"the number of balls in the box with the most number of balls is {most_equal_box_balls_count} "
       f"and the weight of 1 ball in that box is {most_equal_box_ball_weight} mg.")

print(f"\nAmong the boxes in which all balls are of equal weight, "
      f"the number of balls in the box with the heaviest balls is {most_equal_heavy_box_balls_count} "
      f"and the weight of 1 ball in that box is {most_equal_heavy_box_ball_weight} mg. ")

print(f"\nThe value of the weight difference where the difference between the weight of the "
      f"different ball and the weight of the other balls in the box is the largest is "
      f"{most_different_box_ball_value} mg ({most_different_box_ball_sign}) "
      f"and percentage is {most_different_box_ball_ratio:.2f} %. ")

print(f"\nThe value of the weight difference where the percentage of the difference "
      f"between the weight of the different ball and the weight of the other balls in the box is the smallest is "
      f"{least_different_box_ball_value} mg ({least_different_box_ball_sign}) "
      f"and percentage is {least_different_box_ball_ratio:.2f} %. ")
