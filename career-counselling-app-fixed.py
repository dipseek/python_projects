import sys

def fetch_career_info_demo(query):
    """Demonstrate career information fetching without external dependencies"""
    print(f"Searching for career information: {query}")
    
    # Simulate web scraping results
    demo_data = {
        "devops engineer": "DevOps Engineers bridge development and operations, focusing on automation, CI/CD pipelines, and infrastructure management.",
        "data scientist": "Data Scientists analyze complex data to help organizations make better decisions using statistical and machine learning techniques.",
        "software engineer": "Software Engineers design, develop, and maintain software applications using various programming languages and frameworks.",
        "machine learning engineer": "ML Engineers build and deploy machine learning models, working with data pipelines and model optimization.",
        "cybersecurity analyst": "Cybersecurity Analysts protect systems from digital attacks, monitor security threats, and implement security measures."
    }
    
    query_lower = query.lower()
    for key, value in demo_data.items():
        if key in query_lower:
            return value
    
    return "Career information not found in demo database. In a real application, this would fetch data from Wikipedia or other sources."

def career_counselling_demo():
    """Demonstrate career counselling functionality without external dependencies"""
    print("=" * 60)
    print("AI CAREER COUNSELLOR DEMONSTRATION")
    print("=" * 60)
    
    print("\nAvailable Career Queries:")
    print("1. Should I become a DevOps Engineer?")
    print("2. What does a Data Scientist do?")
    print("3. How to become a Software Engineer?")
    print("4. Machine Learning Engineer career path")
    print("5. Cybersecurity Analyst opportunities")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION MODE")
    print("=" * 60)
    
    # Simulate career counselling session
    queries = [
        "Should I become a DevOps Engineer?",
        "What does a Data Scientist do?",
        "How to become a Software Engineer?",
        "Machine Learning Engineer career path",
        "Cybersecurity Analyst opportunities"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{i}. Query: {query}")
        
        # Simulate web data fetching
        web_data = fetch_career_info_demo(query)
        print(f"   Web Data: {web_data}")
        
        # Simulate AI response
        ai_responses = [
            "Based on the data, DevOps Engineering is excellent for automation enthusiasts. Focus on CI/CD, cloud platforms, and infrastructure as code.",
            "Data Science offers great opportunities. Develop skills in Python, statistics, and machine learning. Consider certifications.",
            "Software Engineering requires strong programming fundamentals. Learn multiple languages and build portfolio projects.",
            "ML Engineering combines software development with ML expertise. Focus on model deployment and production systems.",
            "Cybersecurity is growing rapidly. Consider certifications like CompTIA Security+ and hands-on security projects."
        ]
        
        print(f"   AI Advice: {ai_responses[i-1]}")
        print(f"   Status: SUCCESS (Demo Mode)")
    
    print("\n" + "=" * 60)
    print("CAREER COUNSELLING FEATURES")
    print("=" * 60)
    print("• Real-time career data fetching")
    print("• AI-powered career advice")
    print("• Interactive chat interface")
    print("• Personalized recommendations")
    print("• Industry trend analysis")
    print("• Skill requirement insights")
    
    print("\n" + "=" * 60)
    print("TECHNICAL IMPLEMENTATION")
    print("=" * 60)
    print("• Web scraping with BeautifulSoup")
    print("• Gemini AI integration for advice")
    print("• Streamlit UI for user interaction")
    print("• Session state management")
    print("• Error handling for API calls")
    print("• Real-time data processing")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    career_counselling_demo()
