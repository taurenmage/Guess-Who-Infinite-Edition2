import probability_calculator




# lottery parameters

total_ping_pong_balls = 1000
initial_lottery_case = []
final_lottery_case = []


detroit = {
    "Name": "Detroit Pistons",
    "Ping-pong balls": int(0.14 * total_ping_pong_balls)
}
charlotte = {
    "Name": "Charlotte Hornets",
    "Ping-pong balls": int(0.14 * total_ping_pong_balls)
}
houston = {
    "Name": "Houston Rockets",
    "Ping-pong balls": int(0.14 * total_ping_pong_balls)
}
san_antonio = {
    "Name": "San Antonio Spurs",
    "Ping-pong balls": int(0.125 * total_ping_pong_balls)
}
washington = {
    "Name": "Washington Wizards",
    "Ping-pong balls": int(0.105 * total_ping_pong_balls)
}
orlando = {
    "Name": "Orlando Magic",
    "Ping-pong balls": int(0.09 * total_ping_pong_balls)
}
la_lakers = {
    "Name": "Los Angeles Lakers",
    "Ping-pong balls": int(0.075 * total_ping_pong_balls)
}
oklahoma_city = {
    "Name": "Oklahoma City Thunder",
    "Ping-pong balls": int(0.06 * total_ping_pong_balls)
}
chicago = {
    "Name": "Chicago Bulls",
    "Ping-pong balls": int(0.045 * total_ping_pong_balls)
}
toronto = {
    "Name": "Toronto Raptors",
    "Ping-pong balls": int(0.03 * total_ping_pong_balls)
}
minnesota = {
    "Name": "Minnesota Timberwolves",
    "Ping-pong balls": int(0.02 * total_ping_pong_balls)
}
golden_state = {
    "Name": "Golden State Warriors",
    "Ping-pong balls": int(0.015 * total_ping_pong_balls)
}
miami = {
    "Name": "Miami Heat",
    "Ping-pong balls": int(0.01 * total_ping_pong_balls)
}
utah = {
    "Name": "Utah Jazz",
    "Ping-pong balls": int(0.005 * total_ping_pong_balls)
}

all_teams_list = [detroit, charlotte, houston, san_antonio, washington, orlando, la_lakers, oklahoma_city, chicago, toronto, minnesota, golden_state, miami, utah]


hat = probability_calculator.Hat(detroit=detroit["Ping-pong balls"], charlotte=charlotte["Ping-pong balls"], houston=houston["Ping-pong balls"], san_antonio=san_antonio["Ping-pong balls"], washington=washington["Ping-pong balls"], orlando=orlando["Ping-pong balls"], la_lakers=la_lakers["Ping-pong balls"], oklahoma_city=oklahoma_city["Ping-pong balls"], chicago=chicago["Ping-pong balls"], toronto=toronto["Ping-pong balls"], minnesota=minnesota["Ping-pong balls"], golden_state=golden_state["Ping-pong balls"], miami=miami["Ping-pong balls"], utah=utah["Ping-pong balls"])

hat.draw(4)



