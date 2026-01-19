import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="HR & Marketing Dashboard",
    page_icon="📊",
    layout="wide"
)

# 데이터 로드 함수
@st.cache_data
def load_hr_data():
    df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df

@st.cache_data
def load_marketing_data():
    df = pd.read_csv("../data/marketing_campaign_dataset.csv")
    # Acquisition_Cost 컬럼의 달러 포맷 정리
    df['Acquisition_Cost'] = df['Acquisition_Cost'].replace(r'[\$,]', '', regex=True).astype(float)
    return df

# 데이터 로드
hr_df = load_hr_data()
marketing_df = load_marketing_data()

# 사이드바 구성
st.sidebar.title("📊 Dashboard")
st.sidebar.markdown("---")

# HR 필터
st.sidebar.subheader("HR 필터")
departments = ["전체"] + list(hr_df['Department'].unique())
selected_dept = st.sidebar.selectbox("부서 선택", departments)

genders = ["전체"] + list(hr_df['Gender'].unique())
selected_gender = st.sidebar.selectbox("성별 선택", genders)

st.sidebar.markdown("---")

# 마케팅 필터
st.sidebar.subheader("마케팅 필터")
channels = ["전체"] + list(marketing_df['Channel_Used'].unique())
selected_channel = st.sidebar.selectbox("채널 선택", channels)

campaign_types = ["전체"] + list(marketing_df['Campaign_Type'].unique())
selected_campaign = st.sidebar.selectbox("캠페인 타입", campaign_types)

# HR 데이터 필터링
filtered_hr = hr_df.copy()
if selected_dept != "전체":
    filtered_hr = filtered_hr[filtered_hr['Department'] == selected_dept]
if selected_gender != "전체":
    filtered_hr = filtered_hr[filtered_hr['Gender'] == selected_gender]

# 마케팅 데이터 필터링
filtered_marketing = marketing_df.copy()
if selected_channel != "전체":
    filtered_marketing = filtered_marketing[filtered_marketing['Channel_Used'] == selected_channel]
if selected_campaign != "전체":
    filtered_marketing = filtered_marketing[filtered_marketing['Campaign_Type'] == selected_campaign]

# 메인 타이틀
st.title("사내 인사(HR) 및 마케팅 현황 대시보드")

# 탭 구성
tab1, tab2 = st.tabs(["📋 HR 분석", "📈 마케팅 분석"])

# 탭 1: HR 분석
with tab1:
    st.header("HR 분석")

    # 퇴사율 KPI
    total_employees = len(filtered_hr)
    attrition_count = len(filtered_hr[filtered_hr['Attrition'] == 'Yes'])
    attrition_rate = (attrition_count / total_employees * 100) if total_employees > 0 else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("총 직원 수", f"{total_employees:,}명")
    with col2:
        st.metric("퇴사자 수", f"{attrition_count:,}명")
    with col3:
        st.metric("퇴사율", f"{attrition_rate:.1f}%")

    st.markdown("---")

    # 차트 영역
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        # 부서별 현황 Bar 차트
        st.subheader("부서별 직원 현황")
        dept_stats = filtered_hr.groupby('Department').agg({
            'EmployeeNumber': 'count',
            'Attrition': lambda x: (x == 'Yes').sum()
        }).reset_index()
        dept_stats.columns = ['Department', 'Total', 'Attrition']
        dept_stats['Attrition_Rate'] = (dept_stats['Attrition'] / dept_stats['Total'] * 100).round(1)

        fig_dept = px.bar(
            dept_stats,
            x='Department',
            y='Total',
            color='Attrition_Rate',
            color_continuous_scale='Reds',
            text='Total',
            labels={'Total': '직원 수', 'Department': '부서', 'Attrition_Rate': '퇴사율(%)'}
        )
        fig_dept.update_traces(textposition='outside')
        fig_dept.update_layout(height=400)
        st.plotly_chart(fig_dept, use_container_width=True)

    with chart_col2:
        # 소득 관계 Box 플롯
        st.subheader("부서별/퇴사 여부별 월 소득")
        fig_income = px.box(
            filtered_hr,
            x='Department',
            y='MonthlyIncome',
            color='Attrition',
            labels={'MonthlyIncome': '월 소득', 'Department': '부서', 'Attrition': '퇴사 여부'},
            color_discrete_map={'Yes': '#EF553B', 'No': '#636EFA'}
        )
        fig_income.update_layout(height=400)
        st.plotly_chart(fig_income, use_container_width=True)

# 탭 2: 마케팅 분석
with tab2:
    st.header("마케팅 분석")

    # ROI KPI
    avg_roi = filtered_marketing['ROI'].mean()
    avg_conversion = filtered_marketing['Conversion_Rate'].mean() * 100
    total_clicks = filtered_marketing['Clicks'].sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("평균 ROI", f"{avg_roi:.2f}")
    with col2:
        st.metric("평균 전환율", f"{avg_conversion:.2f}%")
    with col3:
        st.metric("총 클릭 수", f"{total_clicks:,}")

    st.markdown("---")

    # 차트 영역
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        # 채널별 전환율 Bar 차트
        st.subheader("채널별 평균 전환율")
        channel_stats = filtered_marketing.groupby('Channel_Used').agg({
            'Conversion_Rate': 'mean',
            'ROI': 'mean'
        }).reset_index()
        channel_stats['Conversion_Rate_Pct'] = (channel_stats['Conversion_Rate'] * 100).round(2)

        fig_channel = px.bar(
            channel_stats,
            x='Channel_Used',
            y='Conversion_Rate_Pct',
            color='ROI',
            color_continuous_scale='Viridis',
            text='Conversion_Rate_Pct',
            labels={'Conversion_Rate_Pct': '전환율(%)', 'Channel_Used': '채널', 'ROI': '평균 ROI'}
        )
        fig_channel.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig_channel.update_layout(height=400)
        st.plotly_chart(fig_channel, use_container_width=True)

    with chart_col2:
        # 예산 효율성 Scatter 플롯
        st.subheader("획득 비용 vs ROI")
        fig_scatter = px.scatter(
            filtered_marketing,
            x='Acquisition_Cost',
            y='ROI',
            color='Channel_Used',
            size='Clicks',
            hover_data=['Campaign_Type', 'Conversion_Rate'],
            labels={'Acquisition_Cost': '획득 비용($)', 'ROI': 'ROI', 'Channel_Used': '채널'}
        )
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, use_container_width=True)

# 푸터
st.sidebar.markdown("---")
st.sidebar.caption("© 2024 HR & Marketing Dashboard")
