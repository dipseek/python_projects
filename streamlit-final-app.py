import streamlit as st
import os
import base64
from pathlib import Path
import subprocess
import sys
import tempfile

# Page configuration
st.set_page_config(
    page_title="Deepika Saini - LW Summer Internship Program 2025",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Additional CSS and JavaScript to force full width
st.markdown("""
<style>
    /* Override Streamlit's default container width */
    .main .block-container {
        max-width: none !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
</style>
<script>
    // Force code blocks to use full width after page load
    setTimeout(function() {
        const codeBlocks = document.querySelectorAll('[data-testid="stCodeBlock"]');
        codeBlocks.forEach(block => {
            block.style.width = '100%';
            block.style.maxWidth = 'none';
            const innerDiv = block.querySelector('div');
            if (innerDiv) {
                innerDiv.style.width = '100%';
                innerDiv.style.maxWidth = 'none';
            }
            const pre = block.querySelector('pre');
            if (pre) {
                pre.style.width = '100%';
                pre.style.maxWidth = 'none';
            }
        });
    }, 1000);
</script>
""", unsafe_allow_html=True)

# Function to run Python code and capture output
def run_python_code(code, timeout=30):
    """Run Python code and return the output"""
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name
        
        # Set environment variables for headless execution
        env = os.environ.copy()
        env['DISPLAY'] = ':0'  # For GUI applications
        env['PYTHONPATH'] = os.getcwd()
        
        # Run the code with timeout
        result = subprocess.run(
            [sys.executable, temp_file_path],
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            cwd=os.getcwd()
        )
        
        # Clean up the temporary file
        try:
            os.unlink(temp_file_path)
        except:
            pass
        
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode,
            'success': result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            'stdout': '',
            'stderr': 'Code execution timed out after 30 seconds',
            'returncode': -1,
            'success': False
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': f'Error running code: {str(e)}',
            'returncode': -1,
            'success': False
        }

