import csv, sqlite3
import Alphavantage as av
import time
import os
#con = sqlite3.connect("1.db")
#cur = con.cursor()
annualConnect = "annual.db"
quarterlyConnect = "quarterly.db"
symbol = "AACG   AAME   AAU   ABEO   ABEV   ABIO   ABUS   ACB   ACCO   ACER   ACEVU   ACH   ACHV   ACIU   ACOR   ACRE   ACRS   ACRX   ACST   ACTG   ACY   ADAP   ADES   ADIL   ADMA   ADMP   ADMS   ADRO   ADTX   ADXS   AEF   AEG   AEHR   AEMD   AESE   AEY   AEZS   AFH   AFI   AFIN   AFMD   AGE   AGEN   AGFS   AGI   AGLE   AGRO   AGRX   AGS   AGTC   AHC   AHPI   AHT   AI   AIH   AIHS   AIKI   AIM   AINC   AINV   AIRI   AJX   AKBA   AKER   AKTS   AKTX   ALDX   ALIM   ALJJ   ALNA   ALOT   ALPN   ALRN   ALSK   ALTG   ALYA   AM   AMAG   AMBO   AMC   AMPE   AMPY   AMRH   AMRN   AMRS   AMRX   AMS   AMTX   ANCN   ANGO   ANH   ANIX   ANPC   ANTE   ANVS   ANY   AP   APDN   APEN   APEX   APHA   APLE   APM   APOP   APRN   APTO   APTS   APTX   APVO   APWC   APYX   AQB   AQMS   AQST   AR   ARA   ARAV   ARAY   ARC   ARCO   ARDS   ARDX   ARI   ARKR   ARL   ARLO   ARLP   ARMP   AROC   ARPO   ARR   ARTL   ARTW   ASC   ASLN   ASM   ASPN   ASPS   ASRT   ASRV   ASTC   ASUR   ASX   ASYS   AT   ATAX   ATCO   ATCX   ATEC   ATEN   ATHE   ATHX   ATI   ATIF   ATLC   ATNM   ATOS   ATRO   ATRS   AUG   AUMN   AUTO   AUY   AVAL   AVCO   AVCT   AVDL   AVEO   AVGR   AVID   AVXL   AWH   AWRE   AWX   AXAS   AXGT   AXL   AXLA   AXR   AXTI   AXU   AYRO   AYTU   AZRX   BAK   BASI   BATL   BB   BBAR   BBCP   BBD   BBDC   BBGI   BBI   BBQ   BBVA   BBW   BCBP   BCDA   BCOM   BCRX   BCS   BDR   BDSI   BEDU   BEST   BFIN   BGCP   BGFV   BGI   BGIO   BGSF   BHAT   BHLB   BHR   BHTG   BIMI   BIOC   BIOL   BIOX   BKCC   BKD   BKEP   BKTI   BKYI   BLCM   BLIN   BLNK   BLRX   BLU   BMRA   BNED   BNGO   BNSO   BNTC   BOCH   BORR   BOSC   BOXL   BPFH   BPT   BPTH   BRFS   BRG   BRKL   BRLI   BRLIU   BRN   BROG   BRQS   BRY   BSBK   BSBR   BSGM   BSM   BSMX   BSQR   BTBT   BTE   BTG   BTN   BTU   BW   BWAY   BWB   BWEN   BWL-A   BXG   BXRX   BYFC   CAAP   CAAS   CADE   CAL   CALA   CAMP   CAN   CANF   CANG   CAPR   CARE   CARS   CARV   CASA   CASI   CATB   CATO   CBAT   CBAY   CBH   CBIO   CBL   CBLI   CCCL   CCLP   CCM   CCO   CCR   CCRC   CCRN   CDE   CDEV   CDMO   CDOR   CDR   CDTX   CDXC   CECE   CEI   CEIX   CEL   CELC   CELP   CEMI   CENX   CEPU   CERC   CERS   CETV   CETX   CFB   CFFN   CFMS   CFRX   CGA   CGBD   CGIX   CGRO   CHCI   CHEK   CHFS   CHMA   CHMI   CHNR   CHRA   CHS   CHU   CIA   CIDM   CIG   CIH   CIIC   CIK   CIM   CINR   CIO   CJJD   CKPT   CKX   CLBS   CLDT   CLEU   CLF   CLGN   CLIR   CLMT   CLNC   CLNE   CLNY   CLPR   CLPS   CLPT   CLRB   CLRO   CLS   CLSD   CLSN   CLUB   CLVS   CLWT   CLXT   CMCM   CMLS   CMO   CMRE   CMRX   CMT   CNCE   CNDT   CNET   CNF   CNFR   CNHI   CNR   CNSL   CNSP   CNTY   CNXM   CO   COCP   CODA   CORR   COTY   CPAC   CPAH   CPE   CPG   CPHI   CPIX   CPLG   CPLP   CPRX   CPSH   CPSS   CPST   CRBP   CRD-A   CRD-B   CRDF   CREG   CRESY   CREX   CRHM   CRIS   CRK   CRMD   CRNT   CRON   CRT   CRVS   CRWS   CSBR   CSLT   CSPI   CSPR   CSTM   CSU   CTEK   CTG   CTHR   CTIB   CTIC   CTK   CTMX   CTRA   CTRM   CTSO   CTXR   CURO   CVA   CVE   CVEO   CVGI   CVU   CVV   CWBC   CWBR   CX   CXDC   CXDO   CXW   CYAD   CYAN   CYCC   CYCN   CYH   CYRN   CZWI   DAC   DAIO   DAKT   DARE   DB   DBCP   DBD   DBI   DBVT   DDD   DESP   DFFN   DGLY   DHC   DHT   DHX   DHY   DL   DLHC   DLNG   DLPN   DLTH   DMAC   DMF   DMPI   DMS   DNK   DNN   DNOW   DOGZ   DPW   DRAD   DRH   DRRX   DRTT   DS   DSE   DSKE   DSS   DSSI   DSWL   DSX   DTEA   DTIL   DTSS   DUO   DUOT   DVAX   DVD   DWSN   DXF   DXLG   DXYN   DYAI   DYNT   EAD   EAF   EARS   EAST   EBON   EBR   EBR-B   ECOR   EDAP   EDF   EDN   EDNT   EDRY   EDSA   EDTK   EEX   EFOI   EGLE   EGY   EH   EHT   EIGI   EKSO   ELA   ELOX   ELSE   ELTK   ELVT   EMAN   EMKR   EMX   ENBL   ENDP   ENG   ENIA   ENIC   ENLC   ENLV   ENOB   ENSV   ENTX   ENZ   EOLS   EPIX   EPM   EPSN   EQ   EQS   ERF   ERII   ERJ   EROS   ERYP   ESBA   ESEA   ESRT   ESTE   ESXB   ET   ETM   ETON   ETTX   EURN   EVC   EVFM   EVGN   EVK   EVLO   EVOK   EVOL   EVRI   EXFO   EXK   EXPR   EXTN   EXTR   EYEG   EYEN   EYES   EYPT   EZPW   F   FAMI   FARM   FAT   FBIO   FBP   FCEL   FCF   FCRD   FEDU   FENC   FENG   FET   FFBW   FFHL   FFNW   FHN   FI   FIIIU   FINV   FIT   FIV   FLDM   FLL   FLMN   FLNG   FLNT   FLR   FLUX   FLY   FNB   FNCB   FNHC   FNKO   FORD   FORK   FOSL   FPAY   FPH   FPI   FPL   FPRX   FRAN   FRBA   FRBK   FRD   FREE   FRO   FRSX   FSI   FSM   FSP   FTEK   FTF   FTFT   FTI   FTK   FTSI   FULC   FUSE   FUV   FVE   FWP   GAIN   GALT   GARS   GASS   GAU   GBR   GCI   GDP   GDYN   GE   GEC   GECC   GEL   GEN   GENE   GEOS   GERN   GEVO   GFN   GGB   GGN   GHSI   GIFI   GIGM   GIK   GILT   GLBS   GLBZ   GLDD   GLG   GLMD   GLNG   GLO   GLOG   GLOP   GLRE   GLUU   GLV   GLYC   GMBL   GMDA   GME   GMLP   GMO   GNCA   GNE   GNFT   GNK   GNLN   GNPX   GNRS   GNSS   GNT   GNUS   GNW   GOED   GOGL   GOGO   GOL   GORO   GPL   GPMT   GPOR   GPP   GPRK   GPRO   GRAM   GRCYU   GRF   GRIL   GRIN   GRNQ   GROW   GRTS   GRTX   GSAT   GSB   GSIT   GSKY   GSL   GSM   GSMG   GSS   GSUM   GSV   GT   GTE   GTEC   GTIM   GTT   GTX   GTYH   GURE   GV   GVP   GWGH   HAFC   HALL   HAPP   HBAN   HBIO   HBM   HBP   HCAP   HCFT   HCHC   HDSN   HEPA   HEXO   HFFG   HFRO   HGLB   HGSH   HHT   HIHO   HIL   HIMX   HJLI   HKIB   HL   HLIT   HLX   HMHC   HMTV   HMY   HNNA   HNRG   HOFV   HONE   HOOK   HOPE   HOTH   HOVNP   HPE   HPR   HQI   HROW   HSDT   HSON   HSTO   HT   HTBK   HTBX   HTGM   HTZ   HUD   HUGE   HUIZ   HUSA   HUSN   HWCC   HX   HYMC   HYRE   HZN   IAF   IAG   IBIO   ICCC   ICD   ICL   ICLK   ICMB   ICON   IDEX   IDN   IDRA   IDT   IDXG   IEA   IEC   IFMK   IFRX   IGC   IHD   IHIT   IHRT   IHT   III   IKNX   IMAC   IMBI   IMGN   IMH   IMMP   IMMR   IMRN   IMTE   IMV   INDO   INFI   INFN   ING   INMB   INN   INOD   INPX   INSE   INTT   INUV   INVE   INWK   IO   IPDN   IPHA   IPWR   IRIX   IRS   ISBC   ISEE   ISIG   ISNS   ISR   ISSC   ITCB   ITI   ITP   ITRG   ITRM   ITUB   IVAC   IVC   IVR   IZEA   JAGX   JAKK   JAN   JAX   JCS   JCTCF   JE   JFIN   JFU   JG   JHY   JILL   JMM   JMP   JNCE   JOB   JP   JRJC   JRS   JRSH   JT   JVA   KALA   KBNT   KBSF   KCAC   KDMN   KEP   KEQU   KERN   KFFB   KFS   KGC   KIN   KINS   KIQ   KLDO   KLR   KLXE   KNDI   KODK   KOPN   KOR   KOS   KOSS   KRKR   KRMD   KRNY   KRP   KTCC   KTOV   KTRA   KVHI   KXIN   KZIA   KZR   LAC   LADR   LAIX   LATN   LBC   LBRT   LC   LCI   LCTX   LCUT   LEAF   LEDS   LEE   LEJU   LEU   LGF-A   LGF-B   LGHL   LGL   LGVW   LIFE   LILA   LILAK   LINC   LIND   LINX   LIQT   LITB   LIVE   LIVX   LIZI   LJPC   LKCO   LLIT   LLNW   LMB   LMFA   LMRK   LND   LOAK   LOAN   LODE   LOGC   LOMA   LONE   LOV   LPCN   LPG   LPL   LPTH   LPTX   LQDA   LQDT   LTBR   LTHM   LTRPA   LTRX   LUB   LUNA   LWAY   LX   LXRX   LXU "
symbol = symbol.split()
path = 'C:/Users/idmytrenko/Documents/Prog/Python/data/fundamental'
basedir = os.path.abspath(os.path.dirname('data/fundamental/'))

