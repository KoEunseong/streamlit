import streamlit as st
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt


# 페이지 제목 설정
st.title("OSMnx 도로 네트워크 시각화")

# 사용자로부터 도시 이름 입력 받기
city_name = New York, USA
graph = ox.graph_from_place(city_name, network_type="all")


    # # 도로 네트워크 그래프를 Matplotlib Figure로 변환
    # fig, ax = ox.plot_graph(graph, show=False, close=False)

    # # Matplotlib Figure를 Streamlit에 표시
st.pyplot(fig)
