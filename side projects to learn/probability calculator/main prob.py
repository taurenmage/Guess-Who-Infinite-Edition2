import probability_calculator

hat = probability_calculator.Hat(blue=4, red=2, green=6)
hat.draw(3)

probability = probability_calculator.experiment(
    hat = hat,
    expected_balls = {"blue": 2,
                      "red": 1},
    num_balls_drawn = 4,
    num_experiments = 3000)

print("Probability:", probability)






