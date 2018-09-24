import pandas as p

# Simple program that turns a Google Sheets file containing information about teams to Discord friendly strings ready
# to be copied and pasted. Currently I don't think any other features will be added but this might change in future.

def fourvsfour (df):
    to_be_printed = []
    unrank_to_be_printed = True

    # Loop through the DataFrame containing our team information.

    for x in range(df.shape[0]):

        # Tier labels are appended at certain intervals. Label not printed if next team is unranked (see below).

        if x == 0 and not df.loc[x, "Unranked"]:
            to_be_printed.append(":octheDiamond: **DIAMOND** *(can be challenged by teams 2 places or less below)*\n\n")
        elif x == 3 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheGold: **GOLD** *(can be challenged by teams 5 places or less below)*\n\n")
        elif x == 10 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheSilver: **SILVER** *(can be challenged by teams 10 places or less below)*\n\n")
        elif x == 25 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheBronze: **BRONZE** *(can be challenged by teams 20 places or less below)*\n\n")
        elif x == 50 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheIron: **IRON** *(can be challenged by any team below)*\n\n")

        # When first team with "True" in the unranked column comes across in the loop the unranked teams label is printed.
        # The Google Sheet is ordered in a way where the unranked teams are always at the bottom.
        # Flag is set so we know not to print the same label again.

        if df.loc[x, "Unranked"] and unrank_to_be_printed:
            unrank_to_be_printed = False
            to_be_printed.append("\n~\n\n:octheBlood: **NEW TEAMS** *(can't be challenged)*\n\n")

        # If the team is ranked the variable is a number if not -- is used

        if df.loc[x, "Unranked"]:
            rank = "--"
        else:
            rank = str(x + 1)

        # Branch based on whether the team has a logo emoji in the DataFrame or not.
        # Lots of formatting to turn the Google Sheets data into Discord friendly string.
        # Pretty sure there is a better way to check if certain value in a DataFrame is null but oh well this works.
        if str(df.loc[x, "Logo"]) == "nan":
            to_be_printed.append(":flag_{}: `{})` `{} {}-{} ({}-{})`\n".format(df.loc[x, "Country code"], rank,
                                 df.loc[x, "Participant name"], df.loc[x, "Set wins"], df.loc[x, "Set losses"],
                                 df.loc[x, "Game wins"], df.loc[x, "Game losses"]))
        else:
            to_be_printed.append(":flag_{}: `{})` :{}: `{} {}-{} ({}-{})`\n".format(df.loc[x, "Country code"], rank,
                                 df.loc[x, "Logo"], df.loc[x, "Participant name"], df.loc[x, "Set wins"],
                                 df.loc[x, "Set losses"], df.loc[x, "Game wins"], df.loc[x, "Game losses"]))

    # Before returning the list is joined to one string.

    to_be_printed.append("-------------------------------------")
    return "".join(to_be_printed)

def onevsone (df):

    # This works pretty much exactly same as the method above so check comments on that for more information.

    to_be_printed = []
    unrank_to_be_printed = True

    for x in range(df.shape[0]):
        if x == 0 and not df.loc[x, "Unranked"]:
            to_be_printed.append(":octheDiamond: **DIAMOND** *(can be challenged by players 2 places or less below)*\n\n")
        elif x == 3 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheGold: **GOLD** *(can be challenged by players 5 places or less below)*\n\n")
        elif x == 10 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheSilver: **SILVER** *(can be challenged by players 10 places or less below)*\n\n")
        elif x == 25 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheBronze: **BRONZE** *(can be challenged by players 20 places or less below)*\n\n")
        elif x == 50 and not df.loc[x, "Unranked"]:
            to_be_printed.append("\n~\n\n:octheIron: **IRON** *(can be challenged by any player below)*\n\n")

        if df.loc[x, "Unranked"] and unrank_to_be_printed:
            unrank_to_be_printed = False
            to_be_printed.append("\n~\n\n:octheBlood: **NEW PARTICIPANTS** *(can't be challenged)*\n\n")

        if df.loc[x, "Unranked"]:
            rank = "--"
        else:
            rank = str(x + 1)

        to_be_printed.append(":flag_{}: `{})` <@{}> `{}-{} ({}-{})`\n".format(df.loc[x, "Country code"], rank,
                                 df.loc[x, "Discord ID"], df.loc[x, "Set wins"],
                                 df.loc[x, "Set losses"], df.loc[x, "Game wins"], df.loc[x, "Game losses"]))

    to_be_printed.append("-------------------------------------")
    return "".join(to_be_printed)

def onevsonechamp (df):

    # Prints the champions list. A bit different from the leaderboards.

    to_be_printed = []

    for x in range(df.shape[0]):
        if x == 0:
            to_be_printed.append("**SHOOTERS**\n\n")
        elif x == 13:
            to_be_printed.append("~\n\n**BLASTERS**\n\n")
        elif x == 19:
            to_be_printed.append("~\n\n**ROLLERS/BRUSHES**\n\n")
        elif x == 25:
            to_be_printed.append("~\n\n**SLOSHERS**\n\n")
        elif x == 30:
            to_be_printed.append("~\n\n**CHARGERS**\n\n")
        elif x == 35:
            to_be_printed.append("~\n\n**SPLATLINGS**\n\n")
        elif x == 40:
            to_be_printed.append("~\n\n**DUALIES**\n\n")
        elif x == 45:
            to_be_printed.append("~\n\n**BRELLAS**\n\n")

    # Any Discord ID that is 1 is a placeholder and is excluded from the string.

        if str(df.loc[x, "Discord ID"]) == "1":
            to_be_printed.append(":{}:\n\n".format(df.loc[x, "Weapon"]))
        elif str(df.loc[x, "Times defended"]) == "0":
            to_be_printed.append(":{}: <@{}>\n\n".format(df.loc[x, "Weapon"], df.loc[x, "Discord ID"]))
        else:
            to_be_printed.append(":{}: <@{}> *Defended this title {} time(s)!*\n\n".format(df.loc[x, "Weapon"],
                                                                                           df.loc[x, "Discord ID"],
                                                                                           df.loc[x, "Times defended"]))
    to_be_printed.append("-------------------------------------")
    return "".join(to_be_printed)



link = input("What is the URL to the Google Docs CSV file? ")
df = p.read_csv(link)
df["Discord ID"] = df["Discord ID"].astype("int64")

# DataFrame and output is a bit different depending on which Ladder it is so different methods for each variation.

selection = input("1 = 4v4 Ladder 2 = 1v1 Ladder 3 = 1v1 Champions 4 = Exit ")
if selection == "1":
    print(fourvsfour(df))
elif selection == "2":
    print(onevsone(df))
elif selection == "3":
    print(onevsonechamp(df))
elif selection != "4":
    print("Invalid input. 1, 2, 3 or 4 was expected but your input was {}".format(selection))