# Custom CSS for better styling
st.markdown("""
<style>
    /* Force full width layout */
    .main .block-container {
        max-width: none !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        width: 100% !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .project-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin-bottom: 1rem;
    }
    .linkedin-embed {
        border: 1px solid #ddd;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .tech-badge {
        background-color: #3498db !important;
        color: white !important;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.2rem;
        display: inline-block;
        border: none;
        text-decoration: none;
    }
    
    /* AGGRESSIVE CODE BLOCK STYLING */
    [data-testid="stCodeBlock"] {
        width: calc(100vw - 4rem) !important;
        max-width: none !important;
        margin-left: -1rem !important;
        margin-right: -1rem !important;
        border-radius: 8px !important;
        border: 2px solid #e9ecef !important;
        background: #f8f9fa !important;
    }
    
    [data-testid="stCodeBlock"] > div {
        width: 100% !important;
        max-width: none !important;
        margin: 0 !important;
        padding: 1rem !important;
    }
    
    [data-testid="stCodeBlock"] pre {
        width: 100% !important;
        max-width: none !important;
        overflow-x: auto !important;
        white-space: pre !important;
        font-size: 0.9rem !important;
        line-height: 1.4 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    [data-testid="stCodeBlock"] code {
        width: 100% !important;
        max-width: none !important;
        display: block !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Fallback for older Streamlit versions */
    .stCodeBlock {
        width: calc(100vw - 4rem) !important;
        max-width: none !important;
        margin-left: -1rem !important;
        margin-right: -1rem !important;
    }
    
    .stCodeBlock > div {
        width: 100% !important;
        max-width: none !important;
    }
    
    .stCodeBlock pre {
        width: 100% !important;
        max-width: none !important;
        overflow-x: auto !important;
    }
    
    .code-container {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 0;
        margin: 1rem -1rem;
        width: calc(100% + 2rem);
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .code-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        font-weight: bold;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .code-content {
        background-color: #ffffff;
        overflow: auto;
        width: 100%;
        max-height: 80vh;
        padding: 1rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem !important;
        }
        .section-header {
            font-size: 1.5rem !important;
        }
        .tech-badge {
            font-size: 0.7rem !important;
            padding: 0.2rem 0.6rem !important;
        }
        [data-testid="stCodeBlock"] {
            width: calc(100vw - 2rem) !important;
            margin-left: -0.5rem !important;
            margin-right: -0.5rem !important;
            font-size: 0.8rem !important;
        }
        .code-container {
            margin: 1rem -0.5rem !important;
            width: calc(100% + 1rem) !important;
        }
    }
    
    /* Error message styling */
    .stAlert > div {
        border-radius: 8px;
    }
    
    /* Responsive design improvements */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem !important;
        }
        .section-header {
            font-size: 1.5rem !important;
        }
        .tech-badge {
            font-size: 0.7rem !important;
            padding: 0.2rem 0.6rem !important;
        }
        .code-container {
            margin: 1rem 0 !important;
            padding: 1rem !important;
            max-height: 50vh !important;
            width: 100% !important;
            min-width: 95% !important;
        }
        .code-header {
            font-size: 1rem !important;
            padding: 0.8rem 1rem !important;
            margin: -1rem -1rem 0.8rem -1rem !important;
        }
        .stCodeBlock {
            font-size: 0.8rem !important;
            max-height: 45vh !important;
            width: 100% !important;
        }
    }
    
    /* Error message styling */
    .stAlert > div {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎓 Menu-Based Streamlit Project")
st.sidebar.markdown("---")

# Navigation menu
menu = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Introduction", "📚 Learnings", "📋 Tasks", "🚀 Mini Projects", "💼 LinkedIn Posts", "🎯 Conclusion"]
)

# Introduction Section
if menu == "🏠 Introduction":
    st.markdown('<h1 class="main-header">Deepika Saini</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Summer Internship Program 2025</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### **Training Details**
    
    **👤 Name:** Deepika Saini  
    **📅 Duration:** 15 June – 31 July 2024  
    **🏢 Organization:** LinuxWorld Pvt. Ltd.  
    **🎯 Field:** Machine Learning  
    
    ### **About the Training**
    
    This comprehensive summer training program covered multiple cutting-edge technologies and concepts in the field of Machine Learning and DevOps. The training encompassed practical hands-on experience with Python programming, Linux administration, Docker containerization, Git version control, Kubernetes orchestration, AWS cloud services, and advanced Machine Learning techniques.
    
    ### **Technologies Covered**
    """)
    
    tech_stack = [
        "Python", "Linux", "Docker", "Machine Learning", 
        "Git", "Kubernetes", "AWS", "Streamlit", "Flask"
    ]
    
    for tech in tech_stack:
        st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # GitHub Profile Section
    st.markdown("### 🔗 GitHub Profile")
    st.markdown("""
    **GitHub:** [@dipseek](https://github.com/dipseek)
    
    **Machine Learning Engineer** based in Jaipur, India

    """)

