#coding: utf-8

class Score:

    bad = 1000 #判定範囲(±ms)
    good = 300 #(±ms)
    great = 150 #(±ms)
    perfect = 60 #(±ms)
 
    #コンストラクタ
    def __init__(self, music_list):
        self.score = 0
        self.tile1 = [x[0] for x in music_list if x[1]==1]
        self.tile2 = [x[0] for x in music_list if x[2]==1]
        self.tile3 = [x[0] for x in music_list if x[3]==1]
        self.tile4 = [x[0] for x in music_list if x[4]==1]
        self.tile5 = [x[0] for x in music_list if x[5]==1]
        self.tile6 = [x[0] for x in music_list if x[6]==1]
        self.tile7 = [x[0] for x in music_list if x[7]==1]
        self.tile8 = [x[0] for x in music_list if x[8]==1]
        self.tile9 = [x[0] for x in music_list if x[9]==1]

         
    #引数:タイルの番号i,経過時間elatime 指定したタイルの判定範囲に応じたスコアを返す
    def determineScore(self,i,elatime):
        #タイルの指定
        if i == 1:
            self.tile = self.tile1
        elif i == 2:
            self.tile = self.tile2
        elif i == 3:
            self.tile = self.tile3
        elif i == 4:
            self.tile = self.tile4
        elif i == 5:
            self.tile = self.tile5
        elif i == 6:
            self.tile = self.tile6
        elif i == 7:
            self.tile = self.tile7
        elif i == 8:
            self.tile = self.tile8
        elif i == 9:
            self.tile = self.tile9

        #判定(perfect=100点, great=70点, good= 50点, bad=10点)
        if any(elatime-self.perfect < t < elatime+self.perfect for t in self.tile):
            self.score = 100 #perfect
        elif any(elatime-self.great < t < elatime+self.great for t in self.tile):
            self.score = 70 #great
        elif any(elatime-self.good < t < elatime+self.good for t in self.tile):
            self.score = 50 #good
        elif any(elatime-self.bad < t < elatime+self.bad for t in self.tile):
            self.score = 10 #bad
        else:
            self.score = 0 #miss
            
        return self.score