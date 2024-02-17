def set_covering(
    states_needed: set[str], stations: dict[str, str]
) -> None | set[str]:
    final_stations: set[str] = set()
    while states_needed:
        best_station: str | None = None
        states_covered: set[str] = set()
        for station, states_for_stations in stations.items():
            covered = states_needed & states_for_stations
            if (
                len(covered) > len(states_covered)
                and station not in final_stations
            ):
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
            continue
        return None
    return final_stations


def main() -> None:
    states_needed: set[str] = set(
        ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
    )

    stations: dict[str, set[str]] = {}

    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    print(set_covering(states_needed, stations))


if __name__ == "__main__":
    main()
