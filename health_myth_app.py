import streamlit as st
import pandas as pd
from datetime import datetime
import time

# ============================================================================
# PAGE CONFIG - FULL WIDTH CUSTOMIZATION
# ============================================================================
st.set_page_config(
    page_title="Health Myth Buster AI | Hack2Skill",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# COMPREHENSIVE CSS STYLING (ENTERPRISE DESIGN SYSTEM)
# ============================================================================
st.markdown("""
<style>
    /* Root Variables */
    :root {
        --primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --primary-dark: #5568d3;
        --success: #10b981;
        --danger: #ef4444;
        --warning: #f59e0b;
        --info: #3b82f6;
        --light-bg: #f8fafc;
        --dark-text: #1e293b;
        --light-text: #64748b;
        --border-color: #e2e8f0;
        --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.15);
    }
    
    /* Main App Styling */
    .main {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2rem;
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    
    /* Header Container - Premium Gradient */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2.5rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 2.5rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 500px;
        height: 500px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(30px); }
    }
    
    .header-container h1 {
        margin: 0;
        font-size: 3rem;
        font-weight: 800;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }
    
    .header-container .tagline {
        margin: 0.8rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.95;
        position: relative;
        z-index: 1;
        font-weight: 300;
    }
    
    .header-container .hackathon-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        margin-top: 1rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        z-index: 1;
    }
    
    /* Stats Cards - Enhanced */
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
        border-color: #667eea;
    }
    
    .stat-card-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .stat-card-label {
        color: var(--light-text);
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        color: var(--dark-text);
        padding-bottom: 0.5rem;
        border-bottom: 3px solid var(--primary);
        display: inline-block;
    }
    
    /* Input Area - Premium */
    .input-container {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
        border: 2px solid var(--border-color);
        margin: 1.5rem 0;
        transition: all 0.3s ease;
    }
    
    .input-container:focus-within {
        border-color: #667eea;
        box-shadow: 0 2px 20px rgba(102, 126, 234, 0.15);
    }
    
    /* Quick Test Buttons - Grid Layout */
    .quick-test-btn {
        background: white;
        border: 2px solid var(--border-color);
        border-radius: 12px;
        padding: 1.2rem 1rem;
        margin: 0.6rem 0;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-weight: 500;
        font-size: 0.95rem;
        text-align: left;
        box-shadow: var(--shadow-sm);
    }
    
    .quick-test-btn:hover {
        background: linear-gradient(135deg, #667eea15, #764ba215);
        border-color: #667eea;
        transform: translateX(8px);
        box-shadow: var(--shadow-md);
    }
    
    .quick-test-btn:active {
        transform: scale(0.98);
    }
    
    /* Verdict Cards - Color-Coded */
    .verdict-true {
        border-left: 6px solid var(--success);
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        padding: 1.8rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);
    }
    
    .verdict-false {
        border-left: 6px solid var(--danger);
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
        padding: 1.8rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.1);
    }
    
    .verdict-partial {
        border-left: 6px solid var(--warning);
        background: linear-gradient(135deg, #fffbf0 0%, #fed7aa 100%);
        padding: 1.8rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.1);
    }
    
    .verdict-card-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .verdict-card-content {
        font-size: 0.95rem;
        line-height: 1.6;
        color: var(--dark-text);
    }
    
    /* Risk Level Badge */
    .risk-safe { background: linear-gradient(135deg, #10b981, #059669); color: white; }
    .risk-caution { background: linear-gradient(135deg, #f59e0b, #d97706); color: white; }
    .risk-dangerous { background: linear-gradient(135deg, #ef4444, #dc2626); color: white; }
    
    .risk-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    
    /* Analysis History - Sidebar Enhancement */
    .history-item {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.8rem 0;
        border-left: 4px solid #667eea;
        box-shadow: var(--shadow-sm);
        transition: all 0.3s ease;
    }
    
    .history-item:hover {
        transform: translateX(5px);
        box-shadow: var(--shadow-md);
    }
    
    .history-verdict {
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }
    
    .history-claim {
        color: var(--light-text);
        font-size: 0.85rem;
        margin: 0.3rem 0;
    }
    
    .history-time {
        color: #9ca3af;
        font-size: 0.75rem;
        font-style: italic;
    }
    
    /* Divider Enhancement */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(to right, transparent, var(--border-color), transparent);
        margin: 2rem 0;
    }
    
    /* Footer Enhancement */
    .footer-text {
        text-align: center;
        color: var(--light-text);
        font-size: 0.85rem;
        padding: 2rem 0;
        border-top: 1px solid var(--border-color);
        margin-top: 2rem;
    }
    
    .footer-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea15, #764ba215);
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        margin: 0.5rem;
        font-weight: 500;
        border: 1px solid var(--border-color);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    }
    
    /* Smooth Transitions */
    * {
        transition: all 0.3s ease;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .header-container h1 {
            font-size: 2rem;
        }
        
        .stat-card-value {
            font-size: 2rem;
        }
        
        .section-header {
            font-size: 1.3rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================
if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

if "verdict_counts" not in st.session_state:
    st.session_state.verdict_counts = {"TRUE": 0, "FALSE": 0, "PARTIALLY TRUE": 0}

if "total_analyses" not in st.session_state:
    st.session_state.total_analyses = 0

# ============================================================================
# SNOWFLAKE CONNECTION & CORTEX FUNCTION
# ============================================================================
conn = st.connection("snowflake")

def cortex_complete(model: str, prompt: str) -> str:
    """Call Snowflake Cortex COMPLETE function via SQL"""
    safe_prompt = prompt.replace("'", "''")
    sql = f"""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
      '{model}',
      '{safe_prompt}'
    ) AS RESPONSE;
    """
    try:
        df = conn.query(sql)
        return df.iloc[0]["RESPONSE"]
    except Exception as e:
        raise Exception(f"Cortex API Error: {str(e)}")

def extract_verdict(response: str) -> str:
    """Extract verdict from AI response"""
    if "**VERDICT:**" in response:
        verdict_section = response.split("**VERDICT:**")[1].split("\n")[0].strip()
        if "TRUE" in verdict_section.upper() and "FALSE" not in verdict_section.upper():
            return "TRUE"
        elif "FALSE" in verdict_section.upper():
            return "FALSE"
        else:
            return "PARTIALLY TRUE"
    return "UNKNOWN"

def extract_risk_level(response: str) -> str:
    """Extract risk level from AI response"""
    if "**RISK LEVEL:**" in response:
        risk_section = response.split("**RISK LEVEL:**")[1].split("\n")[0].strip()
        return risk_section
    return "Unknown"

# ============================================================================
# PREMIUM HEADER
# ============================================================================
st.markdown("""
<div class="header-container">
    <h1>🩺 Health Myth Buster AI</h1>
    <p class="tagline">AI-Powered Medical Fact-Checking | Combat Health Misinformation in Real-Time</p>
    <div class="hackathon-badge">🏆 Hack2Skill AI for Good 2025 | Open Innovation Category</div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# ENHANCED STATS DASHBOARD
# ============================================================================
st.markdown('<div class="section-header">📊 Analysis Dashboard</div>', unsafe_allow_html=True)

stat_cols = st.columns(4, gap="medium")

with stat_cols[0]:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-card-label">✅ Verified True</div>
        <div class="stat-card-value">{st.session_state.verdict_counts['TRUE']}</div>
    </div>
    """, unsafe_allow_html=True)

with stat_cols[1]:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-card-label">❌ Debunked False</div>
        <div class="stat-card-value">{st.session_state.verdict_counts['FALSE']}</div>
    </div>
    """, unsafe_allow_html=True)