# Learnings Section
elif menu == "📚 Learnings":
    st.markdown('<h2 class="section-header">Key Learnings</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### **Python Programming**
    - **System Integration:** Learned to read system RAM, send WhatsApp messages, emails, and SMS using Python
    - **Web Automation:** Developed skills in web scraping, posting to social media platforms
    - **Image Processing:** Created digital images and implemented face swapping algorithms
    - **API Integration:** Worked with various APIs for communication and data retrieval
    
    ### **Linux Administration**
    - **Command Line Mastery:** Explored GUI programs and their underlying terminal commands
    - **System Administration:** Enhanced terminal and GUI interfaces in Linux
    - **Process Control:** Understood interrupt signals (Ctrl+C, Ctrl+Z) and process management
    - **Communication Tools:** Sent emails, WhatsApp messages, tweets, and SMS through Linux terminal
    
    ### **Docker & Containerization**
    - **Container Management:** Set up and configured various services in Docker containers
    - **Docker-in-Docker (DIND):** Learned to run Docker inside Docker containers
    - **GUI Applications:** Successfully ran graphical software inside Docker containers
    - **Audio Support:** Implemented sound card access for programs inside Docker
    - **ML Integration:** Ran machine learning models and Flask applications in containers
    
    ### **Git Version Control**
    - **Repository Management:** Created and managed Git repositories
    - **Branching Strategy:** Worked with feature branches and merge operations
    - **Open Source Contribution:** Forked repositories and created pull requests
    - **Collaborative Development:** Learned best practices for team collaboration
    
    ### **Kubernetes Orchestration**
    - **Container Orchestration:** Understood the benefits and use cases of Kubernetes
    - **Case Studies:** Analyzed real-world implementations in various companies
    - **Scalability:** Learned about microservices architecture and deployment strategies
    
    ### **AWS Cloud Services**
    - **EC2 Management:** Launched and terminated instances using Boto3
    - **CloudWatch:** Accessed and analyzed logs from AWS CloudWatch
    - **S3 Storage:** Studied different storage classes and their use cases
    - **Cloud Integration:** Integrated Python applications with AWS services
    
    ### **Machine Learning**
    - **Data Preprocessing:** Explored various data imputation techniques
    - **Feature Engineering:** Understood categorical variable handling and weight management
    - **Model Optimization:** Learned about different initializers and optimizers
    - **Neural Networks:** Studied activation functions and pooling layer relationships
    - **Real-world Applications:** Built practical ML models for salary and house price prediction
    """)

# Tasks Section
elif menu == "📋 Tasks":
    st.markdown('<h2 class="section-header">Completed Tasks</h2>', unsafe_allow_html=True)
    
    # Python Tasks
    st.markdown("### 🐍 Python Tasks")
    python_tasks = [
        ("Read the RAM using Python", "read-ram.py"),
        ("Send WhatsApp message using Python", "send-whatsapp-message.py"),
        ("Send email using Python", "send_email.py"),
        ("Send WhatsApp message without using contact number", None),
        ("Send SMS using Python", "send-sms.py"),
        ("Make a phone call using Python", "make_calls.py"),
        ("Search on Google using Python", "search-web.py"),
        ("Post on Instagram/X (Twitter)/Facebook using Python", "post-insta.py"),
        ("Download entire website data using Python", "download-website-data.py"),
        ("Email without showing email ID", "send_email.py"),
        ("Technical difference between Tuple and List", None),
        ("Create digital image using Python", "create-digital-image3.py"),
        ("Swap faces in two images using Python", "swap_faces.py"),
        ("Menu-based Python application", "menu-based.py"),
        ("Menu-driven Python application", "menu-driven.py"),
        ("Create digital image 1", "create-digital-image1.py"),
        ("Create digital image 2", "create-digital-image2.py")
    ]
    
    for i, (task, filename) in enumerate(python_tasks, 1):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown(f"**{i}.** {task}")
        with col2:
            if filename and os.path.exists(filename):
                if st.button(f"View Code", key=f"python_{i}"):
                    try:
                        if os.path.exists(filename):
                            with open(filename, "r", encoding="utf-8") as f:
                                code_content = f.read()
                                # Use expander for better width control
                                with st.expander(f"📄 {filename}", expanded=True):
                                    # Use text_area which uses full width by default
                                    st.text_area(
                                        label="",
                                        value=code_content,
                                        height=500,
                                        key=f"code_display_{i}",
                                        label_visibility="collapsed"
                                    )
                        else:
                            st.warning(f"⚠️ File '{filename}' not found in the current directory.")
                    except FileNotFoundError:
                        st.error(f"❌ File '{filename}' could not be found.")
                    except PermissionError:
                        st.error(f"❌ Permission denied when trying to read '{filename}'.")
                    except UnicodeDecodeError:
                        st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
                    except Exception as e:
                        st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
            elif filename:
                st.markdown(f"*File: {filename}*")
        with col3:
            if filename and os.path.exists(filename):
                pass # Removed Run Code button
    
    st.markdown("---")
    
    # Linux Tasks
    st.markdown("### 🐧 Linux Tasks")
    linux_tasks = [
        "Write blog post on companies using Linux",
        "Choose 5 GUI programs and find commands working behind them",
        "Add more terminals and GUI interfaces in Linux",
        "Send email, WhatsApp, tweet, and SMS through Linux terminal",
        "Find commands behind Ctrl+C and Ctrl+Z interrupt signals"
    ]
    
    for i, task in enumerate(linux_tasks, 1):
        st.markdown(f"**{i}.** {task}")
    
    st.markdown("---")
    
    # Docker + ML Tasks
    st.markdown("### 🐳 Docker + Machine Learning Tasks")
    docker_tasks = [
        "Create blog on Docker case studies",
        "Run tools/technology in Docker",
        "Set up Apache webserver in Docker",
        "Learn Docker-in-Docker (DIND)",
        "Run graphical software inside Docker",
        "Give sound card access to Docker programs",
        "Run linear regression model inside Docker",
        "Run Flask app inside Docker",
        "Run menu-based Python project inside Docker",
        "Install Firefox browser inside Docker"
    ]
    
    for i, task in enumerate(docker_tasks, 1):
        st.markdown(f"**{i}.** {task}")
    
    st.markdown("---")
    
    # Git Tasks
    st.markdown("### 📝 Git Tasks")
    git_tasks = [
        "Create new folder, initialize Git repo, add file, and commit",
        "Create feature branch, make changes, and merge back to main",
        "Fork repository, clone locally, make changes, and create PR"
    ]
    
    for i, task in enumerate(git_tasks, 1):
        st.markdown(f"**{i}.** {task}")
    
    st.markdown("---")
    
    # Kubernetes Tasks
    st.markdown("### ☸️ Kubernetes Tasks")
    st.markdown("**1.** Create blog on Kubernetes case studies")
    
    st.markdown("---")
    
    # AWS Tasks
    st.markdown("### ☁️ AWS Tasks")
    aws_tasks = [
        "Write blog on AWS use case studies",
        "Launch and terminate EC2 instance using Boto3",
        "Create Boto3 code to access CloudWatch logs",
        "Study different S3 storage classes and create blog"
    ]
    
    for i, task in enumerate(aws_tasks, 1):
        st.markdown(f"**{i}.** {task}")
    
    st.markdown("---")
    
    # Machine Learning Tasks
    st.markdown("### 🤖 Machine Learning Tasks")
    ml_tasks = [
        "Find different techniques of data imputation",
        "Find what happens to weight of dropped category in categorical variable",
        "Search about different initializers and their use cases",
        "Find use cases of optimizers",
        "Find which activation function works with which type of pooling"
    ]
    
    for i, task in enumerate(ml_tasks, 1):
        st.markdown(f"**{i}.** {task}")
    
    st.markdown("---")
    
    # All Available Files Section
    st.markdown("### 📁 All Available Files in Project Folder")
    st.markdown("Click on any file to view its code:")
    
    # Get all Python and notebook files
    try:
        python_files = [f for f in os.listdir('.') if f.endswith(('.py', '.ipynb')) and f != 'summer_training_portfolio.py']
    except PermissionError:
        st.error("❌ Permission denied when trying to list files in the current directory.")
        python_files = []
    except Exception as e:
        st.error(f"❌ Error listing files: {str(e)}")
        python_files = []
    
    # Create columns for better layout
    cols = st.columns(4)
    for i, filename in enumerate(python_files):
        col_idx = i % 4
        with cols[col_idx]:
            st.markdown(f"**{filename}**")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"View", key=f"view_file_{i}"):
                    try:
                        if os.path.exists(filename):
                            with open(filename, "r", encoding="utf-8") as f:
                                code_content = f.read()
                                # Use expander for better width control
                                with st.expander(f"📄 {filename}", expanded=True):
                                    st.text_area(
                                        label="",
                                        value=code_content,
                                        height=500,
                                        key=f"all_files_{i}",
                                        label_visibility="collapsed"
                                    )
                        else:
                            st.warning(f"⚠️ File '{filename}' not found in the current directory.")
                    except FileNotFoundError:
                        st.error(f"❌ File '{filename}' could not be found.")
                    except PermissionError:
                        st.error(f"❌ Permission denied when trying to read '{filename}'.")
                    except UnicodeDecodeError:
                        st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
                    except Exception as e:
                        st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
            with col2:
                pass # Removed Run button

# Mini Projects Section
elif menu == "🚀 Mini Projects":
    st.markdown('<h2 class="section-header">Mini Projects</h2>', unsafe_allow_html=True)
    
    # Project 1: Road Safety Chatbot
    st.markdown("### 🚗 Road Safety Chatbot using Streamlit")
    st.markdown("""
    **Description:** A conversational AI chatbot focused on road safety awareness and guidelines.
    
    **Technologies:** Streamlit, Gemini AI, Python
    
    **Features:**
    - Interactive chat interface
    - Road safety guidelines and tips
    - Real-time responses using AI
    """)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("**File:** RoadSafetyGemini-fixed.py")
    with col2:
        if st.button("View Code", key="road_safety"):
            filename = "RoadSafetyGemini-fixed.py"
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        code_content = f.read()
                        with st.container():
                            with st.expander(f"🚗 {filename} - Road Safety Chatbot", expanded=True):
                                st.text_area(
                                    label="",
                                    value=code_content,
                                    height=500,
                                    key="road_safety_code",
                                    label_visibility="collapsed"
                                )
                else:
                    st.warning(f"⚠️ File '{filename}' not found in the current directory.")
            except FileNotFoundError:
                st.error(f"❌ File '{filename}' could not be found.")
            except PermissionError:
                st.error(f"❌ Permission denied when trying to read '{filename}'.")
            except UnicodeDecodeError:
                st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
            except Exception as e:
                st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
    with col3:
        pass # Removed Run Code button
    
    st.markdown("---")
    
    # Project 2: Automation Panel
    st.markdown("### ⚙️ Automation Panel using Streamlit")
    st.markdown("""
    **Description:** A comprehensive automation panel for various system tasks and operations.
    
    **Technologies:** Streamlit, Python, System Integration
    
    **Features:**
    - System automation tools
    - Task scheduling interface
    - Process management
    """)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("**File:** automation_panel.py")
    with col2:
        if st.button("View Code", key="automation"):
            filename = "automation_panel.py"
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        code_content = f.read()
                        with st.container():
                            with st.expander(f"⚙️ {filename} - Automation Panel", expanded=True):
                                st.text_area(
                                    label="",
                                    value=code_content,
                                    height=500,
                                    key="automation_code",
                                    label_visibility="collapsed"
                                )
                else:
                    st.warning(f"⚠️ File '{filename}' not found in the current directory.")
            except FileNotFoundError:
                st.error(f"❌ File '{filename}' could not be found.")
            except PermissionError:
                st.error(f"❌ Permission denied when trying to read '{filename}'.")
            except UnicodeDecodeError:
                st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
            except Exception as e:
                st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
    with col3:
        pass # Removed Run Code button
    
    st.markdown("---")
    
    # Project 3: Salary Prediction
    st.markdown("### 💰 Salary Prediction Model")
    st.markdown("""
    **Description:** Machine learning model to predict salary based on various features.
    
    **Technologies:** Python, Scikit-learn, Pandas, NumPy
    
    **Features:**
    - Data preprocessing and analysis
    - Feature engineering
    - Model training and evaluation
    - Salary prediction interface
    """)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("**File:** salary_prediction-fixed.py")
    with col2:
        if st.button("View Code", key="salary"):
            filename = "salary_prediction-fixed.py"
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        code_content = f.read()
                        with st.container():
                            with st.expander(f"💰 {filename} - Salary Prediction Model", expanded=True):
                                st.text_area(
                                    label="",
                                    value=code_content,
                                    height=500,
                                    key="salary_code",
                                    label_visibility="collapsed"
                                )
                else:
                    st.warning(f"⚠️ File '{filename}' not found in the current directory.")
            except FileNotFoundError:
                st.error(f"❌ File '{filename}' could not be found.")
            except PermissionError:
                st.error(f"❌ Permission denied when trying to read '{filename}'.")
            except UnicodeDecodeError:
                st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
            except Exception as e:
                st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
    with col3:
        pass # Removed Run Code button
    
    st.markdown("---")
    
    # Project 4: House Price Prediction
    st.markdown("### 🏠 House Price Prediction Model")
    st.markdown("""
    **Description:** Advanced machine learning model for predicting house prices.
    
    **Technologies:** Python, Machine Learning, Data Analysis
    
    **Features:**
    - Comprehensive data analysis
    - Advanced feature selection
    - Model optimization
    - Price prediction with confidence intervals
    """)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("**File:** house_price_pred-fixed.py")
    with col2:
        if st.button("View Code", key="house_price"):
            filename = "house_price_pred-fixed.py"
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        code_content = f.read()
                        with st.container():
                            with st.expander(f"🏠 {filename} - House Price Prediction Model", expanded=True):
                                st.text_area(
                                    label="",
                                    value=code_content,
                                    height=500,
                                    key="house_price_code",
                                    label_visibility="collapsed"
                                )
                else:
                    st.warning(f"⚠️ File '{filename}' not found in the current directory.")
            except FileNotFoundError:
                st.error(f"❌ File '{filename}' could not be found.")
            except PermissionError:
                st.error(f"❌ Permission denied when trying to read '{filename}'.")
            except UnicodeDecodeError:
                st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
            except Exception as e:
                st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
    with col3:
        pass # Removed Run Code button
    
    st.markdown("---")
    
    # Project 5: Career Counselling App
    st.markdown("### 🎯 Career Counselling Application")
    st.markdown("""
    **Description:** Interactive application for career guidance and counseling.
    
    **Technologies:** Streamlit, Python, Career Assessment
    
    **Features:**
    - Career assessment tools
    - Personalized recommendations
    - Interactive questionnaires
    - Career path guidance
    """)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown("**File:** career-counselling-app-fixed.py")
    with col2:
        if st.button("View Code", key="career"):
            filename = "career-counselling-app-fixed.py"
            try:
                if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8") as f:
                        code_content = f.read()
                        with st.container():
                            with st.expander(f"🎯 {filename} - Career Counselling Application", expanded=True):
                                st.text_area(
                                    label="",
                                    value=code_content,
                                    height=500,
                                    key="career_code",
                                    label_visibility="collapsed"
                                )
                else:
                    st.warning(f"⚠️ File '{filename}' not found in the current directory.")
            except FileNotFoundError:
                st.error(f"❌ File '{filename}' could not be found.")
            except PermissionError:
                st.error(f"❌ Permission denied when trying to read '{filename}'.")
            except UnicodeDecodeError:
                st.error(f"❌ Unable to decode '{filename}'. The file may contain non-UTF-8 characters.")
            except Exception as e:
                st.error(f"❌ Unexpected error reading file '{filename}': {str(e)}")
    with col3:
        pass # Removed Run Code button

# LinkedIn Posts Section
elif menu == "💼 LinkedIn Posts":
    st.markdown('<h2 class="section-header">LinkedIn Posts & Content</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 📋 Note about LinkedIn Embeds
    Due to LinkedIn's embedding restrictions, some posts may not display full content in the embedded view. 
    You can click the "View Full Post" links to see the complete content on LinkedIn.
    
    **💡 Tips for better viewing:**
    - Click "View Full Post" links to see complete content
    - Some embeds may show truncated content due to LinkedIn's limitations
    - All posts are accessible via direct LinkedIn links
    """)
    
    # Linux Posts
    st.markdown("### 🐧 Linux Posts")
    
    st.markdown("#### 1. Companies Using Linux - Blog Post")
    st.markdown("""
    **Content:** Explain why companies are using Linux and what benefits they are getting.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7348696391545671681" 
                height="742" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_companies-using-linux-activity-7348696391545671681)** 
        """)
    
    st.markdown("#### 2. GUI Programs in Linux")
    st.markdown("""
    **Content:** Choose 5 GUI programs in Linux and find out the commands working behind them.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7355884418034552832" 
                height="589" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_linux-gui-programs-activity-7355884418034552832)** 
        """)
    
    st.markdown("#### 3. Enhanced Terminal and GUI Interfaces")
    st.markdown("""
    **Content:** Explore methods to enhance terminal and GUI experiences in Linux.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7355928194648076288" 
                height="694" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_linux-terminal-gui-activity-7355928194648076288)** 
        """)
    
    st.markdown("#### 4. Communication through Linux Terminal")
    st.markdown("""
    **Content:** Send an email, WhatsApp message, tweet, and SMS through the Linux terminal.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7355917109509451777" 
                height="676" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_linux-terminal-communication-activity-7355917109509451777)** 
        """)
    
    st.markdown("#### 5. Interrupt Signals in Linux")
    st.markdown("""
    **Content:** Find the command working behind the Ctrl+C and Ctrl+Z interrupt signals.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7352959371309408256" 
                height="515" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_linux-interrupt-signals-activity-7352959371309408256)** 
        """)
    
    st.markdown("---")
    
    # Docker + ML Posts
    st.markdown("### 🐳 Docker + Machine Learning Posts")
    
    st.markdown("#### 1. Docker Case Studies")
    st.markdown("""
    **Content:** Create a blog on a case study of why Docker is used by different companies.
    """)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7351899055565819905" 
                height="2105" width="504" frameborder="0" allowfullscreen="" 
                title="Embedded post"></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **[View Full Post](https://www.linkedin.com/posts/deepika-saini-90663a279_docker-case-studies-activity-7351899055565819905)** 
        """)
    
    st.markdown("#### 2. Running Tools in Docker")
    st.markdown("""
    **Content:** Successfully ran MySQL inside Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7351913046727938049" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 3. Apache Webserver in Docker")
    st.markdown("""
    **Content:** Set up and configure the Apache webserver in Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7351893648927567872" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 4. Docker-in-Docker (DIND)")
    st.markdown("""
    **Content:** Run Docker inside Docker (DIND).
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7350058565455278081" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 5. Graphical Software in Docker")
    st.markdown("""
    **Content:** Install Firefox browser inside Docker with GUI support.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7350060545925926912" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 6. Sound Card Access in Docker")
    st.markdown("""
    **Content:** Give sound card access to any program inside Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7355836590956449794" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 7. Linear Regression in Docker")
    st.markdown("""
    **Content:** Run linear regression model inside Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7350054797858754560" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 8. Flask App in Docker")
    st.markdown("""
    **Content:** Run Flask app inside Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7350057012572934144" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 9. Menu-based Python Project in Docker")
    st.markdown("""
    **Content:** Run menu-based Python project inside Docker.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:7350058034229891072" 
            height="400" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Git Posts
    st.markdown("### 📝 Git Posts")
    
    st.markdown("#### 1. Git Repository Setup")
    st.markdown("""
    **Content:** Create a new folder, initialize it as a Git repository, add a file, and commit it.
    """)
    st.markdown("""
    <a href="https://www.linkedin.com/posts/deepika-saini-90663a279_today-i-completed-a-foundational-git-activity-7348571696511057920-JmJN" 
       target="_blank">View Post</a>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 2. Git Branching and Merging")
    st.markdown("""
    **Content:** Create a new branch called feature1, make some changes in it, and merge it back into the main branch.
    """)
    st.markdown("""
    <a href="https://www.linkedin.com/posts/deepika-saini-90663a279_i-practiced-one-of-the-most-important-version-activity-7348572930848509952-ak6s" 
       target="_blank">View Post</a>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 3. Fork and Pull Request")
    st.markdown("""
    **Content:** Fork an existing repository from GitHub, clone it locally, make some changes, and create a pull request.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7348574048676630528" 
            height="794" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Kubernetes Posts
    st.markdown("### ☸️ Kubernetes Posts")
    
    st.markdown("#### 1. Kubernetes Case Studies")
    st.markdown("""
    **Content:** Create a blog on case studies of why companies use Kubernetes and the benefits they get.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7352664851275505665" 
            height="550" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # AWS Posts
    st.markdown("### ☁️ AWS Posts")
    
    st.markdown("#### 1. AWS Use Case Studies")
    st.markdown("""
    **Content:** Write a blog on the AWS use case studies.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7351926619566981120" 
            height="1460" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 2. S3 Storage Classes")
    st.markdown("""
    **Content:** Study different storage classes of S3 and create a blog.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7351965414249164801" 
            height="1372" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Machine Learning Posts
    st.markdown("### 🤖 Machine Learning Posts")
    
    st.markdown("#### 1. Data Imputation Techniques")
    st.markdown("""
    **Content:** Find different techniques of data imputation.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7356980161948389378" 
            height="670" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 2. Categorical Variable Weight Management")
    st.markdown("""
    **Content:** Find what happens to the weight of dropped category in categorical variable.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7356991043831058434" 
            height="660" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 3. Neural Network Initializers")
    st.markdown("""
    **Content:** Search about different initializers and their use cases & create a blog of it.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7357000640016863232" 
            height="642" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 4. Optimizer Use Cases")
    st.markdown("""
    **Content:** Find the use cases of optimizers & create a blog of it.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7357011418002460673" 
            height="660" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 5. Activation Functions and Pooling")
    st.markdown("""
    **Content:** Find which activation function works with which type of pooling.
    """)
    st.markdown("""
    <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7357012723278233601" 
            height="642" width="504" frameborder="0" allowfullscreen="" 
            title="Embedded post"></iframe>
    """, unsafe_allow_html=True)

# Conclusion Section
elif menu == "🎯 Conclusion":
    st.markdown('<h2 class="section-header">Internship Conclusion</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ### **🎓 Summer Summary**
    
    This comprehensive summer training program at **LinuxWorld Pvt. Ltd.** has been an incredible journey of learning and growth. Over the course of **23 June – 31 July 2024**, I have gained hands-on experience with cutting-edge technologies and developed practical skills that are highly relevant in today's tech industry.
    
    ### **📈 Key Achievements**
    
    **✅ Completed 50+ Tasks** across multiple technology domains  
    **✅ Built 5 Mini Projects** demonstrating practical application  
    **✅ Created 20+ LinkedIn Posts** sharing knowledge and experiences  
    **✅ Mastered 8+ Technologies** from basics to advanced concepts  
    **✅ Developed Real-world Applications** using modern frameworks
    
    ### **🛠️ Technical Skills Acquired**
    
    **Programming & Automation:**
    - Python programming with system integration
    - Web automation and API development
    - Image processing and computer vision
    
    **DevOps & Cloud:**
    - Linux system administration
    - Docker containerization and orchestration
    - Git version control and collaboration
    - Kubernetes deployment and management
    - AWS cloud services and automation
    
    **Machine Learning:**
    - Data preprocessing and feature engineering
    - Model development and optimization
    - Neural network architecture design
    - Real-world ML application development
    
    ### **🚀 Projects Completed**
    
    1. **Road Safety Chatbot** - AI-powered conversational interface
    2. **Automation Panel** - Streamlit-based system automation tool
    3. **Salary Prediction Model** - ML model for salary forecasting
    4. **House Price Prediction** - Advanced regression analysis
    5. **Career Counselling App** - Interactive career guidance system
    
    ### **💡 Learning Outcomes**
    
    - **Practical Experience:** Gained hands-on experience with real-world tools and technologies
    - **Problem Solving:** Developed strong analytical and problem-solving skills
    - **Documentation:** Learned to create comprehensive documentation and share knowledge
    - **Collaboration:** Understood the importance of version control and team collaboration
    - **Cloud Computing:** Acquired skills in modern cloud infrastructure and deployment
    
    ### **🎯 Future Applications**
    
    The skills acquired during this training will be invaluable for:
    - **Software Development** roles requiring full-stack capabilities
    - **DevOps Engineering** positions focusing on automation and deployment
    - **Machine Learning** careers in data science and AI
    - **Cloud Architecture** roles in cloud-native development
    - **System Administration** positions in Linux environments
    
    ### **🙏 Acknowledgments**
    
    I would like to express my sincere gratitude to:
    - **LinuxWorld Pvt. Ltd.** for providing this excellent learning opportunity
    - **Training Mentors** for their guidance and support throughout the program
    - **Fellow Trainees** for collaborative learning and knowledge sharing
    
    ### **📊 Training Statistics**
    
    | Category | Count |
    |----------|-------|
    | Python Tasks | 13 |
    | Linux Tasks | 5 |
    | Docker + ML Tasks | 10 |
    | Git Tasks | 3 |
    | Kubernetes Tasks | 1 |
    | AWS Tasks | 4 |
    | ML Tasks | 5 |
    | Mini Projects | 5 |
    | LinkedIn Posts | 20+ |
    
    **Total Tasks Completed: 46+**
    
    This training has been a transformative experience that has equipped me with the skills and confidence to pursue a successful career in technology. The combination of theoretical knowledge and practical application has provided a solid foundation for future growth and development in the field of Machine Learning and DevOps.
    """)
    
    # Contact Information
    st.markdown("---")
    st.markdown("""
    ### **📞 Contact Information**
    
    **Name:** Deepika Saini  
    **Email:** dipseek5@gmail.com  
    **LinkedIn:** www.linkedin.com/in/deepika-saini-90663a279  
    **GitHub:** https://github.com/dipseek  
    
    *Ready to contribute to innovative projects and continue learning!*
    """)

# Default case for menu navigation
else:
    st.error("⚠️ Unknown menu selection. Please select a valid option from the sidebar.")
    st.markdown("### Available Sections:")
    st.markdown("""
    - 🏠 Introduction
    - 📚 Learnings  
    - 📋 Tasks
    - 🚀 Mini Projects
    - 💼 LinkedIn Posts
    - 🎯 Conclusion
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8rem;'>
    <p>Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
