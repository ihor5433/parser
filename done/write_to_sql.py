import csv, sqlite3
import pandas
from sqlalchemy import create_engine
import Alphavantage as av
import json
import csv
from pandas import read_csv
import csv_to_sqlite
import time
con = sqlite3.connect("test.db")  # change to 'sqlite:///your_filename.db'
cur = con.cursor()

symbol = "AACG   AAME   AAU   ABEO   ABEV   ABIO   ABUS   ACB   ACCO   ACER   ACEVU   ACH   ACHV   ACIU   ACOR   ACRE   ACRS   ACRX   ACST   ACTG   ACY   ADAP   ADES   ADIL   ADMA   ADMP   ADMS   ADRO   ADTX   ADXS   AEF   AEG   AEHR   AEMD   AESE   AEY   AEZS   AFH   AFI   AFIN   AFMD   AGE   AGEN   AGFS   AGI   AGLE   AGRO   AGRX   AGS   AGTC   AHC   AHPI   AHT   AI   AIH   AIHS   AIKI   AIM   AINC   AINV   AIRI   AJX   AKBA   AKER   AKTS   AKTX   ALDX   ALIM   ALJJ   ALNA   ALOT   ALPN   ALRN   ALSK   ALTG   ALYA   AM   AMAG   AMBO   AMC   AMPE   AMPY   AMRH   AMRN   AMRS   AMRX   AMS   AMTX   ANCN   ANGO   ANH   ANIX   ANPC   ANTE   ANVS   ANY   AP   APDN   APEN   APEX   APHA   APLE   APM   APOP   APRN   APTO   APTS   APTX   APVO   APWC   APYX   AQB   AQMS   AQST   AR   ARA   ARAV   ARAY   ARC   ARCO   ARDS   ARDX   ARI   ARKR   ARL   ARLO   ARLP   ARMP   AROC   ARPO   ARR   ARTL   ARTW   ASC   ASLN   ASM   ASPN   ASPS   ASRT   ASRV   ASTC   ASUR   ASX   ASYS   AT   ATAX   ATCO   ATCX   ATEC   ATEN   ATHE   ATHX   ATI   ATIF   ATLC   ATNM   ATOS   ATRO   ATRS   AUG   AUMN   AUTO   AUY   AVAL   AVCO   AVCT   AVDL   AVEO   AVGR   AVID   AVXL   AWH   AWRE   AWX   AXAS   AXGT   AXL   AXLA   AXR   AXTI   AXU   AYRO   AYTU   AZRX   BAK   BASI   BATL   BB   BBAR   BBCP   BBD   BBDC   BBGI   BBI   BBQ   BBVA   BBW   BCBP   BCDA   BCOM   BCRX   BCS   BDR   BDSI   BEDU   BEST   BFIN   BGCP   BGFV   BGI   BGIO   BGSF   BHAT   BHLB   BHR   BHTG   BIMI   BIOC   BIOL   BIOX   BKCC   BKD   BKEP   BKTI   BKYI   BLCM   BLIN   BLNK   BLRX   BLU   BMRA   BNED   BNGO   BNSO   BNTC   BOCH   BORR   BOSC   BOXL   BPFH   BPT   BPTH   BRFS   BRG   BRKL   BRLI   BRLIU   BRN   BROG   BRQS   BRY   BSBK   BSBR   BSGM   BSM   BSMX   BSQR   BTBT   BTE   BTG   BTN   BTU   BW   BWAY   BWB   BWEN   BWL-A   BXG   BXRX   BYFC   CAAP   CAAS   CADE   CAL   CALA   CAMP   CAN   CANF   CANG   CAPR   CARE   CARS   CARV   CASA   CASI   CATB   CATO   CBAT   CBAY   CBH   CBIO   CBL   CBLI   CCCL   CCLP   CCM   CCO   CCR   CCRC   CCRN   CDE   CDEV   CDMO   CDOR   CDR   CDTX   CDXC   CECE   CEI   CEIX   CEL   CELC   CELP   CEMI   CENX   CEPU   CERC   CERS   CETV   CETX   CFB   CFFN   CFMS   CFRX   CGA   CGBD   CGIX   CGRO   CHCI   CHEK   CHFS   CHMA   CHMI   CHNR   CHRA   CHS   CHU   CIA   CIDM   CIG   CIH   CIIC   CIK   CIM   CINR   CIO   CJJD   CKPT   CKX   CLBS   CLDT   CLEU   CLF   CLGN   CLIR   CLMT   CLNC   CLNE   CLNY   CLPR   CLPS   CLPT   CLRB   CLRO   CLS   CLSD   CLSN   CLUB   CLVS   CLWT   CLXT   CMCM   CMLS   CMO   CMRE   CMRX   CMT   CNCE   CNDT   CNET   CNF   CNFR   CNHI   CNR   CNSL   CNSP   CNTY   CNXM   CO   COCP   CODA   CORR   COTY   CPAC   CPAH   CPE   CPG   CPHI   CPIX   CPLG   CPLP   CPRX   CPSH   CPSS   CPST   CRBP   CRD-A   CRD-B   CRDF   CREG   CRESY   CREX   CRHM   CRIS   CRK   CRMD   CRNT   CRON   CRT   CRVS   CRWS   CSBR   CSLT   CSPI   CSPR   CSTM   CSU   CTEK   CTG   CTHR   CTIB   CTIC   CTK   CTMX   CTRA   CTRM   CTSO   CTXR   CURO   CVA   CVE   CVEO   CVGI   CVU   CVV   CWBC   CWBR   CX   CXDC   CXDO   CXW   CYAD   CYAN   CYCC   CYCN   CYH   CYRN   CZWI   DAC   DAIO   DAKT   DARE   DB   DBCP   DBD   DBI   DBVT   DDD   DESP   DFFN   DGLY   DHC   DHT   DHX   DHY   DL   DLHC   DLNG   DLPN   DLTH   DMAC   DMF   DMPI   DMS   DNK   DNN   DNOW   DOGZ   DPW   DRAD   DRH   DRRX   DRTT   DS   DSE   DSKE   DSS   DSSI   DSWL   DSX   DTEA   DTIL   DTSS   DUO   DUOT   DVAX   DVD   DWSN   DXF   DXLG   DXYN   DYAI   DYNT   EAD   EAF   EARS   EAST   EBON   EBR   EBR-B   ECOR   EDAP   EDF   EDN   EDNT   EDRY   EDSA   EDTK   EEX   EFOI   EGLE   EGY   EH   EHT   EIGI   EKSO   ELA   ELOX   ELSE   ELTK   ELVT   EMAN   EMKR   EMX   ENBL   ENDP   ENG   ENIA   ENIC   ENLC   ENLV   ENOB   ENSV   ENTX   ENZ   EOLS   EPIX   EPM   EPSN   EQ   EQS   ERF   ERII   ERJ   EROS   ERYP   ESBA   ESEA   ESRT   ESTE   ESXB   ET   ETM   ETON   ETTX   EURN   EVC   EVFM   EVGN   EVK   EVLO   EVOK   EVOL   EVRI   EXFO   EXK   EXPR   EXTN   EXTR   EYEG   EYEN   EYES   EYPT   EZPW   F   FAMI   FARM   FAT   FBIO   FBP   FCEL   FCF   FCRD   FEDU   FENC   FENG   FET   FFBW   FFHL   FFNW   FHN   FI   FIIIU   FINV   FIT   FIV   FLDM   FLL   FLMN   FLNG   FLNT   FLR   FLUX   FLY   FNB   FNCB   FNHC   FNKO   FORD   FORK   FOSL   FPAY   FPH   FPI   FPL   FPRX   FRAN   FRBA   FRBK   FRD   FREE   FRO   FRSX   FSI   FSM   FSP   FTEK   FTF   FTFT   FTI   FTK   FTSI   FULC   FUSE   FUV   FVE   FWP   GAIN   GALT   GARS   GASS   GAU   GBR   GCI   GDP   GDYN   GE   GEC   GECC   GEL   GEN   GENE   GEOS   GERN   GEVO   GFN   GGB   GGN   GHSI   GIFI   GIGM   GIK   GILT   GLBS   GLBZ   GLDD   GLG   GLMD   GLNG   GLO   GLOG   GLOP   GLRE   GLUU   GLV   GLYC   GMBL   GMDA   GME   GMLP   GMO   GNCA   GNE   GNFT   GNK   GNLN   GNPX   GNRS   GNSS   GNT   GNUS   GNW   GOED   GOGL   GOGO   GOL   GORO   GPL   GPMT   GPOR   GPP   GPRK   GPRO   GRAM   GRCYU   GRF   GRIL   GRIN   GRNQ   GROW   GRTS   GRTX   GSAT   GSB   GSIT   GSKY   GSL   GSM   GSMG   GSS   GSUM   GSV   GT   GTE   GTEC   GTIM   GTT   GTX   GTYH   GURE   GV   GVP   GWGH   HAFC   HALL   HAPP   HBAN   HBIO   HBM   HBP   HCAP   HCFT   HCHC   HDSN   HEPA   HEXO   HFFG   HFRO   HGLB   HGSH   HHT   HIHO   HIL   HIMX   HJLI   HKIB   HL   HLIT   HLX   HMHC   HMTV   HMY   HNNA   HNRG   HOFV   HONE   HOOK   HOPE   HOTH   HOVNP   HPE   HPR   HQI   HROW   HSDT   HSON   HSTO   HT   HTBK   HTBX   HTGM   HTZ   HUD   HUGE   HUIZ   HUSA   HUSN   HWCC   HX   HYMC   HYRE   HZN   IAF   IAG   IBIO   ICCC   ICD   ICL   ICLK   ICMB   ICON   IDEX   IDN   IDRA   IDT   IDXG   IEA   IEC   IFMK   IFRX   IGC   IHD   IHIT   IHRT   IHT   III   IKNX   IMAC   IMBI   IMGN   IMH   IMMP   IMMR   IMRN   IMTE   IMV   INDO   INFI   INFN   ING   INMB   INN   INOD   INPX   INSE   INTT   INUV   INVE   INWK   IO   IPDN   IPHA   IPWR   IRIX   IRS   ISBC   ISEE   ISIG   ISNS   ISR   ISSC   ITCB   ITI   ITP   ITRG   ITRM   ITUB   IVAC   IVC   IVR   IZEA   JAGX   JAKK   JAN   JAX   JCS   JCTCF   JE   JFIN   JFU   JG   JHY   JILL   JMM   JMP   JNCE   JOB   JP   JRJC   JRS   JRSH   JT   JVA   KALA   KBNT   KBSF   KCAC   KDMN   KEP   KEQU   KERN   KFFB   KFS   KGC   KIN   KINS   KIQ   KLDO   KLR   KLXE   KNDI   KODK   KOPN   KOR   KOS   KOSS   KRKR   KRMD   KRNY   KRP   KTCC   KTOV   KTRA   KVHI   KXIN   KZIA   KZR   LAC   LADR   LAIX   LATN   LBC   LBRT   LC   LCI   LCTX   LCUT   LEAF   LEDS   LEE   LEJU   LEU   LGF-A   LGF-B   LGHL   LGL   LGVW   LIFE   LILA   LILAK   LINC   LIND   LINX   LIQT   LITB   LIVE   LIVX   LIZI   LJPC   LKCO   LLIT   LLNW   LMB   LMFA   LMRK   LND   LOAK   LOAN   LODE   LOGC   LOMA   LONE   LOV   LPCN   LPG   LPL   LPTH   LPTX   LQDA   LQDT   LTBR   LTHM   LTRPA   LTRX   LUB   LUNA   LWAY   LX   LXRX   LXU "
symbol = symbol.split()
# print(symbol)
income = "INCOME_STATEMENT"
balance = "BALANCE_SHEET"
cash = "CASH_FLOW"
function =["INCOME_STATEMENT","BALANCE_SHEET","CASH_FLOW"] 

