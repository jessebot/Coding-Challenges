#!/usr/bin/env python3
# an interview challenge given to Jesse Hitch on 9/23/20


def process_csv_file(results_file=""):
    """
    processes given CSV file, return nicer dict of dicts
    """
    final_dict = {}

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

            pretty_parties_dict = {}

            for key, value in party_votes.items():
                pretty_parties_dict[party_codes[key]] = value

            final_dict[constituency] = pretty_parties_dict

    return final_dict


def print_result(results_dict):
    """
    prints election results to stdout with given results dictionary
    """
    total_votes_in_election = 0
    total_votes_per_constituency = {}
    # print a nice seperater
    for constituency, party_votes in results_dict.items():
        print(f"Results for {constituency}".center(80, "*"))
        total_constituency_votes = 0
        # print the name of the person
        for party, votes in party_votes.items():
            total_constituency_votes += votes
            # print party and number of votes
            print(f"{party} votes: {votes}")

        print(f"Total votes for {constituency}: {total_constituency_votes}")
        total_votes_per_constituency[constituency] = total_constituency_votes
        total_votes_in_election += total_constituency_votes

    print("Final Results".center(80, "*"))
    print(f"Total votes in election: {total_votes_in_election}")
    print(f"Percentages of total votes, by constituency:")
    for constituency, total_votes in total_votes_per_constituency.items():
        percentage_dec = total_votes / total_votes_in_election
        percentage_of_total = percentage_dec * 100
        percentage_of_total_int = int(percentage_of_total)
        print(f"{constituency}: {percentage_of_total_int}%")

if __name__ == '__main__':
    parsed_csv_dict = process_csv_file("test_file.csv")
    print_result(parsed_csv_dict)
