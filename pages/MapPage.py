import streamlit as st
import folium
from folium.plugins import LocateControl, MarkerCluster
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import time
import random
import pandas as pd

# 주소 → 위도/경도 변환
def geocode(address):
    geolocator = Nominatim(user_agent="my_map_app")
    location = geolocator.geocode(address, timeout=10)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# ⭐️ 추가: 위치에 따라 지역 설정
def get_region(lat, lon):
    if lat and lon:
        if 37.4 <= lat <= 37.6 and 127.0 <= lon <= 127.1:
            return "강남"
        elif 38.1 <= lat <= 38.3 and 128.5 <= lon <= 128.6:
            return "속초"
        else:
            return "기타"
    else:
        return None

def location_set():
        
    # 강남구 주민센터 리스트
    center_locations = [
        {"name": "강남구청", "lat": 37.5172, "lon": 127.0473},
        {"name": "압구정 주민센터", "lat": 37.5275, "lon": 127.0286},
        {"name": "청담동 주민센터", "lat": 37.5252, "lon": 127.0537},
        {"name": "삼성1동 주민센터", "lat": 37.5142, "lon": 127.0636},
        {"name": "대치1동 주민센터", "lat": 37.5025, "lon": 127.0560},
    ]

    # 강남구 초등학교/중학교 리스트
    school_locations = [
        {"name": "언주초등학교", "lat": 37.5087, "lon": 127.0359},
        {"name": "도곡초등학교", "lat": 37.4913, "lon": 127.0487},
        {"name": "대청초등학교", "lat": 37.4945, "lon": 127.0727},
        {"name": "진선여자중학교", "lat": 37.5043, "lon": 127.0494},
        {"name": "대명중학교", "lat": 37.4882, "lon": 127.0586},
    ]

    # 속초 주민센터 리스트
    sokcho_center_locations = [
        {"name": "속초시청", "lat": 38.2060, "lon": 128.5911},
        {"name": "동명동 주민센터", "lat": 38.2118, "lon": 128.5955},
        {"name": "조양동 주민센터", "lat": 38.2057, "lon": 128.5919},
        {"name": "속초읍 주민센터", "lat": 38.2068, "lon": 128.5852},
    ]

    # 속초 초등학교/중학교 리스트
    sokcho_school_locations = [
        {"name": "속초초등학교", "lat": 38.2064, "lon": 128.5891},
        {"name": "속초중학교", "lat": 38.2100, "lon": 128.5915},
        {"name": "청초초등학교", "lat": 38.2075, "lon": 128.5923},
        {"name": "속초여자중학교", "lat": 38.2076, "lon": 128.5910},
    ]

    return center_locations, school_locations, sokcho_center_locations, sokcho_school_locations



def marker(lat, lon, region, address):

    center_locations, school_locations, sokcho_center_locations, sokcho_school_locations = location_set()

    if lat and lon:
        if region == "기타":
            st.error("현재 강남구와 속초 지역만 지원합니다.")
        else:
            # 지도 생성
            m = folium.Map(location=[lat, lon], zoom_start=13)

            # 입력한 주소 위치 마커
            folium.Marker(
                [lat, lon],
                popup=address,
                tooltip=address,
                icon=folium.Icon(color="red")
            ).add_to(m)

            # 내 위치 버튼
            LocateControl(auto_start=False).add_to(m)

            # ⭐️ 지역에 맞는 데이터만 표시
            if region == "강남":
                # 강남 주민센터
                center_cluster = MarkerCluster().add_to(m)
                for center in center_locations:
                    folium.Marker(
                        location=[center["lat"], center["lon"]],
                        popup=center["name"],
                        tooltip=center["name"],
                        icon=folium.Icon(color="blue", icon="home")
                    ).add_to(center_cluster)

                # 강남 초중학교
                school_cluster = MarkerCluster().add_to(m)
                for school in school_locations:
                    folium.Marker(
                        location=[school["lat"], school["lon"]],
                        popup=school["name"],
                        tooltip=school["name"],
                        icon=folium.Icon(color="green", icon="education", prefix='fa')
                    ).add_to(school_cluster)

            elif region == "속초":
                # 속초 주민센터
                center_cluster = MarkerCluster().add_to(m)
                for center in sokcho_center_locations:
                    folium.Marker(
                        location=[center["lat"], center["lon"]],
                        popup=center["name"],
                        tooltip=center["name"],
                        icon=folium.Icon(color="purple", icon="home")
                    ).add_to(center_cluster)

                # 속초 초중학교
                school_cluster = MarkerCluster().add_to(m)
                for school in sokcho_school_locations:
                    folium.Marker(
                        location=[school["lat"], school["lon"]],
                        popup=school["name"],
                        tooltip=school["name"],
                        icon=folium.Icon(color="orange", icon="education", prefix='fa')
                    ).add_to(school_cluster)

            # 지도 출력
            st_folium(m, width=700, height=500)

            # ------ 지도 밑에 실시간 투표율 표시 ------
            st.markdown("---")
            st.subheader("🗳️ 2026 대선 서울 투표율 (실시간 업데이트 중)")

            vote_percentage = 35.0
            placeholder = st.empty()

            for i in range(10):
                vote_percentage += random.uniform(0.1, 0.5)
                if vote_percentage >= 77.9:
                    vote_percentage = 77.9
                placeholder.metric(label="현재 서울 투표율", value=f"{vote_percentage:.1f}%")
                time.sleep(2)

            # ------ 대기 시간 표시 ------
            st.markdown("---")
            st.subheader("📍 현재 예상 대기 시간 (실시간)")

            def generate_wait_times(locations):
                wait_list = []
                for place in locations:
                    wait_min = random.randint(1, 30)
                    wait_list.append({"장소": place["name"], "대기 시간": f"{wait_min}분"})
                return pd.DataFrame(wait_list)

            if region == "강남":
                st.markdown("### 🏢 강남구 주민센터")
                center_df = generate_wait_times(center_locations)
                st.table(center_df)

                st.markdown("### 🏫 강남구 초/중학교")
                school_df = generate_wait_times(school_locations)
                st.table(school_df)

            elif region == "속초":
                st.markdown("### 🏢 속초시 주민센터")
                sokcho_center_df = generate_wait_times(sokcho_center_locations)
                st.table(sokcho_center_df)

                st.markdown("### 🏫 속초시 초/중학교")
                sokcho_school_df = generate_wait_times(sokcho_school_locations)
                st.table(sokcho_school_df)

    else:
        st.error("위치를 찾을 수 없습니다. 다시 입력해 주세요.")



def main():
    # Streamlit 앱
    st.title("희망 투표 장소로 이동하세요")

    address = st.text_input("당신의 5,900만원을 가장 쉽게 사용하는 방법:", "서울 강남구")

    lat, lon = geocode(address)

    region = get_region(lat, lon)

    marker(lat, lon, region, address)


if __name__ == "__main__":
    main()

