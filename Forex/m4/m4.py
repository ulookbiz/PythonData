#........................................................
# Наполнение таблицы уровней
#........................................................
from dbAccess import dbData

db = dbData("EURUSD")
levs = []
levs.append( {"timeframe":"D1","level":"1.2092","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2123","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2173","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2203","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2234","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2253","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.2284","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("XAUUSD")
levs = []
levs.append( {"timeframe":"D1","level":"1810.84","plus":0,"minus":0},
             {"timeframe":"D1","level":"1831.54","plus":0,"minus":0},
             {"timeframe":"D1","level":"1848.77","plus":0,"minus":0},
             {"timeframe":"D1","level":"1869.47","plus":0,"minus":0},
             {"timeframe":"D1","level":"1886.7","plus":0,"minus":0},
             {"timeframe":"D1","level":"1907.4","plus":0,"minus":0},
             {"timeframe":"D1","level":"1924.63","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("XAGUSD")
levs = []
levs.append( {"timeframe":"D1","level":"27.02","plus":0,"minus":0},
             {"timeframe":"D1","level":"27.24","plus":0,"minus":0},
             {"timeframe":"D1","level":"27.46","plus":0,"minus":0},
             {"timeframe":"D1","level":"27.68","plus":0,"minus":0},
             {"timeframe":"D1","level":"27.91","plus":0,"minus":0},
             {"timeframe":"D1","level":"28.13","plus":0,"minus":0},
             {"timeframe":"D1","level":"28.35","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("USDJPY")
levs = []
levs.append( {"timeframe":"D1","level":"109.05","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.20","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.34","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.49","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.63","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.78","plus":0,"minus":0},
             {"timeframe":"D1","level":"109.91","plus":0,"minus":0}             
            )
db.levels(levs)

db = dbData("USDCHF")
levs = []
levs.append( {"timeframe":"D1","level":"0.8919","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.8949","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.8992","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.9022","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.9065","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.9095","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.9138","plus":0,"minus":0}             
            )
db.levels(levs)

db = dbData("GBPUSD")
levs = []
levs.append( {"timeframe":"D1","level":"1.3969","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4034","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4071","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4136","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4172","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4238","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.4274","plus":0,"minus":0},
           )
db.levels(levs)

db = dbData("GBPJPY")
levs = []
levs.append( {"timeframe":"D1","level":"156","plus":0,"minus":0},
             {"timeframe":"D1","level":"155.64","plus":0,"minus":0},
             {"timeframe":"D1","level":"155.27","plus":0,"minus":0},
             {"timeframe":"D1","level":"154.91","plus":0,"minus":0},
             {"timeframe":"D1","level":"154.54","plus":0,"minus":0},
             {"timeframe":"D1","level":"154.18","plus":0,"minus":0},
             {"timeframe":"D1","level":"153.81","plus":0,"minus":0}             
            )
db.levels(levs)

db = dbData("GBPCAD")
levs = []
levs.append( {"timeframe":"D1","level":"1.7251","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7203","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7171","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7123","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7092","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7043","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.7012","plus":0,"minus":0},
           )
db.levels(levs)


db = dbData("CADJPY")
levs = []
levs.append( {"timeframe":"D1","level":"89.59","plus":0,"minus":0},
             {"timeframe":"D1","level":"89.84","plus":0,"minus":0},
             {"timeframe":"D1","level":"90.0","plus":0,"minus":0},
             {"timeframe":"D1","level":"90.25","plus":0,"minus":0},
             {"timeframe":"D1","level":"90.41","plus":0,"minus":0},
             {"timeframe":"D1","level":"90.67","plus":0,"minus":0},
             {"timeframe":"D1","level":"90.83","plus":0,"minus":0}             
            )
db.levels(levs)

db = dbData("USDPLN")
levs = []
levs.append( {"timeframe":"D1","level":"3.6532","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.6736","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.6869","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.7073","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.7206","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.7410","plus":0,"minus":0},
             {"timeframe":"D1","level":"3.7543","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("AUDUSD")
levs = []
levs.append( {"timeframe":"D1","level":"0.7812","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.7789","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.7773","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.775","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.7733","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.771","plus":0,"minus":0},
             {"timeframe":"D1","level":"0.7694","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("AUDNZD")
levs = []
levs.append( {"timeframe":"D1","level":"1.0718","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0731","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0754,"plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0768","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0791","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0804","plus":0,"minus":0},
             {"timeframe":"D1","level":"1.0828","plus":0,"minus":0}
           )
db.levels(levs)

db = dbData("EURJPY")
levs = []
levs.append( {"timeframe":"H4","level":"130.545","plus":0,"minus":0},
             {"timeframe":"W1","level":"130.373","plus":0,"minus":0},
             {"timeframe":"H4","level":"129.9","plus":0,"minus":0} )
db.levels(levs)

db = dbData("EURNZD")
levs = []
levs.append( {"timeframe":"H1","level":"1.677","plus":0,"minus":0} )
db.levels(levs)

db = dbData("GBPAUD")
levs = []
levs.append( {"timeframe":"D1","level":"1.812","plus":0,"minus":0} )
db.levels(levs)

db = dbData("GBPNZD")
levs = []
levs.append( {"timeframe":"H4","level":"1.955","plus":0,"minus":0} )
db.levels(levs)

db = dbData("GBPSGD")
levs = []
levs.append( {"timeframe":"D1","level":"1.835","plus":0,"minus":0} )
db.levels(levs)

db = dbData("AUDCHF")
levs = []
levs.append( {"timeframe":"D1","level":"0.7087","plus":0,"minus":0},
             {"timeframe":"H4","level":"0.702","plus":0,"minus":0} )
db.levels(levs)

db = dbData("NZDJPY")
levs = []
levs.append( {"timeframe":"H1","level":"77.55","plus":0,"minus":0},
             {"timeframe":"H4","level":"77.686","plus":0,"minus":0} )
db.levels(levs)

db = dbData("BTCUSD")
levs = []
levs.append( {"timeframe":"H4","level":"55000","plus":200,"minus":200})
db.levels(levs)

db = dbData("ETHUSD")
levs = []
levs.append( {"timeframe":"H4","level":"1400","plus":0,"minus":0},
            {"timeframe":"H4","level":"1600","plus":0,"minus":0},
            {"timeframe":"H4","level":"1800","plus":0,"minus":0},
            {"timeframe":"H4","level":"2000","plus":0,"minus":0},
            {"timeframe":"H4","level":"2200","plus":0,"minus":0},
            {"timeframe":"H4","level":"2400","plus":0,"minus":0} )
db.levels(levs)