def open_csv_file(csv_file_path):
    """
    Open and read data from a csv file without headers (skipping the first row)
    :param csv_file_path: path of the csv file to process
    :return: a list with the csv content
    """
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        data = list()
        for row in reader:
            data.append(row)

        return data


def get_header_from_csv_and_create_in_sql(
    name_table, create_table=True, name_file=income, circle=False, only_return=False
):
    data = []
    u = ""

    functions = ["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"]
    # if create_table == True:
    # cur.execute('CREATE TABLE if not exists '+name_table+' (date_id INTEGER PRIMARY KEY AUTOINCREMENT)')
    if circle == True:
        for i in functions:
            with open("data/fundamental/" + i + ".csv") as file:
                reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    data = data + row
                    break
        data = list(dict.fromkeys(data))
        for i in data:
            u = u + i + ","
        u = u[:-1]
        cur.execute(
            "create table if not exists "
            + name_table
            + " (id_date INTEGER PRIMARY KEY AUTOINCREMENT,"
            + u
            + ")"
        )

    """Получить заголовок в виде строки"""
    with open("data/fundamental/" + name_file + ".csv") as file:
        reader = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data = data + row
            break
    for i in data:
        u = u + i + ","
    u = u[:-1]
    return u





def create_header_in_sql(symbol):
    """Создание колонки для каждой новой таблици"""
    list_value = ["INCOME_STATEMENT", "BALANCE_SHEET"]
    a = 0
    cur.execute("CREATE TABLE " + symbol + " (date_id PRIMARY KEY AUTOINCREMENT")
    with open("data_file1.csv", "r") as csvfile:
        reader1 = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
        for row in reader1:
            b = len(row)
            if a == 0:
                for i in range(b):
                    cur.execute("alter table stocks_test add column  " + row[i])
                a += 1
            con.commit()
            break
    with open("data_file1.csv", "r") as csvfile:
        reader1 = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
        for row in reader1:
            b = len(row)
            if a == 0:
                for i in range(2, b):
                    cur.execute("alter table stocks_test add column  " + row[i])
                a += 1
            con.commit()
            break


