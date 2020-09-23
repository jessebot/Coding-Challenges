#!/usr/bin/env python3
# an interview challenge


def process_csv_file(results_file=""):
    """
    processes given CSV file, string
    """

    party_codes = {"C": "Conservative Party",
                   "L": "Labour Party",
                   "UKIP": "UKIP",
                   "LD": "Liberal Democrats",
                   "G": "Green Party",
                   "Ind": "Independent",
                   "SNP": "SNP"}

    # open the file
    with open(results_file) as csv_file:
        # creates a list of lines
        election_lines = csv_file.readlines()
        # iterate through each line, since these are not consistent CSV lines
        for line in election_lines:
            # turn csv line into a list
            result_list = line.split(',')
            # 1st element in result_list is removed and stored in this var:
            constituency = result_list.pop(0)
            # if the remaining items in the list aren't an even number,
            # the csv row is malformed
            if len(result_list) % 2 != 0:
                raise Exception("Malformed csv row detected!!")
            # this is a starting dictionary of the results per party code
            party_votes = {"C": 0, "L": 0, "UKIP": 0, "LD": 0, "G": 0,
                           "Ind": 0, "SNP": 0}
            # use enumerate to iterate through the list/maintain index position
            for index, value in enumerate(result_list):
                # if the index is divisible by 2, it should be a vote int
                if index % 2 == 0:
                    try:
                        # votes are still str type/sometimes have extra spaces
                        votes = int(value.strip())
                    except:
                        raise Exception("not an int!")

                    # this will get the next item index, the party code
                    party_code_index = index + 1
                    # we need to clean up this string, just in case
                    party_code = result_list[party_code_index].strip()
                    try:
                        party_votes[party_code] = party_votes[party_code] + votes
                    except:
                        raise Exception("Not a valid party code!")

            # print a nice seperater
            print("Results".center(80, "*"))
            # print the name of the person
            print(constituency)
            # print party and number of votes
            for key, value in party_votes.items():
                print(f"{party_codes[key]}: {value}")


process_csv_file("test_file.csv")