#print(os.path.join('data','fundamental'))
functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]
functions2 = [
    "INCOME_STATEMENT_annual_report",
    "BALANCE_SHEET_annual_report",
    "CASH_FLOW_annual_report",
]


def create_table_and_header(
    name_table, create_table=True,circle=True
):
    
    
    count = 0
    global functions,functions2
    f = functions
    f2 = functions2
    for i in [quarterlyConnect, annualConnect]:
        con = sqlite3.connect(i)
        print('sqlite3.connect('+str(i)+')')
        cur = con.cursor()
        data = []
        listColumn = ""
        if count == 1:
            f = f2
        for i in f:
            
            with open("data/fundamental/" + i + ".csv") as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data + row
                    break
        data = list(dict.fromkeys(data))
        for i in data[1:]:  #add if 
            listColumn = listColumn + i + ","
        listColumn = listColumn[:-1]
        cur.execute(
            "create table if not exists "
            + name_table
            + " (id_date INTEGER PRIMARY KEY AUTOINCREMENT, fiscalDateEnding DATE UNIQUE ON CONFLICT IGNORE,"
            + listColumn
            + ")"
        )
        con.commit()
        con.close()
        count += 1
    return listColumn


def insert_into_table_value(annualTable, quarterlyTable, name):
    
    count = 0
    global functions,functions2
    f = functions
    f2 = functions2
    for i in [quarterlyConnect, annualConnect]:
        con = sqlite3.connect(i)
        cur = con.cursor()
        if count == 1:
            f = f2
        for func in f:
            with open("data/fundamental/" + func + ".csv", "r") as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                a = 0
                for row in reader:
                    a += 1
                    if a== 1:
                        column_set = row
                    if a % 2 == 1 and a != 1:
                        cur.execute("INSERT INTO "+ name+ " (fiscalDateEnding) VALUES('"+ row[0]+ "')")  # создаю первую коло
                        con.commit()
                        for i in range(len(row)):
                            if i != 0:
                                cur.execute("update "+ name+ " set "+ column_set[i]+ "='"+ row[i]+ "' where fiscalDateEnding= \""+ row[0]+ '"')
                                con.commit()
        count += 1



h = 0

for stock in symbol:
    if h == 10:
        break
    for parametr in functions:
        av.get_data_alphavantage(stock, parametr)
        av.read_data_from_json(stock, parametr)
        aa=5
    create_table_and_header(stock)
    insert_into_table_value(annualConnect, quarterlyConnect, stock)
    print("Прошел" + str(h) + "цыкл")
    for t in range(60):
        print("Осталось ждать" + str(t) + "секунд")
        time.sleep(1)
    h += 1

# create_table_and_header('aame')
# insert_into_table_value(annualConnect, quarterlyConnect, 'aame')