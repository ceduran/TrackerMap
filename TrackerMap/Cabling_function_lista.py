#!/usr/bin/env python
import re

def Dictionarie(filename):

    FiletxtFEDs = open(filename,'r')

    Fd = "FedCrate/FedSlot/FedId/FeUnit/FeChan/FedCh"
    Fc = "FecCrate/FecSlot/FecRing/CcuAddr/CcuChan"
    D = "DcuId/DetId"
    Ll = "LldChan/APV0/APV1"
    pair = "pairNumber/nPairs/nStrips"
    DC = "DCU/MUX/PLL/LLD"

    CablingInfoDict={}

    # Creating lists
    FedCrateList = []
    FedSlotList = []
    FedIdList=[]
    FeUnitList=[]
    FeChanList=[]
    FedChList=[]

    FecCrateList=[]
    FecSlotList=[]
    FecRingList=[]
    CcuAddrList=[]
    CcuChanList=[]
    
    DcuIdList=[]
    DetIdList=[]

    LldChanList=[]
    APV0List=[]
    APV1List=[]
    pairNumberList=[]
    nPairsList=[]
    nStripsList=[]

    DCUList=[]
    MUXList=[]
    PLLList=[]
    LLDList=[]


    for line in FiletxtFEDs:
        if Fd in line:
            pattern = re.split('\W+',line)
            FedCrateList.append(pattern[7])
            FedSlotList.append(pattern[8])
            FedIdList.append(pattern[9])
            FeUnitList.append(pattern[10])
            FeChanList.append(pattern[11])
            FedChList.append(pattern[12])
        if Fc in line:
            pattern = re.split('\W+',line)
            FecCrateList.append(pattern[6])
            FecSlotList.append(pattern[7])
            FecRingList.append(pattern[8])
            CcuAddrList.append(pattern[9])
            CcuChanList.append(pattern[10])
        if D in line:
            pattern = re.split('\W+',line)
            DcuIdList.append(pattern[3])
            DetIdList.append(pattern[4])
        if Ll in line:
            pattern = re.split('\W+',line)
            LldChanList.append(pattern[4])
            APV0List.append(pattern[5])
            APV1List.append(pattern[6])
        if pair in line:
            pattern = re.split('\W+',line)
            pairNumberList.append(pattern[4])
            nPairsList.append(pattern[5])
            nStripsList.append(pattern[6])
        if DC in line:
            pattern = re.split('\W+',line)
            DCUList.append(pattern[6])
            MUXList.append(pattern[7])
            PLLList.append(pattern[8])
            LLDList.append(pattern[9])
        

    for fedcrate,fedslot,fedid,feunit,fechan,fedch,feccrate,fecslot,fecring,ccuaddr,ccuchan,dcuid,detid,lldchan,apv0,apv1,pairnumber,npairs,nstrips,dcu,mux,pll,lld  in zip(FedCrateList,FedSlotList,FedIdList,FeUnitList,FeChanList,FedChList,FecCrateList,FecSlotList,FecRingList,CcuAddrList,CcuChanList,DcuIdList,DetIdList,LldChanList,APV0List,APV1List,pairNumberList,nPairsList,nStripsList,DCUList,MUXList,PLLList,LLDList):

        if detid in CablingInfoDict.keys(): 
            CablingInfoDict[detid].update({pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}})

        else:
                CablingInfoDict.update({detid:{pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}}})
    
    return CablingInfoDict
    
def creaciontxt():
        archi=open('data.txt','w')
        archi.close()


creaciontxt()

ourdictionary = Dictionarie('CablingInfo_Run100357.txt')
#ourdictionary = Dictionarie('CablingInfo_Run105505.txt')


#print ourdictionary["0x1c04d545"]["1"]["FedCrate"]
#print ourdictionary["0x1c04d584"].keys()
#print ourdictionary["0x1c04d584"].values()
#print len(ourdictionary)


#j=1
archi=open('data.txt','w')

for a in ourdictionary.keys():
    #print int(a,16)
    archi.write(str(int(a,16)))
    archi.write("  1")
    archi.write('\n')
    #print int(a,16) >>archi
    
archi.close()
