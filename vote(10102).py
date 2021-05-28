interviewer = int(input("심사위원은 총 몇 명인가요? : "))

vote = []
if 1 <= interviewer <= 15:
    vote.extend(input("심사위원들은 누구에게 투표하였습니까? (한 줄에 심사위원 투표 개표 결과를 입력해주세요.) : "))

    if 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") > vote.count("B"):
        print("A의 최종우승이 확정되었습니다.")

    elif 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") < vote.count("B"):
        print("B의 최종우승이 확정되었습니다.")

    elif 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") == vote.count("B"):
        print("투표결과 동점입니다. 재대결을 펼치도록 하겠습니다.")

    elif len(vote) != interviewer:
        print("투표 개수와 심사위원 수가 일치하지 않습니다. 다시 시작해주십시요.")

    elif len(vote) < 1 or len(vote) > 15:
        print("오류입니다.")

    else:
        print(" ")

else:
    print("심사위원 수는 한 명이상 15명이하로만 설정할 수 있습니다.")


# if 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") > vote.count("B"):
#     print("A의 최종우승이 확정되었습니다.")

# elif 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") < vote.count("B"):
#     print("B의 최종우승이 확정되었습니다.")

# elif 1 <= len(vote) <= 15 and len(vote) == interviewer and vote.count("A") == vote.count("B"):
#     print("투표결과 동점입니다. 재대결을 펼치도록 하겠습니다.")

# elif len(vote) != interviewer:
#     print("투표 개수와 심사위원 수가 일치하지 않습니다. 다시 시작해주십시요.")

# elif len(vote) < 1 or len(vote) > 15:
#     print("오류입니다.")

# else:
#     print(" ")

    # interviewer = int(input("심사위원은 총 몇 명인가요? : "))

    # vote = []
    # for i in range(1, interviewer + 1):
    #     vote.append(input("심사위원들은 누구에게 투표하였습니까? : "))

    # if vote.count("A") > vote.count("B"):
    #     print("A의 최종우승이 확정되었습니다.")

    # elif vote.count("A") < vote.count("B"):
    #     print("B의 최종우승이 확정되었습니다.")

    # else:
    #     print("투표결과 동점입니다. 재대결을 펼치도록 하겠습니다.")
