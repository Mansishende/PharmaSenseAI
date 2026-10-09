import streamlit as st
import pandas as pd
from pathlib import Path

# ============================================================
# PHARMASENSEAI - PHARMACEUTICAL RESEARCH INTELLIGENCE
# ============================================================

st.set_page_config(
    page_title="PharmaSenseAI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown("""
<style>
/* ---------- GLOBAL ---------- */
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(45,212,191,0.08), transparent 28%),
        radial-gradient(circle at 90% 15%, rgba(59,130,246,0.08), transparent 25%),
        linear-gradient(135deg, #07111f 0%, #0b1728 52%, #06101d 100%);
    color: #f8fafc;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #081321 0%, #0b1829 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #dbe7f3;
}

/* ---------- HEADER ---------- */
.brand {
    font-size: 44px;
    font-weight: 850;
    letter-spacing: -1.8px;
    line-height: 1.05;
    margin-bottom: 8px;
}

.brand span {
    color: #2dd4bf;
}

.hero-subtitle {
    color: #9fb1c4;
    font-size: 17px;
    margin-bottom: 28px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(45,212,191,0.10);
    border: 1px solid rgba(45,212,191,0.25);
    color: #5eead4;
    font-size: 13px;
    font-weight: 700;
}

/* ---------- CARDS ---------- */
.card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.085);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.18);
}streamlit run src/app.py

.stat-card {
    background: linear-gradient(
        145deg,
        rgba(45,212,191,0.13),
        rgba(255,255,255,0.035)
    );
    border: 1px solid rgba(45,212,191,0.18);
    border-radius: 18px;
    padding: 21px;
    min-height: 130px;
}

.stat-icon {
    font-size: 27px;
}

.stat-number {
    font-size: 30px;
    font-weight: 850;
    margin-top: 5px;
    color: #f8fafc;
}

.stat-label {
    color: #9fb1c4;
    font-size: 13px;
    margin-top: 4px;
}

.section-title {
    font-size: 27px;
    font-weight: 800;
    margin: 28px 0 7px 0;
}

.section-caption {
    color: #8fa4b9;
    margin-bottom: 18px;
}

.profile-card {
    background: linear-gradient(
        145deg,
        rgba(15,23,42,0.92),
        rgba(15,36,54,0.80)
    );
    border: 1px solid rgba(45,212,191,0.18);
    border-radius: 22px;
    padding: 28px;
    margin-top: 12px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.22);
}

.profile-id {
    color: #5eead4;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.profile-name {
    font-size: 32px;
    font-weight: 850;
    margin-top: 5px;
}

.info-box {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.075);
    border-radius: 15px;
    padding: 17px;
    min-height: 90px;
    margin-bottom: 12px;
}

.info-label {
    color: #8196ab;
    font-size: 11px;
    font-weight: 750;
    letter-spacing: 0.7px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.info-value {
    color: #f8fafc;
    font-size: 16px;
    font-weight: 650;
    word-break: break-word;
}

/* ---------- SEARCH ---------- */
.search-card {
    background: linear-gradient(
        145deg,
        rgba(14,116,144,0.12),
        rgba(255,255,255,0.035)
    );
    border: 1px solid rgba(56,189,248,0.14);
    border-radius: 20px;
    padding: 24px;
    margin-top: 20px;
}

div[data-baseweb="input"] {
    border-radius: 12px;
}

div[data-baseweb="select"] > div {
    border-radius: 12px;
}

.stButton > button {
    border-radius: 12px;
    min-height: 43px;
    font-weight: 750;
    border: 1px solid rgba(45,212,191,0.25);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(45,212,191,0.18);
}

/* ---------- ALERT ---------- */
.success-box {
    padding: 14px 17px;
    border-radius: 13px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.20);
    color: #86efac;
    font-weight: 650;
    margin: 14px 0;
}

.empty-box {
    padding: 24px;
    border-radius: 18px;
    background: rgba(255,255,255,0.035);
    border: 1px dashed rgba(255,255,255,0.13);
    text-align: center;
    color: #91a4b8;
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #64788d;
    font-size: 12px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.06);
}

/* Hide Streamlit chrome */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "synthetic_dataset"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def load_csv(filename):
    """Load a CSV safely."""
    path = DATA_DIR / filename

    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def find_column(df, possible_names):
    """Find a column without depending on exact capitalization."""
    if df.empty:
        return None

    normalized = {
        str(col).strip().lower().replace(" ", "_"): col
        for col in df.columns
    }

    for name in possible_names:
        key = name.lower().strip().replace(" ", "_")
        if key in normalized:
            return normalized[key]

    return None


def clean_value(value):
    """Convert missing/NaN values into friendly text."""
    if pd.isna(value):
        return "Not available"

    text = str(value).strip()

    if not text:
        return "Not available"

    return text


