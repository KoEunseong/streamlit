import streamlit as st
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


# 페이지 제목 설정
st.title("OSMnx 도로 네트워크 시각화")

# 사용자로부터 도시 이름 입력 받기
city_name = st.text_input("도시 이름을 입력하세요", "New York, USA")

# OSMnx를 사용하여 도로 네트워크 가져오기
try:
    graph = ox.graph_from_place(city_name, network_type="all")
    st.success("도로 네트워크 데이터 로드 완료!")
except:
    st.error("도로 네트워크 데이터를 로드하는 중 오류가 발생했습니다.")

# 도로 네트워크 시각화
if graph is not None:
    # 도로 네트워크 그래프를 Matplotlib Figure로 변환
    fig, ax = ox.plot_graph(graph, show=False, close=False)

    # Matplotlib Figure를 Streamlit에 표시
    st.pyplot(fig)
