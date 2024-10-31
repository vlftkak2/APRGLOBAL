import streamlit as st
import pandas as pd
import pymssql
import numpy as np

# DB 연결
conn = pymssql.connect(host=st.secrets['server'], user=st.secrets['username'], password=st.secrets['password'], database=st.secrets['database'], charset="utf8", autocommit=True)
cursor = conn.cursor()

def GlobalStockINSERT():
    # 재고 프로시저 실행
    usp_query = "Exec usp_GlobalSapStock"
    cursor.execute(usp_query)

# 재고부족 확인
def GlobalStockCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 재고 함수 실행
    fu_query = "SELECT * FROM fu_GlobalSapStock('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    Stockdata = pd.DataFrame(data)

    if Stockdata.empty and seq!="":
        st.success(" "+country+" : 재고부족 이상없음🆗")
        return True
    elif seq == "":
        return Stockdata
    else:
        st.warning(" "+country+" : 재고부족 이상있음⚠️")
        return Stockdata
    
# RST 출고에러 확인
def GlobalRSTCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 해외RST 함수 실행
    fu_query = "SELECT * FROM fu_GlobalRSTCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    RSTdata = pd.DataFrame(data)

    if RSTdata.empty and seq!="":
        st.success(" "+country+" : RST 출고 이상없음🆗")
        return True
    elif seq == "":
        return RSTdata
    else:
        st.warning(" "+country+" : RST 출고 이상있음⚠️")
        return RSTdata
    
# RST 입고에러 확인
def GlobalRSTINCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 해외RST 함수 실행
    fu_query = "SELECT * FROM fu_GlobalINRSTCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    RSTdata = pd.DataFrame(data)

    if RSTdata.empty and seq!="":
        st.success(" "+country+" : RST 입고 이상없음🆗")
        return True
    elif seq == "":
        return RSTdata
    else:
        st.warning(" "+country+" : RST 입고 이상있음⚠️")
        return RSTdata    