with stat_cols[2]:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-card-label">⚠️ Partially True</div>
        <div class="stat-card-value">{st.session_state.verdict_counts['PARTIALLY TRUE']}</div>
    </div>
    """, unsafe_allow_html=True)

with stat_cols[3]:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-card-label">📈 Total Analyzed</div>
        <div class="stat-card-value">{sum(st.session_state.verdict_counts.values())}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# INPUT SECTION
# ============================================================================
st.markdown('<div class="section-header">🔍 Verify a Claim</div>', unsafe_allow_html=True)
st.write("Enter any health rumor, home remedy, or viral wellness claim. Our AI will verify it instantly.")

st.markdown('<div class="input-container">', unsafe_allow_html=True)

with st.form(key="myth_form", clear_on_submit=True):
    user_claim = st.text_area(
        label="Health claim",
        placeholder="Type a health claim... Example: 'Does drinking warm lemon water cure cancer?'",
        height=90,
        label_visibility="collapsed",
        max_chars=500
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 1])
    
    with col_btn1:
        submit_btn = st.form_submit_button("✨ Verify with AI", use_container_width=True, type="primary")
    
    with col_btn2:
        clear_btn = st.form_submit_button("🔄 Clear Input", use_container_width=True)
    
    with col_btn3:
        st.write("")  # Spacer

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# QUICK TEST SECTION (ENHANCED GRID)
# ============================================================================
st.markdown('<div class="section-header">⚡ Quick Test Claims</div>', unsafe_allow_html=True)
st.write("Click any claim to instantly verify. Perfect for demo purposes:")

quick_claims = [
    ("🚫 Drinking bleach cures COVID-19", "Drinking bleach can cure COVID-19"),
    ("💊 Antibiotics treat common colds", "Antibiotics cure the common cold"),
    ("💉 Vaccines cause autism", "Vaccines cause autism"),
    ("🧼 Hand washing prevents infections", "Washing hands prevents spread of infections"),
    ("🦴 Cracking knuckles causes arthritis", "Cracking knuckles causes arthritis")
]

quick_claim_selected = None

# Create 3-column grid for buttons
grid_cols = st.columns(3, gap="small")

for idx, (display_text, actual_claim) in enumerate(quick_claims):
    with grid_cols[idx % 3]:
        if st.button(display_text, use_container_width=True, key=f"quick_{idx}"):
            quick_claim_selected = actual_claim
            user_claim = actual_claim
            submit_btn = True

# Use quick claim if selected
if quick_claim_selected:
    user_claim = quick_claim_selected

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================================
# PROCESSING & ENHANCED OUTPUT
# ============================================================================
if submit_btn and user_claim.strip():
    with st.spinner("🧠 Analyzing claim with Snowflake Cortex AI..."):
        time.sleep(0.5)  # Smooth UX
        try:
            prompt = f"""
