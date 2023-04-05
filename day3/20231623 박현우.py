win_team = input('이긴 팀을 입력하세요: ')
lose_team = input('진 팀을 입력하세요: ')
win_team_point = int(input('이긴 팀의 점수를 입력하세요: '))
lose_team_point = int(input('진 팀의 점수를 입력하세요: '))
stadium = input('경기장을 입력하세요: ')
goat = input('우수선수를 입력하세요: ')

print(f'어제 {stadium}에서 있었던 경기에서 {win_team}팀이 {lose_team}팀을 꺾고 4강에 합류했다. 양 팀은 이번에도 경기 끝까지 경기 접전을 벌이며 치열한 접접을 이어갔다. 후반부에서도 양 팀이 팽팽하게 맞섰고, 혈전 끝에 {win_team}가 끝내 승리했다.')
print(f'이번 경기에서 {win_team}의 {goat} 선수가 혼자서 {win_team_point - 1}점의 득점을 이어나가며 총 {win_team_point}점의 득점으로 {lose_team_point}점을 얻은 {lose_team}팀을 {win_team_point - lose_team_point}점의 차로 승리로 이끌었다.')