# 해외 수기출고 중복확인
def GlobalSugiDuplicate(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 해외RST 함수 실행
    fu_query = "SELECT * FROM fu_GlobalSugiDuplicate('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    SugiDuplicatedata = pd.DataFrame(data)

    if SugiDuplicatedata.empty and seq!="":
        st.success(" "+country+" : 수기출고 중복없음🆗")
        return True
    elif seq == "":
        return SugiDuplicatedata 
    else:
        st.warning(" "+country+" : 수기출고 중복있음⚠️")
        return SugiDuplicatedata 

# 해외 클레임등록 중복확인
def GlobalClaimDuplicate(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 클레임등록 함수 실행
    fu_query = "SELECT * FROM fu_GlobalClaimDuplicate('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    ClaimDuplicatedata = pd.DataFrame(data)

    if ClaimDuplicatedata.empty and seq!="":
        st.success(" "+country+" : 클레임등록 중복없음🆗")
        return True
    elif seq == "":
        return ClaimDuplicatedata 
    else:
        st.warning(" "+country+" : 클레임등록 중복있음⚠️")
        return ClaimDuplicatedata 
    
# 수기출고 소수점 에러확인
def GlobalSugiDecimalPoint(seq):
    
    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    #수기출고 함수 실행
    fu_query = "SELECT * FROM Fu_SugiDecimalPoint('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    SugiPointDuplicatedata = pd.DataFrame(data)

    if SugiPointDuplicatedata.empty and seq!="":
        st.success(" "+country+" : 수기출고 소수점 이상없음🆗")
        return True
    elif seq == "":
        return SugiPointDuplicatedata     
    else:
        st.warning(" "+country+" : 수기출고 소수점 이상있음⚠️")
        return SugiPointDuplicatedata     

# 클레임등록 소수점 에러확인
def GlobalClaimDecimalPoint(seq):
    
    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    # 클레임등록 함수 실행
    fu_query = "SELECT * FROM Fu_ClaimDecimalPoint('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    ClaimPointDuplicatedata = pd.DataFrame(data)

    if ClaimPointDuplicatedata.empty and seq!="":
        st.success(" "+country+" : 클레임등록 소수점 이상없음🆗")
        return True
    elif seq == "":
        return ClaimPointDuplicatedata     
    else: 
        st.warning(" "+country+" : 클레임등록 소수점 이상있음⚠️")
        return ClaimPointDuplicatedata     

# WMS출고요청/실적미수신
def GlobalWMSOutCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"    

    fu_query = "SELECT * FROM fu_GlobalWmsOutCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    resultdataframe = pd.DataFrame(data)

    if resultdataframe.empty and seq!="":
        st.success(" "+country+" : WMS출고요청➞실적미수신 이상없음🆗")
        return True
    elif seq == "":
        return resultdataframe     
    else: 
        st.warning(" "+country+" : WMS출고요청➞실적미수신⚠️")
        return resultdataframe       

# WMS입고요청/실적미수신
def GlobalWMSInCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"    

    fu_query = "SELECT * FROM fu_GlobalWmsInCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    resultdataframe = pd.DataFrame(data)

    if resultdataframe.empty and seq!="":
        st.success(" "+country+" : WMS입고요청➞실적미수신 이상없음🆗")
        return True
    elif seq == "":
        return resultdataframe     
    else: 
        st.warning(" "+country+" : WMS입고요청➞실적미수신⚠️")
        return resultdataframe 
    
# 해외 7-11 중복문서 확인
def GlobalSevenElevenDuplicate(seq):

    # 해외RST 함수 실행
    fu_query = "SELECT * FROM fu_GlobalSevenElevenDuplicate()"
    data = pd.read_sql_query(fu_query,conn)
    
    SevenElevenDuplicatedata = pd.DataFrame(data)

    if SevenElevenDuplicatedata.empty and seq!="999":
        st.success("대만 : 7-11 납품생성 중복없음🆗")
        return True
    elif seq == "999":
        return SevenElevenDuplicatedata 
    else:
        st.warning("대만 : 7-11 납품생성 중복있음⚠️")
        return SevenElevenDuplicatedata
    
# 기타출고 WMS요청 취소 & 문서상태 미결    
def GlobalEtcReqCheck(seq):

    country = ""
    if seq == "1":
        country="미국"
    elif seq == "2":
        country = "홍콩"
    elif seq == "3":
        country = "일본"
    elif seq == "4":
        country = "대만"
    elif seq == "5":
        country = "싱가포르"
    elif seq == "999":
        seq = ""
    else:
        country == "없음"

    fu_query = "SELECT * FROM Fu_GlobalEtcReqCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    GlobalEtcCheck = pd.DataFrame(data)

    if GlobalEtcCheck.empty and seq!= "":
        st.success(" "+country+" : 기타출고 문서상태 이상없음🆗")
        return True
    elif seq == "":
        return GlobalEtcCheck 
    else:
        st.warning(" "+country+" : 기타출고 문서상태 마감필요⚠️")
        return GlobalEtcCheck

# 미국 PG비교
def GlobalUSPaymentMethodCheck(seq):

    # 미국PG Function
    fu_query = "SELECT * FROM Fu_USOrderPG() WHERE CollectPG <> TransactionLastPG ORDER BY Divi,U_Refno DESC"
    data = pd.read_sql_query(fu_query,conn)
    
    GlobalUSPaymentMethodCheck = pd.DataFrame(data)

    if GlobalUSPaymentMethodCheck.empty and seq!="999":
        st.success("미국 : PG수집 이상없음🆗")
        return True
    elif seq == "999":
        return GlobalUSPaymentMethodCheck 
    else:
        st.warning("미국 : PG수집 이상있음⚠️")
        return GlobalUSPaymentMethodCheck


# 해외 API수집 확인
def GlobalAPICheck(seq):

    time = ""
    if seq == "1":
        time = "오전"
    elif seq =="2":
        time = "오후"
    else:
        time="에러"

    # 쇼피파이/샵라인 함수 실행
    fu_query = "SELECT * FROM FU_GlobalApiCheck('"+seq+"')"
    data = pd.read_sql_query(fu_query,conn)
    
    GlobalApidata = pd.DataFrame(data)

    if GlobalApidata.empty:
        st.success(" "+time+" : 쇼피파이/샵라인 데이터수집 이상없음🆗")
        return True
    else:
        st.info(" "+time+" : 쇼피파이/샵라인 데이터 미수집⚠️")
        return GlobalApidata    
    
