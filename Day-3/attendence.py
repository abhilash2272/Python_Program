# A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
# Write a Python program that:
# Cleans each day's list (normalizes case, removes duplicates).
# Prints the total number of unique attendees across all days.
# Prints the list of attendees who attended all three days.
# Prints the list of attendees who attended exactly one day.
# Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
# Produces a final report with counts and sorted lists for each of the above outputs.
def atten(day1, day2, day3):
    # Normalize case and remove duplicates
    d1 = set(email.lower() for email in day1)
    d2 = set(email.lower() for email in day2)
    d3 = set(email.lower() for email in day3)
    # Unique attendees across all days
    unique_attendees = d1 | d2 | d3
    # Attendees who attended all three days
    all_three = d1 & d2 & d3
    # Attendees who attended exactly one day
    one_day = (d1 - d2 - d3) | (d2 - d1 - d3) | (d3 - d1 - d2)
    # Pairwise overlaps
    d1_d2 = d1 & d2
    d2_d3 = d2 & d3
    d1_d3 = d1 & d3
    print("Total unique attendees:", len(unique_attendees))
    print("Unique attendees (sorted):", sorted(unique_attendees))
    print("Attended all three days:", len(all_three))
    print("List (sorted):", sorted(all_three))
    print("Attended exactly one day:", len(one_day))
    print("List (sorted):", sorted(one_day))
    print("Day1 & Day2 overlap:", len(d1_d2), sorted(d1_d2))
    print("Day2 & Day3 overlap:", len(d2_d3), sorted(d2_d3))
    print("Day1 & Day3 overlap:", len(d1_d3), sorted(d1_d3))
day1 = ["Alice@Email.com", "bob@email.com", "carol@email.com", "alice@email.com"]
day2 = ["Bob@email.com", "dave@email.com", "eve@email.com", "carol@email.com"]
day3 = ["eve@email.com", "alice@email.com", "frank@email.com", "bob@email.com"]
atten(day1, day2, day3)

    
