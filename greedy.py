
def find_stations(stations, states):
    result = set()
    states_covered = set()

    while True:
        # Find the station that covers the most un-covered states
        most_new = 0
        most_new_station = None

        for station, station_states in stations.items():
            if station in result: continue # Don't process already picked stations

            valid_states = station_states.intersection(states) # Only add states that were asked for
            difference = valid_states.difference(states_covered) # New states from this station
            if len(difference) > most_new:
                most_new = len(difference) # Update the max
                most_new_station = station
        
        # Add that station to the result
        if most_new_station:
            result.add(most_new_station)
            states_covered = states_covered.union(stations[most_new_station])
        # If not all states covered and we didn't find a station that covers something new
        elif (len(states_covered) < len(states)):
            return None
        # We're done looking
        else:
            break

    return result


def test_stations():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut",
        "ca", "az"])

    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    print(find_stations(stations, states_needed))


if __name__ == "__main__":
    test_stations()