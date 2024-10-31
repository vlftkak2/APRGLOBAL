import streamlit as st
import pandas as pd
import numpy as np
import datetime
from modules.nav import sidebar
from containter.footer import footer
from modules.globalfunction import *

st.set_page_config(page_title="해외물류운영팀 모니터링",
                   page_icon="🔥",
                   layout="wide")

vert_space = '<div style="padding: 20px 5px;"></div>'

sidebar()
footer()

curdate = datetime.datetime.now()
curdate = curdate.strftime("%Y-%m-%d")

curweek = datetime.datetime.now()
curweek = curweek.strftime("%w")

if curweek == "1":
    curweek = "월"
elif curweek == "2":
    curweek = "화"
elif curweek == "3":
    curweek = "수"
elif curweek == "4":
    curweek = "목"
elif curweek == "5":
    curweek = "금"
elif curweek =="6":
    curweek = "토"
elif curweek == "0":
    curweek ="일"
else:
    curweek = "에러"

with st.spinner('Data Loading Please Wait...'):

    st.title('🔥APR 해외 모니터링')
    st.subheader("📅날짜 : "+curdate+"("+curweek+")")

    st.markdown(vert_space, unsafe_allow_html=True)
    Range1, Range2, Range3 = st.columns(3)

    # 범위1
    with Range1:
        #재고부족 확인
        st.markdown("### 재고부족 확인")  
        GlobalStockINSERT() #국가별 재고부족 DATA INSERT
        GlobalStockCheck('1') #미국
        GlobalStockCheck('2') #홍콩
        GlobalStockCheck('3') #일본
        GlobalStockCheck('4') #대만
        GlobalStockCheck('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### 클레임 소수점 확인") 
        GlobalClaimDecimalPoint('1') #미국
        GlobalClaimDecimalPoint('2') #홍콩
        GlobalClaimDecimalPoint('3') #일본
        GlobalClaimDecimalPoint('4') #대만
        GlobalClaimDecimalPoint('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)   
        st.markdown("### 수기출고 중복 확인")
        GlobalSugiDuplicate('1') #미국
        GlobalSugiDuplicate('2') #홍콩
        GlobalSugiDuplicate('3') #일본
        GlobalSugiDuplicate('4') #대만
        GlobalSugiDuplicate('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### 기타출고요청 WMS취소➞문서상태 미결")
        GlobalEtcReqCheck('1') #미국
        GlobalEtcReqCheck('2') #홍콩
        GlobalEtcReqCheck('3') #일본
        GlobalEtcReqCheck('4') #대만
        GlobalEtcReqCheck('5') #싱가포르    

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### 쇼피파이/샵라인 데이터수집 확인") 
        GlobalAPICheck('1')
        GlobalAPICheck('2')        

    # 범위2
    with Range2:
        st.markdown("### RST 입고 문서생성 에러여부")  
        GlobalRSTINCheck('1') #미국
        GlobalRSTINCheck('2') #홍콩
        GlobalRSTINCheck('3') #일본
        GlobalRSTINCheck('4') #대만
        GlobalRSTINCheck('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)   
        st.markdown("### 클레임 중복 확인") 
        GlobalClaimDuplicate('1') #미국
        GlobalClaimDuplicate('2') #홍콩 
        GlobalClaimDuplicate('3') #일본 
        GlobalClaimDuplicate('4') #대만 
        GlobalClaimDuplicate('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### WMS입고요청➞실적미수신")    
        GlobalWMSInCheck('1') #미국
        GlobalWMSInCheck('2') #일본
        GlobalWMSInCheck('3') #홍콩
        GlobalWMSInCheck('4') #대만
        GlobalWMSInCheck('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### 7-11 중복납품 확인")   
        GlobalSevenElevenDuplicate('4')     

    # 범위3
    with Range3:
        #RST 출고문서 확인
        st.markdown("### RST 출고 문서생성 에러여부")  
        GlobalRSTCheck('1') #미국
        GlobalRSTCheck('2') #홍콩
        GlobalRSTCheck('3') #일본
        GlobalRSTCheck('4') #대만
        GlobalRSTCheck('5') #싱가포르    

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### 수기출고 소수점 확인")
        GlobalSugiDecimalPoint('1') #미국
        GlobalSugiDecimalPoint('2') #홍콩
        GlobalSugiDecimalPoint('3') #일본
        GlobalSugiDecimalPoint('4') #대만
        GlobalSugiDecimalPoint('5') #싱가포르

        st.markdown(vert_space, unsafe_allow_html=True)
        st.markdown("### WMS출고요청➞실적미수신")
        GlobalWMSOutCheck('1') #미국
        GlobalWMSOutCheck('2') #일본
        GlobalWMSOutCheck('3') #홍콩
        GlobalWMSOutCheck('4') #대만
        GlobalWMSOutCheck('5') #싱가포르  

        #st.markdown(vert_space, unsafe_allow_html=True)
        #st.markdown("### 미국 PG수집 확인")
        #GlobalUSPaymentMethodCheck('1')

    st.markdown(vert_space, unsafe_allow_html=True)
    st.markdown("### 국가별 데이터 상세조회") 
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["재고부족","RST입고","RST출고","클레임소수점","클레임중복","수기출고소수점","수기출고중복","WMS입고요청_실적미수신","WMS출고요청_실적미수신","기타출고요청_선택마감","7-11"])

    with tab1:
        StockAllData=GlobalStockCheck('999')
        if StockAllData is not True:
            st.dataframe(StockAllData)
    with tab2:
        RSTAllData=GlobalRSTINCheck('999')
        if RSTAllData is not True:
            st.dataframe(RSTAllData)         

    with tab3:
        RSTAllData=GlobalRSTCheck('999')
        if RSTAllData is not True:
            st.dataframe(RSTAllData)             
    with tab4:
        SugiDupliAllData=GlobalSugiDuplicate('999')
        if SugiDupliAllData is not True:
            st.dataframe(SugiDupliAllData)    
    with tab5:        
        ClaimDuplieAllData=GlobalClaimDuplicate('999')
        if ClaimDuplieAllData is not True:
            st.dataframe(ClaimDuplieAllData)    
    with tab6:
        SugiDupliPointAllData=GlobalSugiDecimalPoint('999')
        if SugiDupliPointAllData is not True:
            st.dataframe(SugiDupliPointAllData)    
    with tab7:
        ClaimDupliPointAllData=GlobalClaimDecimalPoint('999')
        if ClaimDupliPointAllData is not True:
            st.dataframe(ClaimDupliPointAllData)  
    with tab8:
        WmsInData=GlobalWMSInCheck('999')
        if WmsInData is not True:
            st.dataframe(WmsInData)   

    with tab9:
        WmsOutData=GlobalWMSOutCheck('999')
        if WmsOutData is not True:
            st.dataframe(WmsOutData)                     
    with tab10:
        EtcCheckAllData=GlobalEtcReqCheck('999')
        if EtcCheckAllData is not True:
            st.dataframe(EtcCheckAllData)   
    with tab11:
        SevenElevenAllData=GlobalSevenElevenDuplicate('999')
        if SevenElevenAllData is not True:
            st.dataframe(SevenElevenAllData)   
