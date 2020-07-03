import random

voca_list = [['creativity', '창의력'], ['matter', '문제'], ['unfold', '펴다, 펼치다'], ['perspective', '관점'], ['ordinary', '평범한'], ['nourish', '키우다, 증진하다'], ['creative', '창의적인'], ['passion', '열정'], ['blade', '칼날'], ['sculptor', '조각가'], ['fragile', '부서지기 쉬운'], ['carve', '조각하다'], ['snap', '툭 부러지다'], ['lead', '연필심, 납'], ['turn into', '~를 ~로 바꾸다'], ['sew', '바느질하다'], ['inspiration', '영감'], ['imaginative', '상상력이 풍부한'], ['major', '전공, 주요한'], ['illustrate', '보여주다'], ['protection', '보호'], ['illusion', '환영, 환상'], ['lead to', '~가 ~하도록 이끌다'], ['experiment', '실험'], ['be involved in', '~에 몰두하다'], ['exhibition', '전시(회)'], ['realistic', '현실적인'], ['novel', '새로운'], ['pitch-black', '칠흙같이 새까만'], ['keen', '날카로운, 예리한'], ['reproduce', '재현하다'], ['put~into life', '생기를 불어넣다'], ['artificial', '인공적인'], ['seldom', '좀처럼 ~않는'], ['depending on', '~에 따라'], ['gorgeous', '멋진, 훌륭한'], ['mainstream', '주류, 대세'], ['come alive', '살아나다'], ['innovative', '혁신적인'], ['astonish', '깜짝 놀라게 하다'], ['musical sheet', '악보'], ['energize', '활기를 복돋우다'], ['rake', '갈퀴로 모으다'], ['bleak', '암울한, 절망적인'], ['mural', '벽화'], ['tempt', '유혹하다'], ['greet', '맞이하다'], ['surroundings', '환경, 주변'], ['scatter', '흩뿌리다'], ['seek to', '~하려고 시도하다'], ['at a glance', '한눈에'], ['object', '물건'], ['line', '~을 따라 늘어서다'], ['expressive', '표현하는'], ['livestock', '가축'], ['triumph', '대성공, 업적'], ['confined', '좁은, 갇힌'], ['fertilizer', '비료'], ['runoff', '유출수'], ['turn to', '~에 의존하다'], ['strain', '압박, 부담'], ['consume', '소비하다'], ['supply', '공급'], ['drain', '퍼내다'], ['inevitable', '불가피한'], ['extend', '확대하다'], ['result in', '~의 결과를 야기하다'], ['manure', '거름, 분뇨'], ['properly', '제대로, 적절히'], ['ecosystem', '생태계'], ['contribute to', '~의 한 원인이 되다'], ['nutrient', '영양분'], ['oxygen', '산소'], ['suffocate', '질식사하다'], ['uninhabitable', '살 수 없는'], ['atmosphere', '대기, 공기'], ['methane', '메탄'], ['be responsible for', '~에 책임이 있다'], ['emission', '방출'], ['release', '배출하다'], ['damp', '축축한'], ['emit', '방출하다'], [
    'statistics', '통계자료'], ['digestive', '소화의'], ['break down', '분해하다, 부수다'], ['burp', '트림하다'], ['pass gas', '방귀를 뀌다'], ['give off', '방출하다'], ['unprecedented', '전례없는'], ['protein', '단백질'], ['concentrated', '집중된, 농축된'], ['bloom', '증가하다'], ['be bound to', '~할 수 밖에 없다'], ['give a second thought', '한 번 더 생각해 보다'], ['abstract', '추상적인'], ['simplified', '단순화된'], ['representation', '표현, 나타낸 것'], ['salient', '두드러진'], ['feature', '특징, 특성'], ['territory', '영토, 영역'], ['phenomenon', '현상'], ['in relation to', '~에 관하여'], ['attribute', '특성, 속성'], ['explicitly', '명시적으로'], ['be related to', '~와 관계가 있다'], ['overall', '전반적인'], ['describe', '묘사하다'], ['navigate', '길을 찾다'], ['means', '수단'], ['communicate', '전달하다, 알리다'], ['capture', '포착하다'], ['detail', '세부 사항'], ['particular', '특정한, 특별한'], ['injury', '부상'], ['initial', '처음의'], ['impact', '영향'], ['resultant', '결과로서 생기는'], ['swell', '붓다'], ['shrink', '수축시키다'], ['blood vessel', '혈관'], ['rush', '몰려듦'], ['opposite', '정반대의'], ['reaction', '반응'], ['chill', '식히다'], ['glow', '달아오르다, 빛나다'], ['gradually', '서서히'], ['reswell', '다시 붓다'], ['physician', '의사'], ['curative', '치료하는'], ['instead', '대신에'], ['recommend', '추천하다'], ['against', '~에 반대하여'], ['experience', '경험'], ['financially', '경제적으로'], ['wealthy', '부유한'], ['wealth', '부, 부유함'], ['personality', '성격'], ['multiplier', '배가시키는 것'], ['cruel', '무정한, 잔인한'], ['generous', '관대한'], ['provide', '제공하다'], ['opportunity', '기회'], ['moreover', '더욱이'], ['thus', '따라서'], ['nevertheless', '그럼에도 불구하고'], ['take time', '시간이 걸리다'], ['strict', '엄격한'], ['along with', '~와 함께'], ['burden', '부담'], ['public performance', '공연'], ['task', '과업, 과제'], ['subject', '피실험자'], ['fluency', '능숙도'], ['flexibility', '유연성'], ['originality', '독창성'], ['composition', '작곡'], ['anecdotal', '일화의'], ['significant', '상당한'], ['undisturbed', '방해받지 않는'], ['convince', '설득하다'], ['similarly', '유사하게, 마찬가지로'], ['additionally', '게다가'], ['therefore', '그러므로']]


def ask(p):
    random.shuffle(voca_list)
    for v in voca_list:
        vi = input('\n' + v[p-1] + ': ')
        if vi == v[2-p]:
            print('맞았어요!')
        else:
            print(f'틀렸습니다! 답은 {v[2-p]}에요.')


ui = ''
while ui != 3:
    print('moseoriVoca에 오신 것을 환영합니다.\n\n1. 한국어 뜻 연습\n2. 스펠링 연습\n3. 종료\n')
    ui = int(input('모드 선택: '))
    if ui in (1, 2):
        ask(ui)
        break

print('\n이용해 주셔서 감사합니다.')
