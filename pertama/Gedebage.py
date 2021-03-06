import shapefile


class Gedebage:
    def __init__(self):
        self.kelurahan = shapefile.Writer('kecamatan_gedebage', shapeType=shapefile.POLYGON)
        self.kelurahan.shapeType
        self.kelurahan.field('nama_kelurahan', 'C')
        self.kantor = shapefile.Writer('kantor_gedebage', shapefile=shapefile.POINT)
        self.kantor.shapeType
        self.kantor.field('nama_kantor', 'C')
        self.jalan = shapefile.Writer('jalan_gedebage', shapefile=shapefile.POLYLINE)
        self.jalan.shapeType
        self.jalan.field('nama_jalan', 'C')

    # Kelurahan
    def kelurahanCimincrang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6960707,-6.9367899],
            [107.6961619,-6.9370242],
            [107.6962692,-6.9372159],
            [107.6964194,-6.9372905],
            [107.6966447,-6.9373118],
            [107.6968271,-6.9373331],
            [107.6967949,-6.9374503],
            [107.6966447,-6.9375994],
            [107.696591,-6.9377165],
            [107.6966768,-6.9378443],
            [107.69687,-6.9379295],
            [107.6970953,-6.9379828],
            [107.6971704,-6.9381532],
            [107.6974922,-6.9382916],
            [107.697342,-6.9384088],
            [107.6973098,-6.9385685],
            [107.6974064,-6.9387709],
            [107.6975137,-6.9389093],
            [107.6976854,-6.9389626],
            [107.697857,-6.9389839],
            [107.6979107,-6.9388241],
            [107.6979429,-6.938707],
            [107.6980394,-6.9386644],
            [107.6981789,-6.9386644],
            [107.6982218,-6.9387709],
            [107.6982218,-6.9388987],
            [107.6980501,-6.9390797],
            [107.6980072,-6.9391862],
            [107.6981467,-6.9393567],
            [107.6982647,-6.9395484],
            [107.6983935,-6.9397401],
            [107.6984149,-6.9398679],
            [107.6984149,-6.9400063],
            [107.6985651,-6.9399424],
            [107.6987261,-6.9398466],
            [107.6988548,-6.9397933,0],
            [107.6988977,-6.9399105,0],
            [107.6987904,-6.940017,0],
            [107.6986724,-6.9401235,0],
            [107.6985866,-6.9402513,0],
            [107.6985222,-6.9404643,0],
            [107.6987368,-6.9405814,0],
            [107.6988333,-6.9406879,0],
            [107.6988226,-6.9408477,0],
            [107.698608,-6.9410287,0],
            [107.698608,-6.9411778,0],
            [107.6986724,-6.9413482,0],
            [107.6988012,-6.9413163,0],
            [107.6989835,-6.9413376,0],
            [107.6990157,-6.9414547,0],
            [107.6989084,-6.9415612,0],
            [107.6989084,-6.9416784,0],
            [107.6989943,-6.9417849,0],
            [107.6992464,-6.9417104,0],
            [107.6995468,-6.9418169,0],
            [107.6998472,-6.9419873,0],
            [107.7000833,-6.9422642,0],
            [107.7000618,-6.942605,0],
            [107.700212,-6.9428393,0],
            [107.699976,-6.9430523,0],
            [107.7001476,-6.9433718,0],
            [107.6999331,-6.9443303,0],
            [107.7001476,-6.9445646,0],
            [107.7001691,-6.9447989,0],
            [107.699976,-6.9450119,0],
            [107.6999331,-6.9454379,0],
            [107.6998043,-6.9465242,0],
            [107.6998043,-6.9481004,0],
            [107.6998472,-6.9497192,0],
            [107.7042675,-6.9502304,0],
            [107.7052975,-6.9508268,0],
            [107.7057481,-6.9518279,0],
            [107.7058125,-6.9530846,0],
            [107.7057481,-6.9552146,0],
            [107.7137303,-6.9554489,0],
            [107.7126574,-6.95432,0],
            [107.7125716,-6.9539579,0],
            [107.7128506,-6.953255,0],
            [107.7129364,-6.9527651,0],
            [107.7130437,-6.9525095,0],
            [107.712872,-6.9505286,0],
            [107.7133226,-6.9493997,0],
            [107.7057695,-6.9468437,0],
            [107.7069068,-6.9418595,0],
            [107.7064347,-6.9413908,0],
            [107.7066493,-6.9361296,0],
            [107.6960707,-6.9367899,0]

        ]])

    def kelurahanRancaNumpang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.7159465,-6.9615335,0],
            [107.716161,-6.960852,0],
            [107.7160323,-6.9602556,0],
            [107.7164614,-6.9598296,0],
            [107.7164614,-6.9591906,0],
            [107.7159036,-6.9586368,0],
            [107.7160323,-6.9578274,0],
            [107.7157319,-6.9573588,0],
            [107.7157319,-6.9566346,0],
            [107.7155173,-6.9560808,0],
            [107.7150023,-6.9558253,0],
            [107.7146161,-6.9559531,0],
            [107.7141869,-6.9562086,0],
            [107.7135861,-6.9560808,0],
            [107.7137303,-6.9554489,0],
            [107.7057481,-6.9552146,0],
            [107.7048314,-6.9642599,0],
            [107.7046202,-6.9675078,0],
            [107.7086938,-6.9655378,0],
            [107.7120841,-6.9637487,0],
            [107.7159465,-6.9615335,0]
        ]])

    def kelurahanRancaBolang(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
                [107.7046202,-6.9675078,0],
                [107.7048135,-6.9638618,0],
                [107.7043629,-6.9637553,0],
                [107.7038263,-6.9635248,0],
                [107.7035475,-6.9631163,0],
                [107.7020025,-6.9628394,0],
                [107.7008224,-6.9629033,0],
                [107.7005863,-6.9626264,0],
                [107.6998782,-6.9622431,0],
                [107.6995135,-6.9617532,0],
                [107.6992345,-6.9619875,0],
                [107.6982688,-6.9615866,0],
                [107.6978398,-6.9612633,0],
                [107.6975179,-6.961242,0],
                [107.6973033,-6.9609225,0],
                [107.6966596,-6.9608373,0],
                [107.696681,-6.9602196,0],
                [107.6960588,-6.959964,0],
                [107.6962948,-6.9592824,0],
                [107.6960802,-6.958899,0],
                [107.696209,-6.9583452,0],
                [107.6958013,-6.9582174,0],
                [107.6959086,-6.9574933,0],
                [107.6954794,-6.9574081,0],
                [107.6953936,-6.9569182,0],
                [107.6951146,-6.95662,0],
                [107.6950932,-6.9561088,0],
                [107.6947928,-6.9558958,0],
                [107.6948786,-6.9548308,0],
                [107.6944065,-6.9547882,0],
                [107.693913,-6.9545113,0],
                [107.6938057,-6.9549799,0],
                [107.6935268,-6.9548947,0],
                [107.6932264,-6.9550012,0],
                [107.6930547,-6.9547456,0],
                [107.6926255,-6.9547456,0],
                [107.6923037,-6.9546178,0],
                [107.6923251,-6.9541066,0],
                [107.6919389,-6.9539788,0],
                [107.6917458,-6.9541705,0],
                [107.6911235,-6.9543409,0],
                [107.6905227,-6.9539149,0],
                [107.6905656,-6.9519979,0],
                [107.6903725,-6.9517849,0],
                [107.6900935,-6.9519766,0],
                [107.6898575,-6.9518701,0],
                [107.6897073,-6.9515506,0],
                [107.6893211,-6.951508,0],
                [107.6890636,-6.9513376,0],
                [107.6888275,-6.951508,0],
                [107.6886344,-6.9519553,0],
                [107.6881623,-6.9518701,0],
                [107.6876259,-6.9515293,0],
                [107.6876688,-6.9511033,0],
                [107.6874328,-6.950869,0],
                [107.6871753,-6.9509116,0],
                [107.6870251,-6.9505921,0],
                [107.6859093,-6.9498253,0],
                [107.6855231,-6.950443,0],
                [107.6853299,-6.9520192,0],
                [107.6851581,-6.9526407,0],
                [107.6854371,-6.9530241,0],
                [107.6856302,-6.9533649,0],
                [107.6857804,-6.9537696,0],
                [107.6857804,-6.954153,0],
                [107.6860164,-6.9547494,0],
                [107.6860164,-6.9552606,0],
                [107.685759,-6.9556014,0],
                [107.6856302,-6.9562617,0],
                [107.6858877,-6.9571988,0],
                [107.6863598,-6.95771,0],
                [107.6864671,-6.9580508,0],
                [107.6861667,-6.958349,0],
                [107.6860379,-6.9591371,0],
                [107.686231,-6.959627,0],
                [107.6864027,-6.960053,0],
                [107.6864027,-6.9606281,0],
                [107.6862954,-6.9612032,0],
                [107.6862954,-6.9621403,0],
                [107.6862954,-6.9629071,0],
                [107.68651,-6.9636739,0],
                [107.6865958,-6.9644407,0],
                [107.6865314,-6.9651436,0],
                [107.6865958,-6.9665493,0],
                [107.6865314,-6.9675291,0],
                [107.6863383,-6.9686153,0],
                [107.6863169,-6.9691478,0],
                [107.6885485,-6.9693821,0],
                [107.6914238,-6.969659,0],
                [107.6944493,-6.9697655,0],
                [107.6961874,-6.9697016,0],
                [107.6982902,-6.9694247,0],
                [107.7008222,-6.9688922,0],
                [107.7028178,-6.9682745,0],
                [107.7046202,-6.9675078,0]
        ]])

    def kelurahanCisarantenKidul(self, nama):
        self.kelurahan.record(nama)
        self.kelurahan.poly([[
            [107.6796651,-6.9380037,0],
                [107.6794076,-6.9411348,0],
                [107.6793432,-6.9427537,0],
                [107.6792789,-6.9474823,0],
                [107.6825833,-6.9479509,0],
                [107.6827765,-6.9486538,0],
                [107.6828408,-6.9492502,0],
                [107.6829696,-6.9496336,0],
                [107.6832915,-6.9498253,0],
                [107.6830125,-6.9517849,0],
                [107.6853299,-6.9520192,0],
                [107.6854801,-6.9511672,0],
                [107.6855231,-6.950443,0],
                [107.6859093,-6.9498253,0],
                [107.6866388,-6.9503152,0],
                [107.6870251,-6.9505921,0],
                [107.6871753,-6.9509116,0],
                [107.6874328,-6.950869,0],
                [107.6876688,-6.9511033,0],
                [107.6876259,-6.9515293,0],
                [107.6881623,-6.9518701,0],
                [107.6886344,-6.9519553,0],
                [107.6888275,-6.951508,0],
                [107.6890636,-6.9513376,0],
                [107.6893211,-6.951508,0],
                [107.6897073,-6.9515506,0],
                [107.6898575,-6.9518701,0],
                [107.6900935,-6.9519766,0],
                [107.6903725,-6.9517849,0],
                [107.6905656,-6.9519979,0],
                [107.6905441,-6.9524665,0],
                [107.6904798,-6.9532759,0],
                [107.6905227,-6.9539149,0],
                [107.6911235,-6.9543409,0],
                [107.6917458,-6.9541705,0],
                [107.6919389,-6.9539788,0],
                [107.6923251,-6.9541066,0],
                [107.6923037,-6.9546178,0],
                [107.6926255,-6.9547456,0],
                [107.6930547,-6.9547456,0],
                [107.6932264,-6.9550012,0],
                [107.6935268,-6.9548947,0],
                [107.6938057,-6.9549799,0],
                [107.693913,-6.9545113,0],
                [107.6944065,-6.9547882,0],
                [107.6948786,-6.9548308,0],
                [107.6948142,-6.9553207,0],
                [107.6947928,-6.9558958,0],
                [107.6950932,-6.9561088,0],
                [107.6951146,-6.95662,0],
                [107.6953936,-6.9569182,0],
                [107.6954794,-6.9574081,0],
                [107.6959086,-6.9574933,0],
                [107.6958013,-6.9582174,0],
                [107.696209,-6.9583452,0],
                [107.6960802,-6.958899,0],
                [107.6962948,-6.9592824,0],
                [107.6960588,-6.959964,0],
                [107.6963592,-6.9600279,0],
                [107.696681,-6.9602196,0],
                [107.696724,-6.9604539,0],
                [107.6966596,-6.9608373,0],
                [107.6973033,-6.9609225,0],
                [107.6975179,-6.961242,0],
                [107.6978398,-6.9612633,0],
                [107.6980972,-6.9615615,0],
                [107.6985908,-6.961668,0],
                [107.6992345,-6.9619875,0],
                [107.6995135,-6.9617532,0],
                [107.6998782,-6.9622431,0],
                [107.7005863,-6.9626264,0],
                [107.7008224,-6.9629033,0],
                [107.7016807,-6.962882,0],
                [107.7020025,-6.9628394,0],
                [107.7024746,-6.9629672,0],
                [107.7029252,-6.9630737,0],
                [107.7035475,-6.9631163,0],
                [107.7037621,-6.9633932,0],
                [107.7040196,-6.9636275,0],
                [107.7043629,-6.9637553,0],
                [107.7048135,-6.9638618,0],
                [107.7057481,-6.9552146,0],
                [107.7057481,-6.9518279,0],
                [107.7052975,-6.9508268,0],
                [107.7042675,-6.9502304,0],
                [107.6998472,-6.9497192,0],
                [107.6997924,-6.9472906,0],
                [107.699976,-6.9450119,0],
                [107.7001691,-6.9447989,0],
                [107.7001476,-6.9445646,0],
                [107.6999331,-6.9443303,0],
                [107.6820898,-6.9379185,0],
                [107.6796651,-6.9380037,0]
        ]])

    # Kantor Kelurahan
    def kantorKelurahanRancaNumpang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.7052045,-6.9627099)

    def kantorKelurahanRancaBolang(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.6921963,-6.9639671)

    def kantorKelurahanCisarantenKidul(self, nama):
        self.kantor.record(nama)
        self.kantor.point(107.688937,-6.9442892)

    def kantorKelurahanCimincrang(self, nama):
        self.kantor.record(nama)
        self.kantor.point( 107.7058811,-6.9460178)

    # Jalan
    def jalanCimincrang(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.7066493,-6.9361296,0],
            [107.7064347,-6.9413908,0],
            [107.7069068,-6.9418595,0],
            [107.7057695,-6.9468437,0],
            [107.7055822,-6.94814,0],
            [107.7057753,-6.9488216,0],
            [107.706183,-6.9495032,0],
            [107.706226,-6.9505256,0],
            [107.7058826,-6.9512072,0],
            [107.7059255,-6.952187,0],
            [107.7058397,-6.9532519,0],
            [107.7057481,-6.9552146,0]
        ]])

    def jalanGedebage(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.6919855,-6.9415877,0],
            [107.691256,-6.9426953,0],
            [107.6893462,-6.942674,0],
            [107.6890887,-6.9440159,0],
            [107.6888098,-6.9467211,0],
            [107.6880373,-6.9483612,0],
            [107.6873721,-6.9495114,0],
            [107.6867284,-6.9507255,0],
            [107.686664,-6.952323,0],
            [107.6864709,-6.9539418,0],
            [107.6862778,-6.9557096,0],
            [107.6864494,-6.9567959,0],
            [107.6867498,-6.957797,0],
            [107.6867284,-6.9592454,0],
            [107.6869859,-6.9641869,0],
            [107.6868786,-6.965763,0],
            [107.686664,-6.9667002,0],
            [107.6869215,-6.9679568,0],
            [107.6877154,-6.9685958,0],
            [107.6891102,-6.9689792,0],
            [107.6901831,-6.969107,0],
            [107.692243,-6.9690431,0],
            [107.6947321,-6.9693413,0],
            [107.6965131,-6.9691922,0],
            [107.6996674,-6.9687023,0],
            [107.7017488,-6.9680207,0],
            [107.7045168,-6.9670197,0]
        ]])

    def jalanRancaNumpang(self, nama):
        self.jalan.record(nama)
        self.jalan.line([[
            [107.7057481,-6.9552146,0],
            [107.7045168,-6.9670197,0]
        ]])

    def close(self):
        self.kelurahan.close()
        self.kantor.close()
        self.jalan.close()
