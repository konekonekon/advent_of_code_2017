def calcul_sum(list_str):
    list_int = [int(i) for i in list_str]
    return sum(list_int)


def create_list(data_str):
    list_number = []
    last_data = None
    # verify 2nd to last data
    for s in data_str:
        if last_data != None and last_data == s:
            list_number.append(s)
        if s is not "\n":
            last_data = s
    # for the first data
    if last_data == data_str[0]:
        list_number.append(data_str[0])

    return list_number


def day1(path):
    file_to_read = open(path, 'r')
    txt = file_to_read.read()
    list_to_sum = create_list(txt)
    # list_to_sum = create_list(str(path))
    result = calcul_sum(list_to_sum)
    print(result)


day1('./day1_input1.d')

# day1(3294199471327195994824832197564859876682638188889768298894243832665654681412886862234525991553276578641265589959178414218389329361496673991614673626344552179413995562266818138372393213966143124914469397692587251112663217862879233226763533911128893354536353213847122251463857894159819828724827969576432191847787772732881266875469721189331882228146576832921314638221317393256471998598117289632684663355273845983933845721713497811766995367795857965222183668765517454263354111134841334631345111596131682726196574763165187889337599583345634413436165539744188866156771585647718555182529936669683581662398618765391487164715724849894563314426959348119286955144439452731762666568741612153254469131724137699832984728937865956711925592628456617133695259554548719328229938621332325125972547181236812263887375866231118312954369432937359357266467383318326239572877314765121844831126178173988799765218913178825966268816476559792947359956859989228917136267178571776316345292573489873792149646548747995389669692188457724414468727192819919448275922166321158141365237545222633688372891451842434458527698774342111482498999383831492577615154591278719656798277377363284379468757998373193231795767644654155432692988651312845433511879457921638934877557575241394363721667237778962455961493559848522582413748218971212486373232795878362964873855994697149692824917183375545192119453587398199912564474614219929345185468661129966379693813498542474732198176496694746111576925715493967296487258237854152382365579876894391815759815373319159213475555251488754279888245492373595471189191353244684697662848376529881512529221627313527441221459672786923145165989611223372241149929436247374818467481641931872972582295425936998535194423916544367799522276914445231582272368388831834437562752119325286474352863554693373718848649568451797751926315617575295381964426843625282819524747119726872193569785611959896776143539915299968276374712996485367853494734376257511273443736433464496287219615697341973131715166768916149828396454638596713572963686159214116763
# )
