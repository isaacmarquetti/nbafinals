from random import randint
from time import sleep

jogo = 1
bucks_win = 0
suns_win = 0
game_gianis = {}
stats_gianis = []
total_gianis = 0
media_gianis = total_gianis/3
while True:
    game_gianis['pts'] = randint(15, 45)
    game_gianis['reb'] = randint(6, 13)
    game_gianis['asi'] = randint(0, 8)
    stats_gianis.append(game_gianis.copy())
    total_gianis += game_gianis['pts']
    midd_pts = randint(10, 28)
    midd_reb = randint(2, 8)
    midd_asi = randint(0, 5)
    book_pts = randint(15, 45)
    book_reb = randint(1, 8)
    book_asi = randint(0, 6)
    paul_pts = randint(10, 25)
    paul_reb = randint(0, 5)
    paul_asi = randint(4, 12)
    bucks = randint(80, 130)
    suns = randint(80, 130)

    if bucks > suns:
        bucks_win += 1
    elif bucks == suns:
        bucks += randint(0, 20)
        suns += randint(0, 20)
        if bucks > suns:
            bucks_win += 1
        else:
            suns_win += 1
    else:
        suns_win += 1
    print("-" * 40)
    print(f'JOGO {jogo}'.center(40))
    print("-" * 40)
    print(f'Milwalkee Bucks |{bucks_win}| {bucks} x {suns} |{suns_win}| Phoenix Suns')
    print(f'              | PTS  | REB  | AST  |')
    print(f'Antetokoumpo: |  {game_gianis["pts"]}  |  {game_gianis["reb"]:0>2}  |  {game_gianis["asi"]:0>2}  |')
    print(f'Middletton:   |  {midd_pts}  |  {midd_reb:0>2}  |  {midd_asi:0>2}  |')
    print(f'Booker:       |  {book_pts}  |  {book_reb:0>2}  |  {book_asi:0>2}  |')
    print(f'Paul:         |  {paul_pts}  |  {paul_reb:0>2}  |  {paul_asi:0>2}  |')
    print("-=" * 20)
    jogo += 1

    if bucks_win < 4 and suns_win < 4:
        print(f'[ 1 ] Ir para o próximo jogo.'
              f'[ 2 ] Stats.')
        r = int(input('Escolha a opção: '))
        print('Próximo jogo...')
        sleep(1)
    else:
        break
    if r == 2:
        print(f'              | PTS  | REB  | AST  |')
        print(f'Antetokoumpo: {total_gianis/(jogo-1)}')

if bucks_win > suns_win:
    print(f'Parabéns MILWALKEE BUCKS CAMPEÃO DA NBA ({bucks_win}x{suns_win})')
else:
    print(f'Parabéns PHOENIX SUNS CAMPEÃO DA NBA ({suns_win}x{bucks_win})')