def open_csv():
    k = ""
    with open("data/fundamental/BALANCE_SHEET.csv", "r") as csvfile:
        reader1 = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
        o = 0
        for row in reader1:
            if o % 2 == 1:
                continue
            k = row
            o += 1
    return k


k = ""
with open("data/fundamental/BALANCE_SHEET.csv", "r") as csvfile:
    reader1 = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    o = 0
    for row in reader1:
        if o == 5:
            break
        k = row
        o += 1
t = ""
u = ""
f = ""
# print(k)

h = [
    "2018-12-31",
    "USD",
    "6731000000",
    "2237000000",
    "3863000000",
    "2868000000",
    "466000000",
    "341000000",
    "1547000000",
    "None",
    "372000000",
    "None",
    "750000000",
    "-165000000",
    "631000000",
    "-60000000",
    "94000000",
    "31000000",
    "15000000",
    "-79000000",
    "13000000",
    "None",
    "None",
    "31000000",
    "-180000000",
    "None",
    "341000000",
    "341000000",
    "None",
]
hnew = [
    "2016-12-31",
    "USD",
    "4556000000",
    "226000000",
    "None",
    "304000000",
    "3290000000",
    "1266000000",
    "None",
    "24000000",
    "10000000",
    "-7436000000",
    "192000000",
    "289000000",
    "95000000",
    "1078000000",
    "1984000000",
    "136000000",
    "136000000",
    "-8000000",
    "348000000",
    "3540000000",
    "58000000",
    "977000000",
    "78000000",
    "1235000000",
    "1114000000",
    "845000000",
    "1824000000",
    "None",
    "None",
    "10000000",
    "None",
    "-7436000000",
    "-50000000",
    "None",
    "321000000",
    "None",
    "1016000000",
    "None",
    "1114000000",
    "192000000",
    "1306000000",
    "None",
    "None",
    "None",
    "8750000000",
    "4556000000",
    "1156000000",
    "None",
    "1005000000",
]
# print(len(hnew))
h1 = "2019-12-31,USD,6731000000,2237000000,3863000000,2868000000,466000000,341000000,1547000000,None,372000000,None,750000000,-165000000,631000000,-60000000,94000000,31000000,15000000,-79000000,13000000,None,None,31000000,-180000000,None,341000000,341000000,None"
# print(len(list(h1)))
for i in k:
    t = t + i + ","
t = t[:-1]
# print(t)

# print(u)
sql = "insert into stocks_test1 (" + u + ") values(" + f + ")"
commit = "?"

for i in range(len(hnew)):
    f += "?,"
f = f[:-1]
sql = "insert into stocks_test1 (" + u + ") values(" + f + ")"
# print(sql)
# cur.executemany(sql,t)
# cur.execute('insert into stocks_test1 ('+u+') values('+f+')',hnew)

# cur.execute(
#    'update stocks_test1 set ebit=40435634 where fiscalDateEnding= "2016-12-31"'
# )
# con.commit()
# print(hnew[0])
b = open_csv_file("data/fundamental/BALANCE_SHEET.csv")
# print(b)

h = 0

for i in symbol:
    if h ==3:
        break
    for a in function:
        av.get_data_alphavantage(i,a)
        av.read_data_from_json(a)   
    get_header_from_csv_and_create_in_sql(i,circle=True)
    print('Прошел'+str(h)+'цыкл')
    for t in range(60):
        print('Осталось ждать'+str(t)+'секунд')
        time.sleep(1)
    h += 1