You are a careful, evidence-based medical assistant. Your job is to verify health claims.

CLAIM: "{user_claim}"

IMPORTANT INSTRUCTIONS:
- Only use "PARTIALLY TRUE" if there is genuine scientific debate or conditions.
- If the claim is clearly false, use "FALSE" and explain why it's dangerous.
- If the claim is broadly correct, use "TRUE".

Provide your response in this exact format:

VERDICT: [TRUE / FALSE / PARTIALLY TRUE]

**EXPLANATION:** [2-3 sentences in simple English explaining the scientific truth]

**RISK LEVEL:** [Safe / Caution / Dangerous]

**MEDICAL ADVICE:** [If harmful, provide a warning. Otherwise explain the evidence.]

**SOURCES:** [Mention evidence categories: WHO, CDC, peer-reviewed studies, medical consensus]
"""
            
            response = cortex_complete("llama3-70b", prompt)
            
            # Extract metadata
            verdict = extract_verdict(response)
            risk_level = extract_risk_level(response)
            
            # Update tracking
            if verdict in st.session_state.verdict_counts:
                st.session_state.verdict_counts[verdict] += 1
            
            st.session_state.analysis_history.append({
                "claim": user_claim,
                "verdict": verdict,
                "risk": risk_level,
                "timestamp": datetime.now()
            })
            
            # Display result with enhanced styling
            st.success("✅ Analysis Complete!", icon="✅")
            
            # Determine styling
            if "FALSE" in verdict:
                verdict_class = "verdict-false"
                verdict_icon = "❌"
            elif "TRUE" in verdict and "PARTIALLY" not in verdict:
                verdict_class = "verdict-true"
                verdict_icon = "✅"
            else:
                verdict_class = "verdict-partial"
                verdict_icon = "⚠️"
            
            # Risk level styling
            if "Safe" in risk_level:
                risk_class = "risk-safe"
            elif "Caution" in risk_level:
                risk_class = "risk-caution"
            else:
                risk_class = "risk-dangerous"
            
            # Display result card
            result_container = st.container(border=False)
            with result_container:
                st.markdown(f"""
