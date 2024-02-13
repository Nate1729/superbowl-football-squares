import csv
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Conference(str, Enum):
    AFC = "AFC"
    NFC = "NFC"
    AFL = "AFL"
    NFL = "NFL"

def transform_str_to_conference(s: str) -> Optional[Conference]:
    """Transform a string into a `Conference`. If the string
    isn't a valid conference, return `None`.
    """
    if s == Conference.AFC:
        return Conference.AFC

    elif s == Conference.NFC:
        return Conference.NFC

    elif s == Conference.AFL:
        return Conference.AFL

    elif s == Conference.NFL:
        return Conference.NFL
    else:
        return None

@dataclass
class Team:
    name: str
    conference: Conference
    box_score: list[int]

    @classmethod
    def from_csv(cls, data: list[str]):
        box_score = [int(d) for d in data[2:] if d != '']

        conference = transform_str_to_conference(
            data[1]
        )

        if conference is None:
            raise Exception(f"{data[1]} is an unknown Super Bowl Conference.")
        
        return cls(name=data[0],
                   conference=conference,
                   box_score=box_score
                )
    
    def is_afc(self) -> bool:
        return self.conference in [Conference.AFC, Conference.AFL]

def bubble_sort(data: list[tuple[int,int]]) -> list[tuple[int, int]]:
    restart = True
    while restart:
        restart=False
        for i in range(len(data)-1):
            left_bubble = data[i]
            right_bubble = data[i+1]
            if left_bubble[1] < right_bubble[1]:
                data[i] = right_bubble
                data[i+1] = left_bubble
                restart=True
    return data


def main() -> None:
    afc_counter: list[int] = [0 for _ in range(10)]
    nfc_counter: list[int] = [0 for _ in range(10)]

    for sb_no in range(1,59):
        with open(f"super_bowl_box_scores/sb_{sb_no}.csv", "r") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)

            team_generator = (Team.from_csv(team) for team in csv_reader)
            for team in team_generator:
                running_score = 0

                for i in range(4):
                    running_score += team.box_score[i] # First Quarter
                    
                    if team.is_afc():
                        afc_counter[running_score%10] += 1
                    else:
                        nfc_counter[running_score%10] += 1
    afc = [(index, count) for (index, count) in enumerate(afc_counter)]
    nfc = [(index, count) for (index, count) in enumerate(nfc_counter)]
    
    print("Last Digit | Occurances")
    for index, count in bubble_sort(afc):
        print(f"{index:-10} | {count}")



if __name__ == "__main__":
    main()
