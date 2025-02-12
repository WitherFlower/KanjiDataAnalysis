import csv
from pprint import pprint

def main():

    kanji_data = read_kanji_data()

    corpus_count = kanji_data["all"]
    print("Total number of kanji: ", corpus_count)
    _ = kanji_data.pop("all")
    sorted_kanji = sorted_list(kanji_data)
    print("Number of different kanji: ", len(sorted_kanji))
    print()
    print("Kanji",   "\t\t", "Index", "\t", "Count")
    print()

    print("K&K  叱",   "\t", find(sorted_kanji, "叱"), "\t", kanji_data["叱"])
    print("JPDB 𠮟",   "\t", find(sorted_kanji, "𠮟"), "\t", kanji_data["𠮟"])
    print()

    print("K&K  頬",   "\t", find(sorted_kanji, "頬"), "\t", kanji_data["頬"])
    print("JPDB 頰",   "\t", find(sorted_kanji, "頰"), "\t", kanji_data["頰"])
    print()

    print("K&K  剥",   "\t", find(sorted_kanji, "剥"), "\t", kanji_data["剥"])
    print("JPDB 剝",   "\t", find(sorted_kanji, "剝"), "\t", kanji_data["剝"])
    print()

    print("Commun 填", "\t", find(sorted_kanji, "填"), "\t", kanji_data["填"])
    print("K&K    塡", "\t", find(sorted_kanji, "塡"), "\t", kanji_data["塡"])
    print()

    print("紫", "\t\t", find(sorted_kanji, "紫"), "\t", kanji_data["紫"])
    print("鳳", "\t\t", find(sorted_kanji, "鳳"), "\t", kanji_data["鳳"])
    print()

    deck_kanji = read_deck()
    deck_kanji_sorted: list[tuple[str, int]] = list()
    for kanji in deck_kanji:
        index = find(sorted_kanji, kanji)
        deck_kanji_sorted.append((kanji, index))

    deck_kanji_sorted = sorted(deck_kanji_sorted, key=lambda x: x[1])

    pprint(deck_kanji_sorted[:10])

    # Check that the deck contains all jouyou kanji
    # jouyou_kanji = read_jouyou()
    # for kanji in jouyou_kanji:
    #     assert find(deck_kanji_sorted, kanji) != -1, f"Could not find jouyou_kanji kanji {kanji} in deck"

    additional_kanji_count = 300
    additional_kanji: list[str] = list()

    for kanji in sorted_kanji:
        if find(deck_kanji_sorted, kanji[0]) == -1:
            additional_kanji.append(kanji[0])
        if len(additional_kanji) == additional_kanji_count:
            break

    print(f"Added up to index { find(sorted_kanji, additional_kanji[-1]) }")
    for index, kanji in enumerate(additional_kanji):
        print(kanji, end="")
        if (index + 1) % 50 == 0:
            print()

def find(list: list[tuple[str, int]], kanji: str):
    for i, v in enumerate(list):
        if v[0] == kanji:
            return i
    return -1

def sorted_list(kanji_data: dict[str, int]):
    kanji_list = kanji_data.items()
    def compare(x: tuple[str, int]):
        return -x[1]

    return sorted(kanji_list, key=compare)

def read_kanji_data():
    kanji_data: dict[str, int] = dict()

    with open("./aozora_characters.csv", encoding="utf-8") as aozora_characters:
        reader = csv.DictReader(aozora_characters)
        for line in reader:
            if not kanji_data.keys().__contains__(line["char"]):
                kanji_data.update({ line["char"]: int(line["char_count"]) })
            else:
                kanji_data.update({ line["char"]: kanji_data[line["char"]] + int(line["char_count"]) })

    with open("./wikipedia_characters.csv", encoding="utf-8") as wikipedia_characters:
        reader = csv.DictReader(wikipedia_characters)
        for line in reader:
            if not kanji_data.keys().__contains__(line["char"]):
                kanji_data.update({ line["char"]: int(line["char_count"]) })
            else:
                kanji_data.update({ line["char"]: kanji_data[line["char"]] + int(line["char_count"]) })

    return kanji_data

def read_deck():
    kanji: list[str] = list()

    with open("./deck.txt", encoding="utf-8") as file:
        for line in file:
            kanji.append(line[0])

    return kanji

def read_jouyou():
    kanji: list[str] = list()

    with open("./jouyou.txt", encoding="utf-8") as file:
        for line in file:
            kanji.append(line[0])

    return kanji

if __name__ == '__main__':
    main()
