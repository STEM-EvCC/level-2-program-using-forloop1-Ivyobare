mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = 0
for mission in mission_names:
    total_missions += 1
# Print the total number of missions
print("Total number of missions:", total_missions)


success = 0
for mission in mission_success:
    if mission:  # Check if the mission is successful (True)
        success += 1
print(f"Number of successful missions: {success}")      


success_rate = (success / total_missions) * 100

# Print the result
print(f"Success Rate: {success_rate:.2f}%")

missions_before_2000 = []


for year, name in zip(mission_years, mission_names):
    if year < 2000:
        missions_before_2000.append(f"{name} ({year})")

# Print the results
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(mission)
        

        
    