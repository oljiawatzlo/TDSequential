class TDSequential:
    def __init__(self,df) -> None:
        self.date = df.index.to_list()
        self.close = df.Close.to_list()
        self.high = df.High.to_list()
        self.low = df.Low.to_list()

        self.bearish_flip = self._BearishTDPriceFlip_()['status']
        self.bullish_flip = self._BullishTDPriceFlip_()['status']

        self.buy_setup_count = self._TDBuySetupCount_()['count']
        self.sell_setup_count = self._TDSellSetupCount_()['count']

        self.tdst_buy = self._TDBuySetup_()['status']
        self.tdst_sell = self._TDSellSetup_()['status']

        

        self.tdst_resistance = self._setTDSTResistance_()['resistance']
        self.tdst_support = self._setTDSTSupport_()['support']
        self.perfect_sell = self._PerfectSellSetup_()['status']
        self.perfect_buy = self._PerfectBuySetup_()['status']
        self.resistance_flip = self._ResistanceFlip_()['resistance']
        self.support_flip = self._SupportFlip_()['support']
        self.buy_countdown = self._TDBuyCountdown_()['status']
        self.buy_countdown_count= self._TDBuyCountdown_()['count']
        

    def _BearishTDPriceFlip_(self) -> dict:
        lstBearish = []
        for i in range(len(self.close)):
            if i > 5:
                if (self.close[i] < self.close[i-4]) and (self.close[i-1] > self.close[i-5]):
                    lstBearish.append(True)
                else:
                    lstBearish.append(False)
            else:
                lstBearish.append(False)

        return {'status' : lstBearish, 'close' : self.close}

    def _BullishTDPriceFlip_(self) -> dict:
        lstBullish = []
        for i in range(len(self.close)):
            if i > 5:
                if (self.close[i] > self.close[i-4]) and (self.close[i-1] < self.close[i-5]):
                    lstBullish.append(True)
                else:
                    lstBullish.append(False)
            else:
                lstBullish.append(False)

        return {'status' : lstBullish, 'close' : self.close}

    def _TDBuySetupCount_(self):
        count = 0
        data = self._BearishTDPriceFlip_()
        lst = []
        for i in range(len(data['status'])):
            if i > 3:
                if count < 1:
                    if data['status']:
                        if data['close'][i]<data['close'][i-4]:
                            count += 1
                            lst.append(count)
                        else:
                            lst.append(0)
                            count = 0
                    else:
                        lst.append(0)
                        count = 0

                elif count >= 1 and count < 8:
                    if data['close'][i]<data['close'][i-4]:
                        count += 1
                        lst.append(count)
                        
                    else:
                        lst.append(0)
                        count = 0

                elif count == 8:
                    if data['close'][i]<data['close'][i-4]:
                        count += 1
                        lst.append(count)
                        count = 0
                        
                    else:
                        lst.append(0)
                        count = 0
                
                else:
                    lst.append(0)
                    count = 0

            else:
                lst.append(0)
                count = 0

        return {'count' : lst}
    
    def _TDSellSetupCount_(self):

        count = 0
        data = self._BullishTDPriceFlip_()
        lst = []
        for i in range(len(data['status'])):
            if i > 3:
                if count < 1:
                    if data['status']:
                        if data['close'][i]>data['close'][i-4]:
                            count += 1
                            lst.append(count)
                        else:
                            lst.append(0)
                            count = 0
                    else:
                        lst.append(0)
                        count = 0

                elif count >= 1 and count < 8:
                    if data['close'][i]>data['close'][i-4]:
                        count += 1
                        lst.append(count)
                    else:
                        lst.append(0)
                        count = 0

                elif count == 8:
                    if data['close'][i]>data['close'][i-4]:
                        count += 1
                        lst.append(count)
                        count = 0
                    else:
                        lst.append(0)
                        count = 0
                
                else:
                    lst.append(0)
                    count = 0

            else:
                lst.append(0)
                count = 0

        return {'count' : lst}

    def _TDBuySetup_(self):
        lstBuySetup = []
        data = self._BearishTDPriceFlip_()
        for i in range(len(data['status'])):
            if i >= 12:
                if data['status'][i-8]:
                    if (data['close'][i]<data['close'][i-4]) and (data['close'][i-1]<data['close'][i-5]) and (data['close'][i-2]<data['close'][i-6]) and (data['close'][i-3]<data['close'][i-7]) and (data['close'][i-4]<data['close'][i-8]) and (data['close'][i-5]<data['close'][i-9]) and (data['close'][i-6]<data['close'][i-10]) and (data['close'][i-7]<data['close'][i-11]) and (data['close'][i-8]<data['close'][i-12]):
                        lstBuySetup.append(True) 
                    else:
                        lstBuySetup.append(False)  
                else:
                    lstBuySetup.append(False)
            else:
                lstBuySetup.append(False)
        return {'status' : lstBuySetup, 'close' : self.close}
    
    def _TDSellSetup_(self):
        lstSellSetup = []
        data = self._BullishTDPriceFlip_()
        for i in range(len(data['status'])):
            if i >= 12:
                if data['status'][i-8]:
                    if (data['close'][i]>data['close'][i-4]) and (data['close'][i-1]>data['close'][i-5]) and (data['close'][i-2]>data['close'][i-6]) and (data['close'][i-3]>data['close'][i-7]) and (data['close'][i-4]>data['close'][i-8]) and (data['close'][i-5]>data['close'][i-9]) and (data['close'][i-6]>data['close'][i-10]) and (data['close'][i-7]>data['close'][i-11]) and (data['close'][i-8]>data['close'][i-12]):
                        lstSellSetup.append(True) 
                    else:
                        lstSellSetup.append(False)  
                else:
                    lstSellSetup.append(False)
            else:
                lstSellSetup.append(False)
        return {'status' : lstSellSetup, 'close' : self.close}

    def _setTDSTResistance_(self):
        lstResistancePrice = []
        resistance = 0
        data = self._TDBuySetup_()
        high = self.high
        for i in range(len(data['status'])):
            if (i < (len(data['status'])-8)):
                if data['status'][i+8]:
                    resistance = high[i]
                    lstResistancePrice.append(resistance)
                else:
                    lstResistancePrice.append(resistance)
            else:
                lstResistancePrice.append(resistance)     
        return {'resistance': lstResistancePrice}

    def _setTDSTSupport_(self):
        lstSupportPrice = []
        support = 0
        data = self._TDSellSetup_()
        low = self.low
        for i in range(len(data['status'])):
            if (i < (len(data['status'])-8)):
                if data['status'][i+8]:
                    support = low[i]
                    lstSupportPrice.append(support)
                else:
                    lstSupportPrice.append(support)
            else:
                lstSupportPrice.append(support)
        return {'support': lstSupportPrice}

    def _ResistanceFlip_(self):
        lstResistancePrice = []
        resistance = 0
        data = self._TDBuySetup_()
        high = self.high
        for i in range(len(data['status'])):
            if data['status'][i]:
                resistance = high[i]
                lstResistancePrice.append(resistance)
            else:
                lstResistancePrice.append(resistance)   
        return {'resistance': lstResistancePrice}

    def _SupportFlip_(self):
        lstSupportPrice = []
        support = 0
        data = self._BullishTDPriceFlip_()
        low = self.low
        for i in range(len(data['status'])):
            if data['status'][i]:
                support = low[i]
                lstSupportPrice.append(support)
            else:
                lstSupportPrice.append(support)
        return {'support': lstSupportPrice}

    def _PerfectSellSetup_(self):
        data = self._TDSellSetup_()['status']
        high = self.high
        lst = []
        for i in range(len(data)):
            if data[i]:
                if ((high[i] >= high[i-2]) and (high[i] >= high[i-3])) or ((high[i-1] >= high[i-2]) and (high[i-2] >= high[i-3])):
                    lst.append('Perfect')
                else:
                    lst.append('Unperfect')
            else:
                lst.append("None")
        return {'status' : lst}

    def _PerfectBuySetup_(self):
        data = self._TDBuySetup_()['status']
        low = self.low
        lst = []
        for i in range(len(data)):
            if data[i]:
                if ((low[i] <= low[i-2]) and (low[i] <= low[i-3])) or ((low[i-1] <= low[i-2]) and (low[i-2] <= low[i-3])):
                    lst.append('Perfect')
                else:
                    lst.append('Unperfect')
            else:
                lst.append("None")
        return {'status' : lst}

    def _PerlRuleSellSetup_(self):
        pass

    def _PerlRuleBuySetup_(self):
        pass

    def _TDSellCountdown_(self):
        high = self.high
        close = self.close
        data = self._TDSellSetup_()['status']
        for i in range(len(data)):
            if data[i]:
                pass
    
    def _TDBuyCountdown_(self):
        low = self.low
        close = self.close
        data = self._TDBuySetup_()['status']
        lst = []
        lstCount = []
        count = 0
        for i in range(len(data)):
            lstCount.append(count)
            if i >=2:
                if count < 1:
                    if data[i]:
                 
                        if (close[i] <= low[i-1]) and (close[i] <= low[i-2]):
                            count += 1
                            lst.append(False)

                             
                        else:
                            lst.append(False)

                    else:
                        lst.append(False)

                elif ((count >= 1) and (count < 13)):

                    if (close[i] <= low[i-1]) and (close[i] <= low[i-2]):                       
                        lst.append(False)
                        count += 1


                    else:
                        lst.append(False)

                
                elif count > 12:
                    lst.append(True)
                    count -= 13

            else:
                lst.append(False)

        return {'status' : lst, 'count' : lstCount}


    
    def Summary(self):
        return {'date' : self.date,  'close' : self.close, 'bearFlip' : self.bearish_flip, 'bullFlip' : self.bullish_flip, 'buySetupCount' : self.buy_setup_count, 'sellSetupCount' : self.sell_setup_count, 'tdstSellSetup' : self.tdst_sell, 'tdstBuySetup' : self.tdst_buy, 'tdstSupport' : self.tdst_support, 'tdstResistance' : self.tdst_resistance, 'perfectSell' :self.perfect_sell, 'perfectBuy' : self.perfect_buy, 'resistanceFlip' : self.resistance_flip, 'supportFlip' : self.support_flip, 'buyCountdown' : self.buy_countdown, "buyCountdownCount": self.buy_countdown_count}

    def getCurrent(self):
        return { 'close' : self.close[-1], 'buySetupCount' : self.buy_setup_count[-1], 'sellSetupCount' : self.sell_setup_count[-1]}

