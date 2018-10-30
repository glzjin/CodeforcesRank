import config
import utils

from_count = 1
username = input("Please input your Codeforces username:")

while True:
    data = {'count': 1000, 'from': from_count, 'handle': username}
    data = utils.api_request("user.status", data)

    calc_problem = []
    rank = 0
    contest_rank = 0

    if len(data['result']) == 0:
        break
    for i in data['result']:
        if i['verdict'] == 'OK':
            if i['problem']['name'] not in calc_problem:
                contest_request_data = {'contestId': i['contestId']}
                contest_data = utils.api_request("contest.standings", contest_request_data)
                contest_name = contest_data["result"]["contest"]["name"]
                div = 0
                if contest_name.find("Div. 1") != -1:
                    div = 1

                if contest_name.find("Div. 2") != -1:
                    div = 2

                if contest_name.find("Div. 3") != -1:
                    div = 3

                calc_problem.append(i['problem']['name'])
                if div != 0:
                    rank += config.Config.rules[div][i['problem']['index']]
                    print("Problem <" + str(i['contestId']) + i['problem']['index'] + " " + i['problem']['name'] + "> <div: " + str(div) + "> rank: " +
                          str(config.Config.rules[div][i['problem']['index']]))
                else:
                    contest_rank += config.Config.rules[2][i['problem']['index']]
                    print("Problem <" + str(i['contestId']) + i['problem']['index'] + " " + i['problem']['name'] + "> contest rank: " +
                          str(config.Config.rules[2][i['problem']['index']]))

    from_count += 1000

    print("=========")
    print("Current total rank: " + str(rank + contest_rank))
    print("Current rank: " + str(rank))
    print("Current contest rank: " + str(contest_rank))