<div class="{verdict_class}">
    <div class="verdict-card-content">
        {response}
        <br><br>
        <span class="risk-badge {risk_class}">⚠️ Risk Level: {risk_level}</span>
    </div>
</div>
""", unsafe_allow_html=True)
            
            # Enhanced timestamp
            col_time1, col_time2 = st.columns([3, 1])
            with col_time1:
                st.caption(f"🔬 Analyzed using Snowflake Cortex (Llama 3 70B) | {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}")
            
        except Exception as e:
            st.error("❌ Analysis Failed", icon="❌")
            with st.expander("See technical details"):
                st.code(str(e), language="text")

elif submit_btn and not user_claim.strip():
    st.warning("⚠️ Please enter a health claim to verify", icon="⚠️")

# ============================================================================
# SIDEBAR - ENHANCED
# ============================================================================
with st.sidebar:
    st.markdown("### ℹ️ About Health Myth Buster")
    
    with st.expander("📖 How It Works", expanded=True):
        st.markdown("""
1. **Enter Claim** - Type any health rumor or wellness claim
2. **AI Analysis** - Snowflake Cortex analyzes against medical evidence
3. **Get Verdict** - TRUE, FALSE, or PARTIALLY TRUE
4. **Risk Assessment** - See potential health impact
5. **Learn** - Understand the medical science behind the verdict
        """)
    
    with st.expander("⚠️ Disclaimer"):
        st.warning("""
**NOT Medical Advice**: This tool provides general information only.

**Always consult** a qualified healthcare provider for:
- Medical diagnosis
- Treatment decisions  
- Emergency situations

**Medical Emergencies**: Call emergency services immediately.
        """)
    
    with st.expander("🛠️ Tech Stack"):
        st.markdown("""
- **AI Model**: Snowflake Cortex (Llama 3 70B)
- **UI**: Streamlit
- **Database**: Snowflake (Cloud Data Platform)
- **Category**: Open Innovation (Hack2Skill)
        """)
    
    st.divider()
    
    st.markdown("### 📝 Recent Analyses")
    
    if st.session_state.analysis_history:
        for idx, item in enumerate(reversed(st.session_state.analysis_history[-5:]), 1):
            st.markdown(f"""
<div class="history-item">
    <div class="history-verdict">{idx}. {item['verdict']} {item['verdict'].replace('TRUE', '✅').replace('FALSE', '❌').replace('PARTIALLY', '⚠️')}</div>
    <div class="history-claim">"{item['claim'][:40]}..."</div>
    <div class="history-time">{item['timestamp'].strftime('%H:%M:%S')}</div>
</div>
""", unsafe_allow_html=True)
    else:
        st.info("💡 No analyses yet. Start by testing a claim!")

# ============================================================================
# PREMIUM FOOTER
# ============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer-text">
    <b>Health Myth Buster AI</b>
    <br>
    <div class="footer-badge">🏆 Hack2Skill AI for Good 2025</div>
    <div class="footer-badge">🤖 Powered by Snowflake Cortex</div>
    <div class="footer-badge">🔒 Privacy First</div>
    <br>
    <p style="margin-top: 1rem;">
    Combat medical misinformation with AI-powered fact-checking | Built to save lives
    </p>
</div>
""", unsafe_allow_html=True)