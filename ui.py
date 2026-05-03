import streamlit as st
from calculations import Interest
from calculations import Npv
from gemini import Utils
from stock_market import StockMarketPrice
import math
interest=Interest()
npv=Npv()
util=Utils()
stock=StockMarketPrice()
st.header("**Welcome!**")
st.write("UYARI: **Lütfen Okuyunuz !** ⚠️ YASAL UYARI VE KULLANIM ŞARTLARI Yatırım Tavsiyesi Değildir: Bu uygulama içerisinde sunulan hesaplamalar, analizler ve yapay zeka yanıtları yalnızca bilgilendirme amaçlıdır; yatırım tavsiyesi (YTD) kapsamında değerlendirilemez.  Risk Beyanı: Finansal piyasalarda (Borsa, Döviz vb.) işlem yapmak yüksek risk içerir ve anaparanızın tamamını kaybetmenize neden olabilir.  Hesaplamalar Hakkında: Faiz ve NPV hesaplamaları matematiksel modeller üzerine kuruludur. Stopaj, vergi, işlem komisyonları veya banka özelindeki masraflar bu hesaplamalara dahil edilmemiş olabilir, bu nedenle gerçek sonuçlar farklılık gösterebilir.  Veri Doğruluğu: Canlı borsa ve döviz verileri API üzerinden çekilmektedir ve gecikmeli gelebilir. Sağlanan verilerin kesinliği garanti edilmez.  Sorumluluk Reddi: Bu uygulamanın kullanımından kaynaklanabilecek doğrudan veya dolaylı herhangi bir zarardan geliştirici sorumlu tutulamaz. Tüm sorumluluk kullanıcıya aittir.  ")
check_box=st.checkbox("You have to accept the contract")
if check_box:
    st.title("Financial Calculator")
    tab1,tab2,tab3=st.tabs(['Calculations','NPV','StockMarket'])
    asd1,asd2=st.sidebar.tabs(["Gemini","Currency"])
    with asd1:
        try:
            st.info("You can chat with gemini")
            text = st.text_area("You can write anything")
            gemini_result = util.gemini_integration(text)
            gemini_buton = st.button("Send", use_container_width=True)
            if gemini_buton:
                spinner = st.spinner("Gemini is creating a message...")
                with spinner:
                    st.write(gemini_result)
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")

    with asd2:
        try:
            st.info("Exchange Currency")
            api_result = util.exchange_rate_api()
            api_buton = st.button("Show Currency", use_container_width=True)
            if api_buton:
                spinner_two = st.spinner("The message is loading...")
                with spinner_two:
                    st.write(f"1 USD = {api_result} TRY")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            print(f"General Error : {except_error}")
    with tab1:
        try:
            st.info("Basic Interest Calculation")
            value = st.number_input("You have to give present value", min_value=10, max_value=1000000, key=1,
                                    value=10000)
            rate = st.number_input("You have to give value of rate", min_value=10, max_value=40, value=12, key=2)
            result1 = interest.basic_interest(value, rate)
            buton1 = st.button("Calculate", use_container_width=True, key=3)
            if buton1:
                st.write(f"The result is : {str(result1)[0:6]} $")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Compound Interest Calculation")
            value2 = st.number_input("You have to give present value", min_value=10, max_value=1000000, key=4,
                                     value=10000)
            rate2 = st.number_input("You have to give value of rate", min_value=10, max_value=40, value=12, key=5)
            time = st.number_input("You have to give time", min_value=3, max_value=40, value=4, key=6)
            result2 = interest.compound_interest(value2, rate2, time)
            buton2 = st.button("Calculate", use_container_width=True, key=7)
            if buton2:
                st.write(f"The result is : {str(result2)[0:6]} $")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Dividend Calculations")
            value3 = st.number_input("You have to give present value", min_value=10, max_value=1000000, value=10000,
                                     key=8)
            rate3 = st.number_input("You have to give value of rate", min_value=10, max_value=40, value=12, key=9)
            time2 = st.number_input("You have to give time", min_value=3, max_value=40, value=4, key=10)
            divient_rate = st.number_input("You have to give dividend rate", min_value=3, max_value=5, value=4, key=11)
            minimum_wage = st.number_input("You have to give value of stock shares", min_value=1000, max_value=1000000,
                                           key=12)
            buton3 = st.button("Calculate", use_container_width=True, key=13)
            result3 = interest.calculate_dividient(value3, rate3, time2, divient_rate, minimum_wage)
            if buton3:
                if result3 == 1:
                    st.success("You can live with your divient income!")
                else:
                    st.error("Your divient is not comfortable for you at the moment!")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")

    with tab2:
        try:
            st.info("Present Value Calculations")
            value4 = st.number_input("You have to give future value!", min_value=620, max_value=100000, value=700,
                                     key=17)
            rate4 = st.number_input("You have to value of inflation", min_value=2, max_value=100, value=4, key=14)
            time3 = st.number_input("You have to give value of time", min_value=1, max_value=10, value=2, key=15)
            buton4 = st.button("Calculate", use_container_width=True, key=16)
            if buton4:
                result4 = npv.calculate_pv(value4, rate4, time3)
                st.write(f"The result is : {str(result4)[0:6]} $")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Future Value Calculations")
            value6 = st.number_input("You have to give a current value", min_value=620, max_value=100000, value=800,
                                     key=19)
            value5 = st.number_input("You have to give a  future value", min_value=620, max_value=100000,
                                     value=1000, key=18)
            rate5 = st.number_input("You have to give value of inflation", min_value=2, max_value=100, value=4,
                                    key=20)
            time4 = st.number_input("You have to give value of time", min_value=2, max_value=10, value=4, key=21)
            buton5 = st.button("Calculate", use_container_width=True, key=22)
            if buton5:
                result5 = npv.profit_for_me(value6, value5, rate5, time4)
                if result5 == 1:
                    st.success("You should invest")
                else:
                    st.error("You should not invest!")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Terminal Value")
            value7 = st.number_input("You have to give a current value", min_value=620, max_value=100000, value=800,
                                     key=23)
            growth_rate = st.number_input("You have to give value of growth rate", min_value=2, max_value=100,
                                          value=4, key=24)
            inflation_rate = st.number_input("You have to give value of inflation", min_value=2, max_value=100,
                                             value=4, key=25)
            buton6 = st.button("Calculate", use_container_width=True, key=26)
            if buton6:
                result6 = npv.calculate_terminal_value(value, growth_rate, inflation_rate, time)
                st.write(f"The result is : {str(result6)[0:6]} $")
            st.info("Stock Valuation")
            value8 = st.number_input("You have to give a Free Cash Flow Value", min_value=math.pow(10, 6),
                                     max_value=math.pow(10, 20), value=math.pow(10, 6), key=33)
            value9 = st.number_input("You have to give a Free Cash Flow Value", min_value=math.pow(10, 6),
                                     max_value=math.pow(10, 20), value=math.pow(10, 6), key=27)
            value10 = st.number_input("You have to give a Free Cash Flow Value", min_value=math.pow(10, 6),
                                      max_value=math.pow(10, 20), value=math.pow(10, 6), key=28)
            inflation_rate_two = st.number_input("You have to give value of inflation", min_value=2, max_value=100,
                                                 value=4, key=29)
            growth_rate_two = st.number_input("You have to give value of growth rate", min_value=2, max_value=100,
                                              value=4, key=30)
            stock_shares = st.number_input("How many shares does stock have?", min_value=math.pow(10, 6),
                                           max_value=math.pow(10, 12), key=31)
            buton7 = st.button("Calculate", use_container_width=True, key=32)
            if buton7:
                result7 = npv.calculate_stock_value(value8, value9, value10, inflation_rate_two, growth_rate_two,
                                                    stock_shares)
                st.write(f"The result is : {str(result7)[0:6]} $")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")

    with tab3:
        try:
            st.info("StockMarket")
            ticker1 = st.selectbox("You have to select one stock",
                                   options=["AAPL", "ASELS.IS", "THYAO.IS", "GM"], key=34)
            year = st.number_input("Year :", min_value=2015, max_value=2026, value=2026, key=41)
            month_one = st.number_input("Month :", min_value=1, max_value=12, value=5, key=35)
            day_one = st.number_input("Day :", min_value=1, max_value=30, value=5, key=36)
            year_two = st.number_input("Year :", min_value=year, max_value=2026, value=2026, key=37)
            month_two = st.number_input("Month :", min_value=1, max_value=12, value=5, key=38)
            day_two = st.number_input("Day :", min_value=1, max_value=30, value=5, key=39)
            buton7 = st.button("Show Price", use_container_width=True, key=40)
            if buton7:
                result8 = stock.write_price(ticker1, year, month_one, day_one, year_two, month_two, day_two)
                st.write(f"Mean value of stock is : {result8[0]} $")
                st.write(f"The min value of stock is : {result8[1]} $")
                st.write(f"The max value of stock is : {result8[2]} $")
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Image of Stock")
            ticker2 = st.selectbox("You have to select one stock",
                                   options=["AAPL", "ASELS.IS", "THYAO.IS", "GM"], key=42)
            year_three = st.number_input("Year :", min_value=2015, max_value=2026, value=2026, key=43)
            month_three = st.number_input("Month :", min_value=1, max_value=12, value=5, key=44)
            day_three = st.number_input("Day :", min_value=1, max_value=30, value=5, key=49)
            year_four = st.number_input("Year :", min_value=year, max_value=2026, value=2026, key=45)
            month_four = st.number_input("Month :", min_value=1, max_value=12, value=5, key=46)
            day_four = st.number_input("Day :", min_value=1, max_value=30, value=5, key=47)
            buton8 = st.button("Show Price", use_container_width=True, key=48)
            if buton8:
                result9 = stock.show_price(ticker2, year_three, month_three, day_three, year_four, month_four,
                                           day_four)
                st.pyplot(result9)
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")
        try:
            st.info("Information About Stock")
            ticker3 = st.selectbox("You have to select one stock",
                                   options=["AAPL", "ASELS.IS", "THYAO.IS", "GM"], key=51)
            buton9 = st.button("Show Info", use_container_width=True, key=50)
            if buton9:
                result10 = stock.show_info_about_stock(ticker3)
                st.write(f"Sector : {result10[0]}")
                st.write(f"P/E Ratio : {result10[1]}")
                st.write(f"Forward P/E : {result10[2]}")
                st.write(f"Industry P/E : {result10[3]}")
                st.write(f"Beta Ratio : {result10[4]}")
            st.info("Compare Stock")
            ticker4 = st.multiselect("You have to select options",
                                     options=["AAPL", "ASELS.IS", "THYAO.IS", "GM"], key=52, max_selections=3)
            year_five = st.number_input("Year :", min_value=2015, max_value=2026, value=2026, key=53)
            month_five = st.number_input("Month :", min_value=1, max_value=12, value=5, key=54)
            day_five = st.number_input("Day :", min_value=1, max_value=30, value=5, key=55)
            year_six = st.number_input("Year :", min_value=year, max_value=2026, value=2026, key=56)
            month_six = st.number_input("Month :", min_value=1, max_value=12, value=5, key=57)
            day_six = st.number_input("Day :", min_value=1, max_value=30, value=5, key=58)
            buton10 = st.button("Show Image", use_container_width=True, key=59)
            if buton10:
                result11 = stock.compare_stockmarket(ticker4[0], ticker4[1], ticker4[2], year_five, month_five,
                                                     day_five, year_six, month_six, day_six)
                st.pyplot(result11)
        except ValueError as v_error:
            st.error(f"Value Error : {v_error}")
        except RuntimeWarning as runtime_error:
            st.error(f"Runtime Error : {runtime_error}")
        except KeyboardInterrupt as keyboard_error:
            st.error(f"Keyboard Error : {keyboard_error}")
        except TypeError as type_error:
            st.error(f"Type Error : {type_error}")
        except ConnectionError as c_error:
            st.error(f"Connection Error : {c_error}")
        except Exception as except_error:
            st.error(f"General Error : {except_error}")

else:
    st.error("You haven't accepted the contract,if you want to use this website,then you accept contract!")