def display_info_card(label, value):
    st.markdown(
        f"""
        <div class="info-box">
            <div class="info-label">{label}</div>
            <div class="info-value">{clean_value(value)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# LOAD DATA
# ============================================================

compounds = load_csv("compounds.csv")
clinical_trials = load_csv("clinical_trials.csv")
adverse_events = load_csv("adverse_events.csv")
lab_results = load_csv("lab_results.csv")
research_documents = load_csv("research_documents.csv")
trial_sites = load_csv("trial_sites.csv")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="font-size:30px;font-weight:850;">
            🧬 PharmaSense<span style="color:#2dd4bf;">AI</span>
        </div>
        <div style="color:#8196ab;margin-top:5px;">
            Research Intelligence
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### 🧭 Navigation")

    page = st.radio(
        "Choose a section",
        [
            "🏠 Overview",
            "🔎 Compound Search",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    st.markdown("### 📁 Data Status")

    if not compounds.empty:
        st.success(f"Compounds loaded: {len(compounds):,}")
    else:
        st.warning("compounds.csv not found")

    st.caption("PharmaSenseAI • Research Platform")


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="brand">🧬 PharmaSense<span>AI</span></div>
    <div class="hero-subtitle">
        Pharmaceutical Research Intelligence Platform
        · Compound Discovery · Research Analytics
    </div>
    <span class="badge">● DATA SYSTEM ONLINE</span>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# OVERVIEW PAGE
# ============================================================

if page == "🏠 Overview":

    st.markdown(
        """
        <div class="section-title">Research Overview</div>
        <div class="section-caption">
            A quick view of the pharmaceutical research knowledge base.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Dashboard metrics
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">🧬</div>
                <div class="stat-number">{len(compounds):,}</div>
                <div class="stat-label">Compounds</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">🧪</div>
                <div class="stat-number">{len(clinical_trials):,}</div>
                <div class="stat-label">Clinical Trial Records</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">⚠️</div>
                <div class="stat-number">{len(adverse_events):,}</div>
                <div class="stat-label">Adverse Event Records</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-icon">🔬</div>
                <div class="stat-number">{len(trial_sites):,}</div>
                <div class="stat-label">Trial Site Records</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Dataset cards
    left, right = st.columns(2)

    with left:
        st.markdown(
            """
            <div class="card">
                <div style="font-size:22px;font-weight:800;">
                    🔬 Research Intelligence
                </div>
                <p style="color:#91a4b8;">
                    Explore pharmaceutical compounds, targets,
                    therapeutic areas, clinical research and
                    related datasets from one interface.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="card">
                <div style="font-size:22px;font-weight:800;">
                    🤖 AI-Ready Architecture
                </div>
                <p style="color:#91a4b8;">
                    The platform is structured so that intelligent
                    search, analytics and AI research assistance can
                    be added on top of the existing dataset.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Quick action
    st.markdown(
        """
        <div class="search-card">
            <div style="font-size:23px;font-weight:800;">
                🔎 Find a Compound
            </div>
            <div style="color:#91a4b8;margin-top:5px;">
                Use Compound Search from the sidebar to explore a compound profile.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# COMPOUND SEARCH PAGE
# ============================================================

elif page == "🔎 Compound Search":

    st.markdown(
        """
        <div class="section-title">🔎 Compound Discovery</div>
        <div class="section-caption">
            Search the pharmaceutical knowledge base using a compound ID.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if compounds.empty:
        st.error(
            "The compounds dataset could not be loaded. "
            "Please check that data/synthetic_dataset/compounds.csv exists."
        )
        st.stop()

    id_column = find_column(
        compounds,
        [
            "compound_id",
            "compoundid",
            "compound id",
            "id",
        ],
    )

    if id_column is None:
        st.error(
            "I could not find a Compound ID column in compounds.csv. "
            f"Available columns: {', '.join(map(str, compounds.columns))}"
        )
        st.stop()

    # Search area
    st.markdown('<div class="search-card">', unsafe_allow_html=True)

    search_col, button_col = st.columns([5, 1])

    with search_col:
        compound_id = st.text_input(
            "Compound ID",
            placeholder="Example: CMP-0009",
            label_visibility="collapsed",
            key="compound_search_input",
        )

    with button_col:
        search_clicked = st.button(
            "🔍 Search",
            use_container_width=True,
            type="primary",
        )

    st.markdown(
        """
        <div style="color:#7f93a8;font-size:13px;margin-top:8px;">
            Example: CMP-0009
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # Search
    if search_clicked:

        search_value = compound_id.strip()

        if not search_value:
            st.warning("Please enter a Compound ID.")

        else:
            matches = compounds[
                compounds[id_column]
                .astype(str)
                .str.strip()
                .str.lower()
                == search_value.lower()
            ]

            if matches.empty:
                st.error(
                    f"No compound was found with ID: {search_value}"
                )

            else:
                st.session_state["selected_compound"] = matches.iloc[0].to_dict()


    # Show selected compound
    if "selected_compound" in st.session_state:

        compound = st.session_state["selected_compound"]

        actual_id = clean_value(compound.get(id_column))

        name_column = find_column(
            compounds,
            [
                "compound_name",
                "compoundname",
                "compound name",
                "name",
            ],
        )

        name = (
            clean_value(compound.get(name_column))
            if name_column
            else "Pharmaceutical Compound"
        )

        st.markdown(
            f"""
            <div class="success-box">
                ✓ Compound {actual_id} found successfully
            </div>

            <div class="profile-card">
                <div class="profile-id">COMPOUND PROFILE</div>
                <div class="profile-name">{name}</div>
                <div style="color:#6ee7d8;margin-top:6px;">
                    {actual_id}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ----------------------------------------------------
        # Important fields
        # ----------------------------------------------------

        preferred_fields = [
            ("Chemical Class", [
                "chemical_class",
                "chemicalclass",
                "chemical class",
                "class",
            ]),
            ("Therapeutic Area", [
                "therapeutic_area",
                "therapeuticarea",
                "therapeutic area",
            ]),
            ("Target Protein", [
                "target_protein",
                "targetprotein",
                "target protein",
                "target",
            ]),
            ("Discovery Phase", [
                "discovery_phase",
                "discoveryphase",
                "discovery phase",
                "phase",
            ]),
            ("Molecular Weight", [
                "molecular_weight_da",
                "molecular_weight",
                "molecularweight",
                "molecular weight",
                "molecular weight da",
            ]),
            ("Mechanism of Action", [
                "mechanism_of_action",
                "mechanismofaction",
                "mechanism of action",
                "moa",
            ]),
        ]

        found_fields = []

        for label, possible_columns in preferred_fields:
            column = find_column(compounds, possible_columns)

            if column is not None:
                found_fields.append(
                    (label, clean_value(compound.get(column)))
                )

        if found_fields:

            st.markdown(
                """
                <div class="section-title">🧬 Compound Intelligence</div>
                """,
                unsafe_allow_html=True,
            )

            # Display in groups of 3
            for start in range(0, len(found_fields), 3):

                row = found_fields[start:start + 3]

                columns = st.columns(len(row))

                for col, (label, value) in zip(columns, row):

                    with col:
                        display_info_card(label, value)

        # ----------------------------------------------------
        # Additional fields
        # ----------------------------------------------------

        excluded = set()

        if id_column:
            excluded.add(id_column)

        if name_column:
            excluded.add(name_column)

        for _, possible_columns in preferred_fields:
            column = find_column(compounds, possible_columns)
            if column:
                excluded.add(column)

        extra_fields = []

        for column in compounds.columns:

            if column in excluded:
                continue

            value = clean_value(compound.get(column))

            if value != "Not available":
                extra_fields.append(
                    (str(column).replace("_", " ").title(), value)
                )

        if extra_fields:

            with st.expander("📋 View Additional Compound Data"):

                for start in range(0, len(extra_fields), 2):

                    row = extra_fields[start:start + 2]

                    columns = st.columns(len(row))

                    for col, (label, value) in zip(columns, row):

                        with col:
                            display_info_card(label, value)

        # ----------------------------------------------------
        # Related datasets
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="section-title">📊 Related Research</div>
            <div class="section-caption">
                Records available in the connected research datasets.
            </div>
            """,
            unsafe_allow_html=True,
        )

        related_datasets = {
            "Clinical Trials": clinical_trials,
            "Adverse Events": adverse_events,
            "Lab Results": lab_results,
            "Research Documents": research_documents,
            "Trial Sites": trial_sites,
        }

        related_cols = st.columns(5)

        for col, (label, dataframe) in zip(
            related_cols,
            related_datasets.items()
        ):

            with col:
                st.markdown(
                    f"""
                    <div class="info-box" style="text-align:center;">
                        <div class="info-label">{label}</div>
                        <div class="info-value">
                            {len(dataframe):,}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # ----------------------------------------------------
        # Full raw record
        # ----------------------------------------------------

        with st.expander("🔍 View Complete Compound Record"):

            display_df = pd.DataFrame(
                [
                    {
                        str(key).replace("_", " ").title(): clean_value(value)
                        for key, value in compound.items()
                    }
                ]
            )

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🧬 PharmaSenseAI &nbsp;•&nbsp;
        Pharmaceutical Research Intelligence Platform
        <br>
        Built for compound discovery and research intelligence.
    </div>
    """,
    unsafe_allow_html=True,
)
